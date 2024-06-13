from calculations import calculate_transmission_time

CCA = 150                         # ms
CCA_PROBABILITY_FAILURE = 0.8
GUARD_TIME = 3                    # ms
PACKET_SIZE = 1280 * 8            # convert bytes to bits

if __name__ == "__main__":
    # Nodes in the network
    nodes = list(range(1, 27))   # 1 to 26

    # Possible routes from 17 to 21
    route1 = [17, 13, 14, 15, 21]
    route2 = [17, 18, 19, 20, 21]
    route3 = [17, 12, 7, 2, 1, 6, 11, 16, 21]

    # Calculate transmission times for each route
    # Print the results
    time_route1, route_completed1 = calculate_transmission_time(route1, CCA, CCA_PROBABILITY_FAILURE, PACKET_SIZE, GUARD_TIME)
    print(f"Transmission time for route {route1}: {time_route1:.2f} ms, route: {route_completed1}")

    time_route2, route_completed2 = calculate_transmission_time(route2, CCA, CCA_PROBABILITY_FAILURE, PACKET_SIZE, GUARD_TIME)
    print(f"Transmission time for route {route2}: {time_route2:.2f} ms, route: {route_completed2}")

    time_route3, route_completed3 = calculate_transmission_time(route3, CCA, CCA_PROBABILITY_FAILURE, PACKET_SIZE, GUARD_TIME)
    print(f"Transmission time for route {route3}: {time_route3:.2f} ms, route: {route_completed3}")
