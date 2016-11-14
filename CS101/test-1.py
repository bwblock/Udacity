#! /usr/bin/env python
def unflatten(flat_array):
    result = []
    for e in range(len(flat_array)):
      if flat_array[e] < 3:
        result.append(flat_array[e])
      if flat_array[e] > 2:
        if len(flat_array) >= e + flat_array[e]:
          result.append(flat_array[e:e+flat_array[e]])
        else:
          result.append(flat_array[e:]
    return result

unflatten([ 3, 5, 2, 1 ])
