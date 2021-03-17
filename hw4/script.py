import os
from typing import List

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('forks', type=int, help='number of forks')
parser.add_argument('iterations', type=int, help='number of iterations')
parser.add_argument('message', type=str, help='message')

args = parser.parse_args()

child_pids: List[int] = []

for i in range(1, args.forks + 1):
    pid = os.fork()
    if (pid == 0):
        child_pids.append(pid)
    else:
        for j in range(args.iterations * i):
            print(f'fork = {i}\titeration = {j}\tmessage = {args.message}')
        exit(0)
        
for pid in child_pids:
    try:
        os.waitpid(pid, 0)
    except ChildProcessError:
        continue
