from constants import ACK_SIZE, CR, MAX_ATTEMPS, MAX_BACKOFF_EXPONENT
import random

def calculate_packet_time(packet_size):
    packet_time = (packet_size / CR) * 1000  # convert to ms
    return packet_time

def calculate_ack_time():
    ack_time = (ACK_SIZE / CR) * 1000  # convert to ms
    return ack_time

def calculate_transmission_time(route, CCA, CCA_probability_failure, packet_size, GUARD_TIME):
    num_hops = len(route) - 1 
    packet_time = calculate_packet_time(packet_size)
    ack_time = calculate_ack_time()
    
    total_time = 0

    for hop in range(num_hops):
        attemps = 0
        backoff_exponent = 0

        while attemps < MAX_ATTEMPS:
            total_time += CCA  # Time it takes to check if channel is free

            attemps += 1
        
            # Simulate CCA
            if random.random() > CCA_probability_failure:
                # Channel is sensed to be idle, so transmit immediately
                total_time += packet_time + ack_time + GUARD_TIME
                break    # The message has already been transmitted
            else:
                # Channel is sensed to be busy
                if backoff_exponent < MAX_BACKOFF_EXPONENT:
                    # Wait for a random backoff time
                    backoff_time = random.randint(0, 2 ** backoff_exponent - 1)
                    total_time += backoff_time
                    backoff_exponent += 1
                else:
                    # Maximum number of backoffs reached, cancel transmission
                    print("Max backoff attempts reached. Transmission cancelled.")
                    return total_time, route[:hop]
                
            if attemps == MAX_ATTEMPS:
                print("Max transmissions attempts reached. Transmission cancelled.")
                return total_time, route[:hop]

    return total_time, route