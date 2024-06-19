import random

def generate_channel_pattern(num_channels):
    # Generate a random permutation of channels
    pattern = list(range(1, num_channels + 1))
    random.shuffle(pattern)
    return pattern

def generate_schedule(channel_pattern, dwell_interval, length):
    schedule = []
    time = 0
    for i in range(length):
        channel = channel_pattern[i % len(channel_pattern)]
        schedule.append((time, channel))
        time += dwell_interval
    return schedule

def obtain_frequency_hopping_schedules(nodes, num_channels, unicast_dwell_interval, num_unicast_slots, broadcast_dwell_interval, num_broadcast_slots):
    unicast_schedule = {}
    broadcast_schedule = {}

    # Generate a single channel pattern for broadcast
    broadcast_channel = 0

    for node in nodes:
        # Generate channel patterns for unicast
        unicast_pattern = generate_channel_pattern(num_channels)

        # Generate schedules based on patterns
        unicast_schedule[node] = generate_schedule(unicast_pattern, unicast_dwell_interval, num_unicast_slots)
        broadcast_schedule[node] = [(i * broadcast_dwell_interval, broadcast_channel) for i in range(num_broadcast_slots)]

    return unicast_schedule, broadcast_schedule

# BUSCAR Y PONER CON LOGICA CUANDO ES EL SCHEDULE Y CUANTO TIEMPO

# INVOLUCRAR LOGICA DE NUM_CHANNELS ?? DEBE AFECTAR EN ALGO