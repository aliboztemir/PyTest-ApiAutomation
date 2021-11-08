from starlette.testclient import TestClient
from app.main import app
import json

client = TestClient(app)


def test_read_main():
    response_deliveries = client.get('/deliveries')
    input_dict_deliveries = json.loads(response_deliveries.text)
    output_dict_deliveries = [x['id'] for x in input_dict_deliveries if x['current_state'] == 'planned']

    response_route = client.get('/route')
    json_format_route = json.loads(response_route.text)


    for val in output_dict_deliveries:
        print(val in json_format_route['planned_route']['deliveries'])



