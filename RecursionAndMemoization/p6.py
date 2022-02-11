import sys

# сделать граф состояний, по нему сделать разметку Гранди. Потом граф упразднить

# считает число Гранди для вершины графа
def grundy_function(table, v):
	neighbor_set = set([grundy_function(table, n) for n in table[v]])

	result = 0	
	while result in neighbor_set: result += 1
	return result

# строит граф
def solve(vs, table=None):
    if table is None:
        table = {}
    table[vs] = []
    for i, v in enumerate(vs):
        table[vs].extend([(
            *vs[:i], 
            *((j, v-j-2) if j != 0 else (v-j-2,)), 
            *vs[i+1:]) 
                for j in range(0, (v-2)//2+1)])
    for n_vs in table[vs]:
        solve(n_vs, table) 
    return table

N = (int(sys.stdin.read()),)
print(grundy_function(solve(N), N)) 