def maxSequence(arr):
    max = 0
    long = len(arr)
    for i range(long):
      for j in range(long):
        if j > i:
          test = sum(arr[i:j])
          if test > max:
            max = test
    return max