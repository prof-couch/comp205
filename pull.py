#!/usr/bin/env python

# This simple pattern does what nbgitpuller does on
# https://jupyterhub.cs.tufts.edu for someone who is
# running their own server instead.

# you must run
#     pip install nbgitpuller
# for this to work

# For details, browse to
#     https://github.com/jupyterhub/nbgitpuller/blob/master/docs/index.md

# enter your repository location as a path on your hard disk.
# an absolute path is recommended. The example path is in Windows.
import os, sys, argparse
from nbgitpuller import GitPuller

def main(repo, dest):
    print (repo, dest)
    question = 'confirm pulling\n    from ' + repo + '\n    into ' + dest
    reply = str(input(question + '\n (y/n): ')).lower().strip()
    if reply[:1] == 'y':
        gp = GitPuller(repo, "master", dest)

        try:
            for line in gp.pull():
                print(line)  # print log output from actions taken
        except Exception as e:
            print(e)

if __name__ == "__main__":
    parser=argparse.ArgumentParser()

    parser.add_argument('--repo', help='The github repository to pull from, uses comp205-dist if not specified')
    parser.add_argument('--dest', help='The destination directory, uses current directory if not specified')

    args=parser.parse_args()

    repo = args.repo if args.repo else "https://github.com/prof-couch/comp205-dist"
    dest = args.dest if args.dest else os.getcwd()
    main(repo, dest)
