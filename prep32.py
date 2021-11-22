def get_common_movies(list):
    common = []
    for i in range(len(list)-1):
        current = list[i]
        for e in current:
            if e in list[i+1]:
                if e not in common:
                    common.append(e)
    thing = set(common)
    return thing
