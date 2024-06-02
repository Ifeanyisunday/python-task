switch_state = bool()
temperature = 16


def on(switch):
    if not switch:
        switch = True
        return switch


def off(switch):
    switch = False
    return switch


def temperature_increase_but_not_beyond_30(temperature_value):
    if 16 <= temperature_value <= 30:
        temperature_value += 1
    if temperature_value >= 30:
        temperature_value = 30
    else:
        return temperature_value
    return temperature_value


def temperature_decrease_but_not_below_16(temperature_value):
    if 16 <= temperature_value <= 30:
        temperature_value -= 1
    if temperature_value <= 16:
        temperature_value = 16
    else:
        return temperature_value
    return temperature_value
