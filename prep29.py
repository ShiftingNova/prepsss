def sum_nums(thing):
    total = 0
    for i in thing:
        for e in i:
            if e < 10:
                total += e
    return total
