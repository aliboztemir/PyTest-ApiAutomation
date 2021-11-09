import datetime

from starlette.testclient import TestClient
from app.main import app
import json

client = TestClient(app)


def test_match_id_deliver_planned():
    # All deliveries from deliveries_for_planning.json that are in current_state planned are present in planned_route.json
    response_deliveries = client.get('/deliveries')
    input_dict_deliveries = json.loads(response_deliveries.text)
    output_dict_deliveries = [x['id'] for x in input_dict_deliveries if
                              x['current_state'] == 'planned']  # filter items with planned status

    response_route = client.get('/route')
    json_format_route = json.loads(response_route.text)
    output_dict_routes = [x['id'] for x in json_format_route['planned_route']['deliveries']]

    exist_list = list(filter(lambda x: x in output_dict_routes, output_dict_deliveries))

    def compare(s, t):
        return sorted(s) == sorted(t) #Compare two lists

    assert compare(exist_list, output_dict_deliveries)


def test_check_carrying_capacity():
    # The sum of weights of the deliveries is less than the carrying_capacity of the vehicle
    response_route = client.get('/route')
    input_dict_route = json.loads(response_route.text)

    carrying_capacity = input_dict_route['planned_route']['resource']['carrying_capacity']

    weights = [x['algorithm_fields']['weight'] for x in input_dict_route['planned_route']['deliveries'] if
               'weight' in x['algorithm_fields']] #Not all items have a weight value. That's why the if condition was added.

    assert carrying_capacity >= sum(weights)


def test_check_all_etas_min_max_route_time():
    # All eta-s of deliveries in planning (estimated time of arrivals) with “type” delivery are within the route_min_time and route_max_time
    response_route = client.get('/route')
    input_dict_route = json.loads(response_route.text)

    eta_list = [x['algorithm_fields']['eta'] for x in input_dict_route['planned_route']['deliveries'] if
                'eta' in x['algorithm_fields']]

    route_min_time = input_dict_route['planned_route']['route_min_time']
    route_max_time = input_dict_route['planned_route']['route_max_time']

    for val in eta_list:
        assert route_min_time <= val <= route_max_time


def test_check_all_etas_min_max_delivery_time():
    # All eta-s of deliveries in planning are within their delivery_min_time and delivery_max_time
    response_route = client.get('/route')
    input_dict_route = json.loads(response_route.text)

    eta_list = list([x['algorithm_fields']['eta'] for x in input_dict_route['planned_route']['deliveries'] if
                     'eta' in x['algorithm_fields']])

    min_time_list = list([x['min_time'] for x in input_dict_route['planned_route']['deliveries']])
    max_time_list = list([x['max_time'] for x in input_dict_route['planned_route']['deliveries']])

    assert len(eta_list) == len(min_time_list) == len(max_time_list)

    for i in range(len(eta_list)):
        assert min_time_list[i] <= eta_list[i] <= max_time_list[i]


def test_check_travel_time_to_next():
    # he travel_time_to next (in seconds) is less than or equal to the time difference between any 2 consecutive deliveries in “planned_route.json”
    response_route = client.get('/route')
    input_dict_route = json.loads(response_route.text)

    eta_list = list([x['algorithm_fields']['eta'] for x in input_dict_route['planned_route']['deliveries'] if
                     'eta' in x['algorithm_fields']])

    time_to_next_list = list(
        [x['algorithm_fields']['time_to_next'] for x in input_dict_route['planned_route']['deliveries'] if
         'time_to_next' in x['algorithm_fields']])

    assert len(eta_list) == len(time_to_next_list) + 1 #+1 because there is no "time_to_next" value in the last item.

    for i in range(len(time_to_next_list)):
        assert time_to_next_list[i] <= (
                datetime.datetime.strptime(eta_list[i + 1], "%Y-%m-%dT%H:%M:%S.%fZ") - datetime.datetime.strptime(
            eta_list[i], "%Y-%m-%dT%H:%M:%S.%fZ")).total_seconds() #String values are converted to datetime type.
