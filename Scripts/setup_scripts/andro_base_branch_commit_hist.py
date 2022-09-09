#/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Objective: used to extract commit history of every single branch
of selected system platform
'''

import os
import csv
import json

import subprocess

def branch_delete():
    base_dir = '/Users/pliu0032/AndroidVersion/platforms/platform_frameworks_base'
    branch_all = '/Users/pliu0032/AndroidVersion/history/scripts/branch_all.txt'
    with open(branch_all) as f:
        lines = [line.strip() for line in f.readlines()]
    os.chdir(base_dir)
    for line in lines:
        splits = line.split('/')
        del_branch = os.popen('git branch -d ' + splits[1]).read()

def commit_history_extract():
    base_dir = '/data1/ENRE/dyt/DataExtraction/CustomizedAndroid/platforms/resurrectionRemix/android_frameworks_base'
    branch_all = '/data1/ENRE/dyt/DataExtraction/CustomizedAndroid/history/resurrectionRemix/branch_all.txt'
    out_dir = '/data1/ENRE/dyt/DataExtraction/CustomizedAndroid/history/resurrectionRemix/branches'
    with open(branch_all) as f:
        lines = [line.strip() for line in f.readlines()]
    pwd = os.getcwd()
    os.chdir(base_dir)
    for line in lines:
        # git checkout -b test origin/test
        splits = line.split('/')
        print("@@:", splits)
        del_branch = os.popen('git branch -d ' + splits[1].strip()).read()
        args = ['git', 'checkout', '-b', splits[1].strip(), line]
        branch_check = os.popen('git checkout -f -b ' + splits[1].strip() + ' ' + line).read()
        branches = os.popen('git branch').readlines()
        for branch in branches:
            if branch.startswith('*'):
                branch_name = branch.split(' ')
                if branch_name[-1].strip() != splits[1].strip():
                    print('## curr branch:', branch, splits)
                    break
        log_args = ['git', 'log']
        proc = subprocess.Popen(log_args, stdout = subprocess.PIPE, stderr = subprocess.PIPE, errors = 'ignore', encoding = 'utf-8')
        try:
            outs, errs = proc.communicate(timeout = 300)
            out_path = os.path.join(out_dir, splits[1] + '.txt')
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(outs)
        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
    os.chdir(pwd)

if __name__ == '__main__':
    commit_history_extract()
#    branch_delete()
