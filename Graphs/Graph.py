def main():
    g = { 'a': { 'b': 0, 'd': 0, 'c': 0 },
          'b': { },
          'd': { 'c': 0, 'e': 0},
          'e': { },
          'c': { 'e': 0 } }
    t = {}
    for v in g:
        top_sort(g, t, v)
    print(t)
    # a = {}
    # for v in t:
    #     if not t[v] in a:
    #         a[t[v]] = []
    #     a[t[v]].append(v)
    # sorted(a)
    # print(a)

def top_sort(g, table, v):
    # проверять, что в t еще нет v
    if not v in table:
        p = [top_sort(g, table, x) for x in g[v]]
        if len(p) != 0:
            table[v] = 1 + max(p)
        else:
            table[v] = 0
    return table[v]

main()