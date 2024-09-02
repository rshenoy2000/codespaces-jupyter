

import sys


def minMax(a: list[int]) -> tuple[int, int]: 
    size_a = len(a)
    (min_val, max_val) = (sys.maxsize,-sys.maxsize)
    start = 0
    if (size_a % 2 == 1):
        (min_val, max_val) = (a[0], a[0])
        start = 1
    
    for i in range(start, size_a-1, 2):
        if  a[i] <= a[i+1] :
            (min_, max_) = (a[i], a[i+1])
        else:
            (min_, max_) = (a[i+1], a[i])
          
        (min_val, max_val) = (min(min_, min_val), max(max_, max_val))
          
    return (min_val, max_val)

def main():
     print(minMax([1, 4, 5, 6, -1, 100]))

if __name__ == "__main__":
    main()