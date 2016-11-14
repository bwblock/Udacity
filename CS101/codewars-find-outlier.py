def find_outlier(integers):
    odds = [i for i,x in enumerate(integers) if x %2 == 1]
    evens = [i for i,x in enumerate(integers) if x%2 == 0]
    return integers[odds[0]] if len(evens) > 1 else integers[evens[0]]