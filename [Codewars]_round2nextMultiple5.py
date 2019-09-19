def round_to_next5(n):
    if n%5 != 0:
      a = n + 5- (n%5)
      return a

    else:
      return n
