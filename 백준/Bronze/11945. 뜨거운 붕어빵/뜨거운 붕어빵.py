N, M = map(int, input().split())

fish = []
for i in range(N):
  fish.append(input())

for i in fish:
  print(i[::-1])