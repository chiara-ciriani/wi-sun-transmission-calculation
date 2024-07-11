# Transmission rate in kilobits per second
CR = 50 * 1000  # convert to bits per second


ACK_SIZE = 50 * 8  # convert bytes to bits


# Number of times the node will try to send the message
MAX_ATTEMPS = 10


# BINARY EXPONENTIAL BACKOFF
MIN_BACKOFF_EXPONENT = 2
MAX_BACKOFF_EXPONENT = 5


######## PHYSICAL LAYER ######## 

PREAMBLE_BITS = 32  # 4 bytes
SFD_BITS = 8  # 1 byte
PHR_BITS = 8  # 1 byte
PHY_OVERHEAD_BITS = PREAMBLE_BITS + SFD_BITS + PHR_BITS