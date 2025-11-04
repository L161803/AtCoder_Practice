#ABC083B - Some Sums
N, A, B = map(int, input().split())
total = 0
for i in range(1, N+1):
    array = list(str(i))
    tmp = sum(map(int, array))
    if A<=tmp and tmp<=B:total += i

print(total)

#改善リスト内包ver
def digit_sum(x: int)->int:
    return sum(map(int, str(x)))

total = sum(i for i in range(1, N+1) if A<=digit_sum(i)<=B)
print(total)