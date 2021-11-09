import json


def deliveries_for_planning():
    with open('data/deliveries_for_planning.json') as stream:
        deliveries = json.load(stream)

    return deliveries


def planned_routes():
    with open('data/planned_route.json') as stream:
        routes = json.load(stream)

    return routes