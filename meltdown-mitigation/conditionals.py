"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = generated_power/theoretical_max_power
    if efficiency * 100 >= 80:
        return 'green'
    if 60 <= efficiency * 100 < 80:
        return 'orange'
    if 30 <= efficiency * 100 < 60:
        return 'red'
    return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    criticality = temperature * neutrons_produced_per_second
    if criticality < 0.9 * threshold:
        return 'LOW'
    if threshold * 0.9 <= criticality < threshold * 1.1:
        return 'NORMAL'
    return 'DANGER'
