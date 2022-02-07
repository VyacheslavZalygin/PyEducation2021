with open('27-B.txt') as f:
  arr = [int(x) for x in f.read().split()[1:]]
  # arr = [2, 10, 3, 4, 4, 3, 6, 5, 11]

def is_spl(n):
  return n > 0 and n % 2 != 0

def step(m_sum, thread, n, k_thread):
  q, c_sum, k, k_max = thread
  new_thread = None

  q[-1] += n
  c_sum += n

  if is_spl(n):
    k += 1
    q.append(0)
    if k > k_max and k != 0:
      if k > k_thread:
        new_thread = (q[:], c_sum, k, k_max+30) # новый поток с потолком в 2 раза выше
        k_thread += 30
      m_sum = max(m_sum, c_sum-n) # перед n
      c_sum -= q.pop(0) # отнимаем прошлое
      m_sum = max(m_sum, c_sum) # с n
      k -= 1
  thread = q, c_sum, k, k_max
  return m_sum, thread, new_thread, k_thread

def fin(m_sum, thread, n):
  q, c_sum, k, k_max = thread

  q[-1] += n
  c_sum += n

  if k == k_max:
    m_sum = max(m_sum, c_sum)  # с n
  thread = q, c_sum, k, k_max
  return m_sum, thread

def main():
  m_sum = 0
  threads = [([0], 0, 0, 30)]
  k_thread = 30
  for j, n in enumerate(arr):
    if j % 10000 == 0: print(j)
    new_threads = []
    for i, thread in enumerate(threads):
      m_sum, threads[i], new_thread, k_thread = step(m_sum, thread, n, k_thread)
      if not new_thread is None:
        new_threads.append(new_thread)
    threads.extend(new_threads)
  for i, thread in enumerate(threads):
    m_sum, threads[i]= fin(m_sum, thread, 0)
  print(m_sum)

main()