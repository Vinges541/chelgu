#!/usr/bin/python3
import os
import argparse
from typing import List
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('forks', type=int, help='number of forks')
parser.add_argument('iterations', type=int, help='number of iterations')
parser.add_argument('message', type=str, help='message')

args = parser.parse_args()

child_pids: List[int] = []
init = os.getppid()

for i in range(1, args.forks + 1):
    pid = os.fork()
    if (pid != 0):
        child_pids.append(pid)
    else:
        for j in range(args.iterations * i):
            if(os.getppid() == init):
                exit(1)
            print(f'fork = {i}\titeration = {j}\tmessage = {args.message}')
            sleep(1)
        exit(0)
        
for pid in child_pids:
    os.waitpid(pid, 0)
