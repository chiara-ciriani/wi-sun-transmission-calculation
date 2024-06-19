from fr_schedules import obtain_frequency_hopping_schedules

NUM_CHANNELS = 5

UNICAST_DWELL_INTERVAL = 50
BROADCAST_DWELL_INTERVAL = 100

NUM_UNICAST_SLOTS = 10
NUM_BROADCAST_SLOTS = 3

if __name__ == "__main__":
    # Nodes in the network
    nodes = list(range(1, 12))   # 1 to 11

    route_1 = [1, 6, 9, 11, 9, 6, 2, 6, 9, 11, 9, 7, 3, 6, 9, 11, 10, 8, 4, 6, 9, 11, 10, 8, 5]
    route_2 = [1, 2, 2, 3, 2, 3, 4, 2, 3, 4, 5]
    route_3 = [1, 2, 3, 4, 5]

    unicast_schedule, broadcast_schedule = obtain_frequency_hopping_schedules(nodes, NUM_CHANNELS, UNICAST_DWELL_INTERVAL, NUM_UNICAST_SLOTS, BROADCAST_DWELL_INTERVAL, NUM_BROADCAST_SLOTS)

    print(unicast_schedule)
    print("")
    print("")
    print(broadcast_schedule)

    # HACER TEST PARA MANTENER QUE SIEMPRE ANDE POR SI FALLA ALGO
    # PERO QUE SEA TEST MAS CHICO