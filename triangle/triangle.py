def equilateral(sides):
    return all(i > 0 for i in sides) and sides.count(sides[0]) == 3


def isosceles(sides):
    return all(i > 0 for i in sides) and (len(set(sides)) <= 2) and (sum(sides) - max(sides) >= max(sides))


def scalene(sides):
    return all(i > 0 for i in sides) and (len(set(sides)) == 3) and (sum(sides) - max(sides) >= max(sides))
