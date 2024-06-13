import argparse
import sys

from calculations import calculate_transmission_time, calculate_probability_of_collision

CCA = 150                 # ms
GUARD_TIME = 3            # ms
PACKET_SIZE = 1280 * 8    # convert bytes to bits

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculates the unicast transmission time of a message from node 17 to 21")
    parser.add_argument("--number_of_nodes", default=10, type=int, help="Number of nodes in the network (default: 10)")
    parser.add_argument("--traffic_load", default=100, type=int, help="Traffic profile in the network (default: 100)")
    parser.add_argument("--propagation_range", default=50, type=int, help="Propagation range of a node (default: 50)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show detailed information (optional)")
    args, unknown = parser.parse_known_args()

    if unknown:
        print(f"Error: Unrecognized parameters: {unknown}")
        sys.exit(1)

    # Nodes in the network
    nodes = list(range(1, args.number_of_nodes + 1))   

    # VER COMO HAGO LO DE HOP
    # Possible routes from 17 to 21
    route1 = [17, 13, 14, 15, 21]
    route2 = [17, 18, 19, 20, 21]
    route3 = [17, 12, 7, 2, 1, 6, 11, 16, 21]

    # Calculate the probability of a collision in the channel
    CCA_probability_collision = calculate_probability_of_collision(args.number_of_nodes, args.traffic_load, args.propagation_range)

    # Calculate transmission times for each route
    time_route1 = calculate_transmission_time(route1, CCA,  CCA_probability_collision, PACKET_SIZE, GUARD_TIME)
    time_route2 = calculate_transmission_time(route2, CCA,  CCA_probability_collision, PACKET_SIZE, GUARD_TIME)
    time_route3 = calculate_transmission_time(route3, CCA,  CCA_probability_collision, PACKET_SIZE, GUARD_TIME)

    # Print results
    print(f"Transmission time for route {route1}: {time_route1:.2f} ms")
    print(f"Transmission time for route {route2}: {time_route2:.2f} ms")
    print(f"Transmission time for route {route3}: {time_route3:.2f} ms")
