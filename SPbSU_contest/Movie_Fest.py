n = int(input())
films = []
for i in range(n):
    film = list(map(int, input().split()))
    films.append(film)

res_films = [[0,0]]
res_cnt = 0

films = sorted(films, key=lambda x: x[1])

for st, fn in films:
    if st >= res_films[-1][1]:
        res_films.append([st, fn])
        res_cnt += 1

print(res_cnt)