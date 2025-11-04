N, M = map(int, input().split())
S = [input() for n in range(N)]
block = set()

for i in range(N - M + 1):
  for j in range(N - M + 1):
      pattern = ''
      for k in range(M):
          pattern += S[i + k][j:j + M]
      block.add(pattern)

print(len(block))