def get_middle(s):
    l = len(s)
    if l % 2 == 0:
      return s[l/2-1:(l/2)+1]
    else:
      return s[int(l/2)]
      
      
      
      