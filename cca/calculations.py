from constants import ACK_SIZE, CR, MAX_ATTEMPS, MIN_BACKOFF_EXPONENT, MAX_BACKOFF_EXPONENT
import random

def calculate_packet_time(packet_size):
    packet_time = (packet_size / CR) * 1000  # convert to ms
    return packet_time

def calculate_ack_time():
    ack_time = (ACK_SIZE / CR) * 1000  # convert to ms
    return ack_time

def calculate_transmission_time(num_hops, CCA, CCA_probability_failure, packet_size, GUARD_TIME, packet_received_probability):
    packet_time = calculate_packet_time(packet_size)
    ack_time = calculate_ack_time()
    
    total_time = 0

    for hop in range(num_hops):
        attemps = 0
        backoff_exponent = MIN_BACKOFF_EXPONENT

        while attemps < MAX_ATTEMPS:
            while backoff_exponent < MAX_BACKOFF_EXPONENT:
                # Wait for a random backoff time
                backoff_time = random.randint(0, 2 ** backoff_exponent - 1)
                total_time += backoff_time
                backoff_exponent += 1

                # Simulate node receiving a packet in his channel
                if random.random() < packet_received_probability:
                    total_time += calculate_packet_time(packet_size)  # capaz mejor otro valor que packet_size 
                    # capaz falte sumar algo --- revisar
                    backoff_exponent = MIN_BACKOFF_EXPONENT

            total_time += CCA  # Time it takes to check if channel is free

            attemps += 1
        
            # Simulate CCA
            if random.random() > CCA_probability_failure:
                # Channel is sensed to be idle, so transmit immediately
                total_time += packet_time + ack_time + GUARD_TIME
                break    # The message has already been transmitted
                
            if attemps == MAX_ATTEMPS:
                print("Max transmissions attempts reached. Transmission cancelled.")
                return total_time, hop

    return total_time, num_hops

# DUDAS:

# - Countdown must freeze??