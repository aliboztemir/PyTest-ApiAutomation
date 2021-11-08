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


    for val in output_dict_deliveries:
        print(val in json_format_route['planned_route']['deliveries'])

def test_check_carrying_capacity():
    response_route = client.get('/route')
    input_dict_route = json.loads(response_route.text)
    output_dict_route = input_dict_route['planned_route']['deliveries']['algorithm_fields']['algorithm_fields']['weight']
    print(output_dict_route)
    #print(sum(info['weight'] for info in input_dict_route['planned_route']['deliveries']['algorithm_fields']['algorithm_fields']))





