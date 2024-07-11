# The time that the channel will be busy sending messages.
def calculate_channel_occupation_time(transmission_count, transmission_time):
    return transmission_count * transmission_time

# The time when the last street light receives the last message.
def calculate_maximum_delay(approach, num_street_lights, transmission_time, num_hops_to_root=0, num_hops_from_root=0):
    if approach == "STANDARD_RPL":
        return ((num_hops_to_root + num_hops_from_root) * transmission_time) * (num_street_lights - 1)
    
    elif approach == "ALTERNATIVE_STANDARD_RPL":
        return (num_hops_to_root * transmission_time) + ((num_street_lights - 1) * (num_hops_from_root * transmission_time))
    
    elif approach == "PROJECTED_ROUTES":
        return ((num_street_lights * (num_street_lights - 1)) / 2) * transmission_time
    
    # Proposed Solution
    return (num_street_lights - 1) * transmission_time