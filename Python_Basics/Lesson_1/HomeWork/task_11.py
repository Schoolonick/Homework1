m, h = int(input()), int(input())
I = lambda: print(round(m / (h * h) * 10 ** 4, 2))
"""
< 16 very bad
  16 - 18.5 bad
  18.5 - 25 norm
  25 - 30 fat
  30 - 35 fatty one-degree
  35 - 40 fatty two-degree
> 40 GG
"""
if __name__ == "__main__":
    I()
