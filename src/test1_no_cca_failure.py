from calculations import calculate_transmission_time
from fr_schedules import obtain_frequency_hopping_schedules

CCA = 150                         # ms
CCA_PROBABILITY_FAILURE = 0

PACKET_RECEIVED_PROBABILITY = 0
RECEIVER_NOT_IN_CHANNEL_PROBABILITY = 0

NUM_CHANNELS = 3

UNICAST_DWELL_INTERVAL = 50
BROADCAST_DWELL_INTERVAL = 100

NUM_UNICAST_SLOTS = 10
NUM_BROADCAST_SLOTS = 3


GUARD_TIME = 3                    # ms
PACKET_SIZE = 1280 * 8            # convert bytes to bits

if __name__ == "__main__":
    # Nodes in the network
    nodes = list(range(1, 12))   # 1 to 11

    route_1 = [1, 6, 9, 11, 9, 6, 2, 6, 9, 11, 9, 7, 3, 6, 9, 11, 10, 8, 4, 6, 9, 11, 10, 8, 5]
    route_2 = [1, 2, 2, 3, 2, 3, 4, 2, 3, 4, 5]
    route_3 = [1, 2, 3, 4, 5]

    unicast_schedule, broadcast_schedule = obtain_frequency_hopping_schedules(nodes, NUM_CHANNELS, UNICAST_DWELL_INTERVAL, NUM_UNICAST_SLOTS, BROADCAST_DWELL_INTERVAL, NUM_BROADCAST_SLOTS)

    print("")
    print(f"Unicast schedule: {unicast_schedule}")
    print("")
    print(f"Broadcast schedule: {broadcast_schedule}")
    print("")
    print("")

    # Calculate transmission times for each route 
    # Print the results

    ## print("The packet will be send using RPL operation")
    ## print("")
    ## time_route1, _ = calculate_transmission_time(route_1, CCA, CCA_PROBABILITY_FAILURE, PACKET_SIZE, GUARD_TIME, PACKET_RECEIVED_PROBABILITY, RECEIVER_NOT_IN_CHANNEL_PROBABILITY, unicast_schedule, broadcast_schedule, NUM_CHANNELS, UNICAST_DWELL_INTERVAL, BROADCAST_DWELL_INTERVAL)
    ## print("")
    ## print(f"Transmission time for RPL Operation: {time_route1:.2f} ms")
## 
    ## print("")
    ## print("")
## 
    ## print("The packet will be send using the Projected DAO Draft operation")
    ## print("")
    ## time_route2, _ = calculate_transmission_time(route_2, CCA, CCA_PROBABILITY_FAILURE, PACKET_SIZE, GUARD_TIME, PACKET_RECEIVED_PROBABILITY, RECEIVER_NOT_IN_CHANNEL_PROBABILITY, unicast_schedule, broadcast_schedule, NUM_CHANNELS, UNICAST_DWELL_INTERVAL, BROADCAST_DWELL_INTERVAL)
    ## print("")
    ## print(f"Transmission time for Projected DAO Draft: {time_route2:.2f} ms")
## 
    ## print("")
    ## print("")

    print("The packet will be send using the Projected DAO Draft and RPL Multicast operation")
    print("")
    time_route3, _ = calculate_transmission_time(route_3, CCA, CCA_PROBABILITY_FAILURE, PACKET_SIZE, GUARD_TIME, PACKET_RECEIVED_PROBABILITY, RECEIVER_NOT_IN_CHANNEL_PROBABILITY, unicast_schedule, broadcast_schedule, NUM_CHANNELS, UNICAST_DWELL_INTERVAL, BROADCAST_DWELL_INTERVAL)
    print("")
    print(f"Transmission time for Projected DAO Draft and RPL Multicast: {time_route3:.2f} ms")