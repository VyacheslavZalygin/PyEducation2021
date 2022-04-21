def parity(expected):
    def filter(x):
        return x % 2 == expected
    return filter

def get_min(collection, count, filter):
    res = sorted(
                  [(i, x) for (i, x) in enumerate(collection) if filter(x)],
                  key=lambda pair: pair[1]
                 )[:count]
    return res if len(res) == count else None

def min_with_none(*collection):
    collection = [x for x in collection if x != None]
    return min(collection) if len(collection) != 0 else None

test = "4\n4 1 3 5 6\n2 3 6\n2 5 8\n2 7 12" # ответ 38, верно
with open('./27-A.txt') as f:
    _, *data = [[int(x) for x in y.split()[1:]] for y in f.read().strip().split('\n')]

for i, row in enumerate(data):
    if sum(row) % 2 != 0:
        j, substracted = get_min(row, 1, parity(1))[0]
        data[i] = (row[:j] + row[j+1:], substracted)
    else:
        data[i] = (row, None)

INDEX, VALUE = 0, 1 # индексы значения и индекса в паре

big_sum = sum(map((lambda pair: sum(pair[0])), data))

for i, row in enumerate(data):
    row, sub = row
    v1 = get_min(row, 1, lambda x: parity(0) and x % 5 != 0) # минимальное чётное
    if v1 != None:
        v1 = v1[0][VALUE]
        if sum(row) - v1 == 0: # проверка, что мы не пытаемся вычесть последнее число
            v1 = None
    
    if sub == None: # нет отброса
        v2 = get_min(row, 2, lambda x: parity(1) and x % 5 != 0) # можно ли вычесть два нечётных числа
        if v2 != None:
            v2 = sum(map((lambda pair: pair[VALUE]), v2)) 
            if sum(row) - v2 == 0:
                v2 = None
    else: # есть отброс
        v2 = get_min(row, 1, parity(1)) # можно ли поменять на другое число
        if v2 != None:
            if (v2[0][VALUE] - sub) % 5 != 0:
                v2 = v2[0][VALUE] - sub
            else:
                v2 = None

    data[i] = min_with_none(v1, v2)

min_delta = min([delta for delta in data if delta != None and delta % 5 != 0])

print(big_sum - min_delta)