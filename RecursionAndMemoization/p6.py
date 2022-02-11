import sys

# сделать граф состояний, по нему сделать разметку Гранди. Потом граф упразднить

# считает число Гранди для вершины графа
def grundy_function(table, v):
	neighbor_set = set([grundy_function(table, n) for n in table[v]])
	
	result = 0	
	while result in neighbor_set: result += 1
	return result

# строит граф
def solve(vs):
    a = []
    a = [[(*vs[:i],  *((j, v-j-2) if j != 0 else (v-j-2,)), *vs[i+1:]) 
            for j in range(0, (v-2)//2+1)] for i, v in enumerate(vs)]
    b = set()
    for n_vs in a:
        b.add(solve(n_vs))
    res = 0
    while res in b: res += 1
    return res

N = (int(sys.stdin.read()),)
print(solve(N))