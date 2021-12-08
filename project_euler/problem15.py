from math import factorial

def solution(n: int = 20) -> int:
    n = 2 * n
    k = n // 2
    
    return int(factorial(n) / (factorial(k) * factorial(n -k)))

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 1:
        print(solution(20))
    else:
        try:
            n = int(sys.argv[1])
            print(solution(n))
        except ValueError:
            print('error number')