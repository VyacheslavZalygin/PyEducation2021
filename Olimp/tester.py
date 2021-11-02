import subprocess
import sys
import os

def run_test(tested_program_path, test_in_path, test_out_path):
    with open(test_in_path, 'r') as f:
        test_in_data = f.read().replace('\n', ' ')
    result = subprocess.run([f'python', f'{tested_program_path}'], input=test_in_data.encode('utf-8'), stdout=subprocess.PIPE).stdout\
        .decode("utf-8").replace('\n', ' ')
    result = result.replace('\r', '')
    with open(test_out_path) as f:
        test_out_data = f.read()
    test_out_data = test_out_data.replace('\n', ' ')
    return result == test_out_data, test_out_data, result

def run_test_set(tested_program_path, test_setPath):
    for cur, dirs, files in os.walk(test_setPath):
        files = [x for x in files if not '.a' in x]
        for test in files:
            res, exp, act = run_test(tested_program_path, test_setPath+'/'+test, test_setPath+'/'+test+'.a')
            if res:
                print(test, 'ok')
            else:
                print(test, 'wrong answer')
                print(f'exp: {exp}\nact: {act}')


def main():
    prog = './municip2021/problem1.py'
    test_set = './municip2021/1/tests'
    run_test_set(prog, test_set)

main()