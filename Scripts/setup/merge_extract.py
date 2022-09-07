#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Objective: used to extract all merge commits from
different branches of downstream projects
'''

import os
import csv

def commit_hist_retrieve(commit_log_path):
    with open(commit_log_path, errors = 'ignore') as f:
        lines = [line for line in f.readlines()]
    idx = 0
    commits = set()
    while idx < len(lines):
        if lines[idx].startswith('commit '):
            splits = lines[idx].split(' ')
            commit_id = splits[-1].strip()
            commits.add(commit_id[:11])
        idx += 1
    return commits

def merge_from_platform_commit_hist(branch_dir):
#    branch_dir = '/Users/pliu0032/AndroidVersion/history/android_base'
    print('android platform commits:', branch_dir)
    branches = os.listdir(branch_dir)
    platform_commits = {}
    for branch in branches:
        branch_path = os.path.join(branch_dir, branch)
        branch_name = branch[:-4]
        commits = commit_hist_retrieve(branch_path)
        platform_commits[branch_name] = commits
    return platform_commits

def platform_commit_hist(branch_dir):
#    branch_dir = '/Users/pliu0032/AndroidVersion/history/lineage/branches'
    print('platform commits:', branch_dir)
    branches = os.listdir(branch_dir)
    platform_commits = {}
    for branch in branches:
        branch_path = os.path.join(branch_dir, branch)
        branch_name = branch[:-4]
        commits = commit_hist_retrieve(branch_path)
        platform_commits[branch_name] = commits
    return platform_commits

def merge_commit_extract(commit_path):
    with open(commit_path, errors = 'ignore') as f:
        lines = [line for line in f.readlines()]
    idx = 0
    outs = ''
    merge_commits = []
    commits = set()
    while idx < len(lines):
        if lines[idx].startswith('commit '):
            commit_splits = lines[idx].split(' ')
            commits.add(commit_splits[-1].strip()[:11])
            idx += 1
            if lines[idx].startswith('Merge: '):
                merge_splits = lines[idx].split(' ')
                outs += lines[idx]
                curr_merge = [commit_splits[-1].strip(), merge_splits[-2].strip()[:11], merge_splits[-1].strip()[:11]]
                is_google_mail = False
                idx += 1
                if lines[idx].startswith('Author: '):
                    splits = lines[idx].split(' ')
                    if splits[-1].strip().startswith('<') and splits[-1].strip().endswith('>'):
                        email_address = splits[-1].strip()[1:-1]
                        if email_address and (email_address.endswith('@google.com') or email_address.endswith('@android.com') or email_address.endswith('@googlemail.com')):
                            is_google_mail = True
                if is_google_mail:
                    curr_merge.append('Google')
                else:
                    curr_merge.append('None')
                if curr_merge:
                    merge_commits.append(curr_merge)
        else:
            idx += 1
    return commits, merge_commits

def commit_branch_retrieve(platform_commits, commit_id):
    for branch, commits in platform_commits.items():
        if commit_id in commits:
            return branch
    return ''

def merge_extract(platform_commits, commit_path, merge_from_platform_commits):
    commits, merge_commits = merge_commit_extract(commit_path)
    valid_merge_outs = []
    invalid_merge_outs = []
    for merge_commit in merge_commits:
        custom_commit_branch = commit_branch_retrieve(platform_commits, merge_commit[1])
        android_commit_branch = commit_branch_retrieve(merge_from_platform_commits, merge_commit[2])
        custom_from_android = commit_branch_retrieve(merge_from_platform_commits, merge_commit[1])
        android_from_custom = commit_branch_retrieve(platform_commits, merge_commit[2])
#        if not custom_commit_branch and android_commit_branch and not custom_from_android and not a_commit_branch:
#        if merge_commit[0] == '70ccfc70e9eb223cda9c20350061522a946601c8':
#            print(merge_commit)
#            print(custom_commit_branch, android_commit_branch, merge_commit, custom_from_android) #, android_from_custom)
        if custom_commit_branch and android_commit_branch and not custom_from_android: # and not android_from_custom:
            if android_from_custom:
                print(custom_commit_branch, android_commit_branch, merge_commit)
            curr = merge_commit
            curr.append(custom_commit_branch)
            curr.append(android_commit_branch)
            valid_merge_outs.append(curr)
        else:
#            print('Not Appropriate', custom_commit_branch, android_commit_branch, merge_commit)
            curr = merge_commit
            curr.append(custom_commit_branch)
            curr.append(android_commit_branch)
            invalid_merge_outs.append(curr)
    return valid_merge_outs, invalid_merge_outs


if __name__ == '__main__':
    merge_from_dir = './CustomizedAndroid/history/android/branches'
    custom_dir = './CustomizedAndroid/history/resurrectionRemix/branches'
    base_out = './CustomizedAndroid/history/android_base/csvs/resurrectionRemix'
    merge_from_platform_commits = merge_from_platform_commit_hist(merge_from_dir)
    platform_commits = platform_commit_hist(custom_dir)
    txts = os.listdir(custom_dir)
    for txt_name in txts:
        if txt_name.endswith('.csv'):
            continue
        txt_path = os.path.join(custom_dir, txt_name)
#        if txt_path != '/Users/pliu0032/AndroidVersion/history/lineage/branches/lineage-16.0.txt':
#            continue
        print(txt_path)
        valid_merge_commit_outs, invalid_merge_commit_outs = merge_extract(platform_commits, txt_path, merge_from_platform_commits)
        valid_merge_out = os.path.join(base_out, txt_name[:-4] + '.csv')
        if valid_merge_commit_outs:
            print(valid_merge_out)
            with open(valid_merge_out, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(valid_merge_commit_outs)
        invalid_merge_out = os.path.join(base_out, txt_name[:-4] + '.android.csv')
        if invalid_merge_commit_outs:
            print(invalid_merge_out)
            with open(invalid_merge_out, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(invalid_merge_commit_outs)
