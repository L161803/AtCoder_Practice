import sys
input = sys.stdin.read
data = input().split()

iterator = iter(data)
N = int(next(iterator))
M = int(next(iterator))

ans = 0
ocu = set()

for _ in range(M):
    r = int(next(iterator))
    c = int(next(iterator))

    target_cells = [
        (r, c),
        (r + 1, c),
        (r, c + 1),
        (r + 1, c + 1)
    ]

    can_place = True
    for cell in target_cells:
        if cell in ocu:
            can_place = False
            break

    if can_place:
        ans += 1

        for cell in target_cells:
            ocu.add(cell)

print(ans)