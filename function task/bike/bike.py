bike_switch_state = bool()
speed_value = 15


def bike_switch_on():
    if not bike_switch_state:
        return True


def bike_switch_off():
    if bike_switch_state:
        return False


def accelerate(speed_number):
    if 0 <= speed_number <= 20:
        speed_number += 1
    elif 21 <= speed_number <= 30:
        speed_number += 2
    elif 31 <= speed_number <= 40:
        speed_number += 3
    else:
        speed_number += 4
    return speed_number


def decelerate(speed_number):
    if 0 <= speed_number <= 20:
        speed_number -= 1
    elif 21 <= speed_number <= 30:
        speed_number -= 2
    elif 31 <= speed_number <= 40:
        speed_number -= 3
    else:
        speed_number -= 4
    return speed_number


def get_gear(speed_number):
    if 0 <= speed_number <= 20:
        return "Gear 1"
    elif 21 <= speed_number <= 30:
        return "Gear 2"
    elif 31 <= speed_number <= 40:
        return "Gear 3"
    else:
        return "Gear 4"


def change_gear_level(speed_number):
    return get_gear(speed_number)
