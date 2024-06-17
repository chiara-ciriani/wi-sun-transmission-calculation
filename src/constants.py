# Transmission rate in kilobits per second
CR = 50 * 1000  # convert to bits per second


ACK_SIZE = 50 * 8  # convert bytes to bits


# Number of times the node will try to send the message
MAX_ATTEMPS = 10


# BINARY EXPONENTIAL BACKOFF
MIN_BACKOFF_EXPONENT = 2
MAX_BACKOFF_EXPONENT = 5