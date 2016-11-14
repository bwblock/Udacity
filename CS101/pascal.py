def pascal(p):
    result = []
    oldlist = [1]
    newlist = []
    j = 2
    while j <= p:
      s = range(j)
      s.pop()
      del s[0]
      newlist.append(oldlist[0])
      if s:
        for i in s:
          newlist.append(oldlist[i]+oldlist[i-1])
      newlist.append(oldlist[len(oldlist)])
      result.append(newlist)
      oldlist = newlist
      newlist = []
      j += 1
    return result