"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    remaining = EXPECTED_BAKE_TIME - int(elapsed_bake_time)
    print(str(remaining) + ' minutes remaining.')
    return remaining


def preparation_time_in_minutes(number_of_layers):
    total_time = number_of_layers * 2
    print(str(total_time) + ' minutes.')
    return total_time


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    total_process = number_of_layers * 2 + elapsed_bake_time
    print('Elapsed time: ' + str(total_process) + ' minutes.')
    return total_process
