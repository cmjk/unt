from enum import Enum


class OrderBy(Enum):
    """
    Corresponds to Sort By options in the UI
    """
    default = 0
    a_to_z = 5
    z_to_a = 6
    price_low_to_high = 10
    price_high_to_low = 11
    created_on = 15
