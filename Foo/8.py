def perms(xs):
    if len(xs) == 0: return [[]]
    return [
    [ xs[i] ] + tail
        for i in range(len(xs))
        for tail in perms(xs[:i] + xs[i+1:])
    ]

def is_good(word):
    for i in range(len(word)-1):
        if word[i] in 'OA' and word[i+1] in 'OA': return False
        if word[i] in 'RSMH' and word[i+1] in 'RSMH': return False
    return True

xs = 'ROSOMAHA'
print(sum([1 for x in set(*perms('abc')) if is_good(x)]))
