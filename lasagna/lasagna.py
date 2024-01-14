"""Functions used in preparing Guido's gorgeous lasagna.

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40


# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining = EXPECTED_BAKE_TIME - int(elapsed_bake_time)
    print(str(remaining) + ' minutes remaining.')
    return remaining




# TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    total_time = number_of_layers * 2
    print(str(total_time) + ' minutes.')
    return total_time




# TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
       Calculate the total elapsed time based on the number of layers and elapsed bake time.

       :param number_of_layers: int - The number of layers in the baking process, multiplied by the time it takes to
       prepare them.
       :param elapsed_bake_time: int - The time already elapsed in the baking process.
       :return: int - The total elapsed time in minutes.

       Function that takes the number of layers and the time of their preparation and the time already elapsed in the
       baking process as arguments and returns the total elapsed time in minutes.
       """
    total_process = number_of_layers * 2 + elapsed_bake_time
    print('Elapsed time: ' + str(total_process) + ' minutes.')
    return total_process

