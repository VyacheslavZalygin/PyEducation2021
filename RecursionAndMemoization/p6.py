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
    for i, v in enumerate(vs):
        table[vs] = [(
            *vs[:i], 
            *((j, v-j-2) if j != 0 else (v-j-2,)), 
            *vs[i+1:]) 
                for j in range(0, (v-2)//2+1)]
    a = set()
    for n_vs in table[vs]:
        if n_vs not in table:
            a.add(solve(n_vs, table))
    res = 0
    while res in a: res += 1 
    return res

N = (int(sys.stdin.read()),)
print(2 if solve(N) == 0 else 1)