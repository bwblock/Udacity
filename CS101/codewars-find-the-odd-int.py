def find_it(seq):
    for e in seq:
      if seq.count(e) % 2 != 0:
        return e
    return None