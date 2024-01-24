"""Functions for calculating steps in exchaning currency."""


def exchange_money(budget, exchange_rate):
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    new_value = budget / (exchange_rate + (exchange_rate *
                                           (spread / 100)))
    value_by_denomination = (new_value // denomination) * denomination
    return int(value_by_denomination)
