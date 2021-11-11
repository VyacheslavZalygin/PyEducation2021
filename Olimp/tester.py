import subprocess
import sys
import os

def run_test(tested_program_path, test_in_path, test_out_path):
    with open(test_in_path, 'r') as f:
        test_in_data = f.read().replace('\n', ' ')
    result = subprocess.run([f'python', f'{tested_program_path}'], input=test_in_data.encode('utf-8'), stdout=subprocess.PIPE).stdout\
        .decode("utf-8").split()
    with open(test_out_path) as f:
        test_out_data = f.read().split()
    return test_out_data == result, test_out_data, result, test_in_data

def run_test_set(tested_program_path, test_setPath):
    for cur, dirs, files in os.walk(test_setPath):
        files = [x for x in files if not '.a' in x]
        i = 0
        passed = 0
        for test in files:
            i += 1
            res, exp, act, inp = run_test(tested_program_path, test_setPath+'/'+test, test_setPath+'/'+test+'.a')
            if res:
                print(i, 'ok')
                passed += 1
            else:
                print(i, 'wrong answer', f'inp: {inp} exp: {exp} act: {act}')
        print(f'passed {passed} of {i}')

def check_answer_2(exp, act):
  if exp[0] != act[0]:
    return False
  exp, act = exp[1:], act[1:]
  exp = [[exp[i * 3 + 0], exp[i * 3 + 1], exp[i * 3 + 2]] for i in range(len(exp) // 3)]
  act = [[act[i * 3 + 0], act[i * 3 + 1], act[i * 3 + 2]] for i in range(len(act) // 3)]
  for z in exp:
    c = False
    for x in act:
      if z == x:
        c = True
    if not c:
      return False
  return True

def main():
    prog = './municip2021/problem3.py'
    test_set = './municip2021/3/tests'
    run_test_set(prog, test_set)

main()