import sys

N, M = map(int, sys.stdin.readline().split())

pokemon_dict = {}
pokemon_dict_number = {}

for i in range(N):
    pokemon = str(sys.stdin.readline().rstrip())
    pokemon_dict[i + 1] = pokemon
    pokemon_dict_number[pokemon] = i + 1
    
for _ in range(M):
    problem = str(sys.stdin.readline().rstrip())
    try:
        print(pokemon_dict[int(problem)])
    except:
        print(pokemon_dict_number[problem])

