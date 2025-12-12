from collections import defaultdict

def solve():
    N, M = map(int, input().split())
    A = list(map(int,input().split()))


    counts = [defaultdict(int) for _ in range(11)]

    for x in A:
        d = len(str(x)) 
        r = x % M       
        counts[d][r] += 1

    ans = 0

    for x in A:
        for k in range(1, 11):
            # 条件: (x * 10^k + y) % M == 0
            # 変形: y % M == (-x * 10^k) % M
            
            left_rem = (x * pow(10, k, M)) % M
            target = (M - left_rem) % M
            ans += counts[k][target]
    
    print(ans)

if __name__ == '__main__':
    solve()