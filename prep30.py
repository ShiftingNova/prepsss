def longest_string(list):
    count = 0
    for i in list:
        for e in i:
            if len(i[e]) > count:
                count = len(i[e])
                words = i[e]
    return words
