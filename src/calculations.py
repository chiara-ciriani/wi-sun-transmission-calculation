from constants import ACK_SIZE, CR, MAX_ATTEMPS, MIN_BACKOFF_EXPONENT, MAX_BACKOFF_EXPONENT, PHY_OVERHEAD_BITS
import random

def calculate_packet_time(packet_size):
    total_bits = packet_size * 8 + PHY_OVERHEAD_BITS  # Convert packet size to bits and add PHY overhead
    packet_time = (total_bits / CR) * 1000  # convert to ms
    return packet_time

def calculate_ack_time():
    ack_bits = ACK_SIZE * 8 + PHY_OVERHEAD_BITS  # Convert ACK size to bits and add PHY overhead
    ack_time = (ack_bits / CR) * 1000  # convert to ms
    return ack_time

def calculate_transmission_time(route, CCA, CCA_probability_failure, packet_size, GUARD_TIME, packet_received_probability, receiver_node_not_in_channel_probability, unicast_schedule, broadcast_schedule, num_channels, unicast_dwell_interval, broadcast_dwell_interval):
    num_hops = len(route) - 1
    packet_time = calculate_packet_time(packet_size)
    ack_time = calculate_ack_time()
    
    total_time = 0

    for hop in range(num_hops):
        attemps = 0
        backoff_exponent = MIN_BACKOFF_EXPONENT

        transmitter = route[hop]
        receiver = route[hop + 1]

        print(f"Sending packet from {transmitter} to {receiver}")
        print(f"Total time: {total_time}")


        while attemps < MAX_ATTEMPS:
            attemps += 1

            print(f"Attemp: {attemps}")

            # Wait a random backoff time
            while backoff_exponent < MAX_BACKOFF_EXPONENT:
                print(f"Waiting a random backoff time...")
                # Wait for a random backoff time
                backoff_time = random.randint(0, 2 ** backoff_exponent - 1)
                total_time += backoff_time
                backoff_exponent += 1
                print(f"Backoff time: {backoff_time}")

                # Simulate node receiving a packet in his channel
                if random.random() < packet_received_probability:
                    print(f"Nodes receives a packet in his channel while waiting")
                    total_time += calculate_packet_time(packet_size)  # capaz mejor otro valor que packet_size 
                    # capaz falte sumar algo --- revisar
                    backoff_exponent = MIN_BACKOFF_EXPONENT

            print(f"Total time: {total_time}")

            total_time += CCA  # Time it takes to check if channel is free
            print(f"Checking is channel is free (CCA)...")
            print(f"Total time: {total_time}")
        
            # Simulate CCA
            if random.random() > CCA_probability_failure:
                print(f"Channel is free :)")

                print(f"Checking if broadcast channel is valid in the broadcast schedule")
                # Check if the broadcast channel is valid in the broadcast schedule
                broadcast_active = False
                for start_time, _ in broadcast_schedule[receiver]:
                    if start_time <= total_time < start_time + broadcast_active:
                        # Broadcast channel is currently active
                        broadcast_active = True
                        wait_time = (start_time + broadcast_active) - total_time
                        total_time += wait_time

                        print(f"Broadcast channel is active, so it has to wait: {wait_time}")
                        print(f"Total time: {total_time}")
                        ## break             ## DUDAAAAA
                    
                ## DUDA: si el canal de broadcast esta activo, se tiene que a hacer el backoff y todo otra vez?
                ## o solo espera el tiempo
                # PREGUNTAR ESTOO
                ## if broadcast_active:
                ##     continue  # Skip the rest and re-check the broadcast schedule

                print(f"Total time: {total_time}")

                # Channel is sensed to be idle
                # Check if the receiver is on the channel
                if random.random() > receiver_node_not_in_channel_probability:
                    # Channel is sensed to be idle and receiver is on the channel, so transmit immediately
                    total_time += packet_time + ack_time + GUARD_TIME
                    
                    print(f"Receiver is in the channel :)")
                    print(f"Message is transmitted")
                    print(f"Total time: {total_time}")

                    break    # The message has already been transmitted
                else:
                    backoff_exponent = MIN_BACKOFF_EXPONENT   # Reset backoff exponent
                    print(f"Receiver is not in the channel :(")
            else:
                print(f"Channel is not free :(")
                
            if attemps == MAX_ATTEMPS:
                print("Max transmissions attempts reached. Transmission cancelled.")
                return total_time, hop

    return total_time, num_hops
