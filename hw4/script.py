#!/usr/bin/python3
import os
import argparse
from typing import List
from time import sleep
from pathlib import PosixPath

parser = argparse.ArgumentParser()
parser.add_argument('forks', type=int, help='number of forks')
parser.add_argument('iterations', type=int, help='number of iterations')
parser.add_argument('message', type=str, help='message')

args = parser.parse_args()

child_pids: List[int] = []

with open('log.txt', mode='w') as log:

    for i in range(1, args.forks + 1):
        pid = os.fork()
        if (pid != 0):
            child_pids.append(pid)
            child, _ = os.waitpid(0, os.WNOHANG)
            if child != 0:
                print(f'child with pid={child} exited with code={code}. parent with pid id={os.getpid()} exited')
                exit(2)
        else:
            parent_pid = os.getppid()
            parent_path = PosixPath(f'/proc/{parent_pid}')
            for j in range(args.iterations * i):
                if not parent_path.exists():
                    print(f'parent with pid={parent_pid} exited. child with pid={os.getpid()} exited')
                    exit(1)
                print(f'fork = {i}\titeration = {j}\tmessage = {args.message}', file=log)
                sleep(1)
            exit(0)

while True:
    child, code = os.waitpid(0, os.WNOHANG)
    if child != 0:
        print(f'child with pid={child} exited with code={code}. parent with pid id={os.getpid()} exited')
        exit(2)