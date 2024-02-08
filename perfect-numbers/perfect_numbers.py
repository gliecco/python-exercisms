def divisors(number):
    divisor_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisor_list.append(i)
    return divisor_list


def classify(number):
    if number < 1:
        raise ValueError(
            'Classification is only possible for positive integers.')

    if sum(divisors(number)) == number * 2:
        return 'perfect'

    if sum(divisors(number)) < number * 2:
        return 'deficient'

    return 'abundant'
