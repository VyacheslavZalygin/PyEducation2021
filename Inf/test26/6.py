import sys

inpt = sys.stdin.read().split()
pairs = [(int(inpt[i]), int(inpt[i + 1]))
         for i in range(0, len(inpt), 2)]

start = 1634515200
end = start + 7 * 24 * 60 * 60

week = [0 for _ in range(7 * 24 * 60 * 60 + 1)]
for st, en in pairs:
  if st < start:
    week[0] += 1
  elif st < end:
    week[st - start + 1] += 1

  if en < start and en != 0:
    week[0] -= 1
  elif en < end and en != 0:
    week[en - start + 1] -= 1

current = 0
current_sec = 0
m = 0
m_sec = 0
for s in week:
  if s != 0:
    if m <= current:
      m = current
      m_sec = current_sec
    current_sec = 0
  current_sec += 1
  current += s
if m <= current:
  m = current
  m_sec = current_sec
print(m, m_sec)