from collections import Counter

from starlette.testclient import TestClient
from app.main import app
import json

client = TestClient(app)


def test_match_id_deliver_planned():
    response_deliveries = client.get('/deliveries')
    input_dict_deliveries = json.loads(response_deliveries.text)
    output_dict_deliveries = [x['id'] for x in input_dict_deliveries if x['current_state'] == 'planned']

    response_route = client.get('/route')
    json_format_route = json.loads(response_route.text)
    output_dict_routes = [x['id'] for x in json_format_route['planned_route']['deliveries']]

    print("Planned Routes")
    for val in output_dict_routes:
        print(val)

    print("Delivery List")
    for val in output_dict_deliveries:
        print(val)

    exist_list = list(filter(lambda x: x in output_dict_routes, output_dict_deliveries))
    print("exist_list")

    for val in exist_list:
        print(val)

    def compare(s, t):
        return sorted(s) == sorted(t)

    assert compare(exist_list, output_dict_deliveries)


def test_check_carrying_capacity():
    response_route = client.get('/route')
    input_dict_route = json.loads(response_route.text)

    carrying_capacity = input_dict_route['planned_route']['resource']['carrying_capacity']
    print("carrying_capacity :", carrying_capacity)

    print("weights")
    weights = [x['algorithm_fields']['weight'] for x in input_dict_route['planned_route']['deliveries'] if
               'weight' in x['algorithm_fields']]
    for val in weights:
        print(val)
    print("sum", sum(weights))

    assert carrying_capacity >= sum(weights)


def test_check_all_etas_min_max_route_time():
    response_route = client.get('/route')
    input_dict_route = json.loads(response_route.text)

    print("eta_list")
    eta_list = [x['algorithm_fields']['eta'] for x in input_dict_route['planned_route']['deliveries'] if
                'eta' in x['algorithm_fields']]
    for val in eta_list:
        print(val)

    route_min_time = input_dict_route['planned_route']['route_min_time']
    print("route_min_time: ", route_min_time)
    route_max_time = input_dict_route['planned_route']['route_max_time']
    print("route_max_time: ", route_max_time)

    for val in eta_list:
        assert route_min_time <= val <= route_max_time
