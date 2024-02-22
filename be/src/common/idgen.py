import time
import random
from datetime import datetime


def generate_new_id() -> int:
    # Unix Nano seconds for August 1, 2015
    epoch_nanosecond = int(datetime(2015, 8, 1, 0, 0, 0).timestamp() * 1e9)

    # Current time in Nano seconds
    now_nanosecond = int(time.time() * 1e9)
    millisecond = (now_nanosecond - epoch_nanosecond) // int(1e6)
    system_no = 2
    unused = 0

    # 16384 is the maximum number representable with 14 bits
    random_no = random.randint(0, 16383)

    id_bits = (
        (0 << (64 - (0 + 1))) |
        (millisecond << (64 - (1 + 41))) |
        (system_no << (64 - (42 + 2))) |
        (unused << (64 - (44 + 6))) |
        (random_no << (64 - (50 + 14)))
    )

    return id_bits

