def neighbors(state):
    count, prev, prevprev = state

    result = []
    if count >= 21: return result
    if prevprev != '+1': result.append((count+1, '+1', prev))
    if prevprev != '+2': result.append((count+1, '+2', prev))
    if prevprev != '*2': result.append((count+1, '*2', prev))

    return result

table = {}
def binmark(state):
    if state in table: return table[state]

    min_steps = None
    max_steps = None
    for steps_to_win, mark in [
        binmark(next_state) 
        for next_state in neighbors(state)
    ]:
        if not mark and (min_steps == None or steps_to_win < min_steps):
            min_steps = steps_to_win
        if mark and (max_steps == None or steps_to_win > max_steps):
            max_steps = steps_to_win

    if min_steps == None and max_steps == None: 
        answer = (0, False) 
    if min_steps != None:
        answer = (min_steps+1, True)
    else:
        answer = (max_steps, False)

    table[state] = answer
    return answer

for count in range(1, 21):
    print(count, '==>', binmark((count, None, None)))