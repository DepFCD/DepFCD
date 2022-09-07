#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Objective: used to resolve the update type of
every conflict single line.
'''
import difflib
import os
import csv
import json

import shutil

from collections import defaultdict


def java_name_extract(java_path):
    slash_pos = java_path.rfind('/')
    return java_path[slash_pos + 1:]


def conflict_first_line(java_path):
    resolve_out = './confresolve'
    with open(java_path) as f:
        lines = [line for line in f.readlines()]
    idx = 0
    conflict_lines = []
    conflict_lines = []
    conflict_line_str = ''
    actual_line = 0
    java_str = ''
    while idx < len(lines):
        # if lines[idx].strip() == '<<<<<<< HEAD':
        if lines[idx].strip() == '<<<<<<<':
            print('idx:', idx)
            conflict_lines.append(actual_line + 1)
            conflict_line_str += (str(actual_line + 1) + '#')
            idx += 1
            while idx < len(lines):
                if lines[idx].strip() == '=======':
                    idx += 1
                    break
                else:
                    java_str += lines[idx]
                    actual_line += 1
                    idx += 1
            while idx < len(lines):
                # if lines[idx].strip() == '>>>>>>> lineage/master':
                if lines[idx].strip() == '>>>>>>>':
                    idx += 1
                    break
                else:
                    idx += 1
        else:
            java_str += lines[idx]
            idx += 1
            actual_line += 1
    java_out = os.path.join(resolve_out, java_name_extract(java_path))
    with open(java_out, 'w') as f:
        f.write(java_str)

    return conflict_line_str[:-1]


import difflib
import re


def diff(file1, file2, encoding='utf-8'):
    """
    Simulates the output of GNU diff.
    You can use `diff(f1, f2)` to simulate `diff -w f1 f2`
    """
    texts = []
    for f in [file1, file2]:
        with open(f, 'r', encoding=encoding) as f:
            text = f.read()
        # Ignore whitespace characters
        for i in '\t\r\v\f':
            text = text.replace(i, '')
        texts += [text.split('\n')]
    text1, text2 = texts

    output = []
    new_part = True
    num = 0
    for line in difflib.unified_diff(text1, text2, fromfile=file1, tofile=file2, n=0, lineterm=''):
        num += 1
        if num < 3:
            continue
        flag = line[0]
        if flag == '-':  # line unique to sequence 1
            new_flag = '< '
        elif flag == '+':  # line unique to sequence 2
            new_flag = '> '
            if new_part:
                new_part = False
                output += ['---']
        elif flag == ' ':  # line common to both sequences
            # new_flag   = b'  '
            continue
        elif flag == '?':  # line not present in either input sequence
            new_flag = '? '
        elif flag == '@':
            output += [re.sub(r'@@ -([^ ]+) \+([^ ]+) @@', r'\1c\2', line)]
            new_part = True
            continue
        else:
            new_flag = flag
        output += [new_flag + line[1:]]

    return '\n'.join(output)


def diff_union_lines(conf):
    merge_from_path = './platforms/frameworks_base'
    custom_path = './platforms/resurrectionRemix/base'
    confs = dict()
    if conf.endswith('.java'):
        merge_from_java = os.path.join(merge_from_path, conf)
        custom_java = os.path.join(custom_path, conf)
        diff_res = os.popen('diff -U 0 ' + custom_java + ' ' + merge_from_java).read()
        # diff_res = diff(custom_java, merge_from_java)
        # diff_res = '\n'.join(difflib.unified_diff(open(custom_java, "r").readlines(), open(merge_from_java, "r").readlines(), lineterm=''))
        # print(diff_res)
        diff_lines = diff_res.split('\n')
        for idx, line in enumerate(diff_lines):
            if line.startswith('@@'):
                # @@ -1401,4 +3319,45 @@
                splits = line.split(' ')
                start = splits[1].split(',')[0].strip()[1:]
                inner_idx = idx + 1
                cnt = 0
                dash_exists = False
                dash_empty = False
                plus_exists = False
                annotation_exists = False
                while inner_idx < len(diff_lines):
                    if diff_lines[inner_idx].startswith('@@'):
                        break
                    elif diff_lines[inner_idx].startswith('-'):
                        dash_exists = True
                        if not diff_lines[inner_idx][1:].strip():
                            if not dash_empty:
                                cnt += 1
                        else:
                            if (not annotation_exists) and diff_lines[inner_idx][1:].strip().startswith('@'):
                                cnt += 1
                                dash_empty = True
                            else:
                                annotation_exists = True
                    elif diff_lines[inner_idx].startswith('+'):
                        plus_exists = True
                    inner_idx += 1
                if dash_exists and plus_exists:
                    start_int = int(start) + cnt
                    lasts = start_int
                    if ',' in splits[1]:
                        lasts = int(splits[1].split(',')[1].strip())
                    confs[str(start_int)] = lasts
    return confs


def conflicts_type_diff_resolve(conflicts):
    custom_path = './platforms/resurrectionRemix/base'
    resolve_dict = defaultdict(int)
    for conf in conflicts:
        if conf.endswith('.java') or conf.endswith('.aidl'):
            conf_line_dict = diff_union_lines(conf)
            custom_java_path = os.path.join(custom_path, conf)
            conflines = ''
            for line in conf_line_dict.keys():
                conflines += (line + '#')
            java_jar = './libs/mergeconftype.jar'
            print(custom_java_path)
            resolve_res = os.popen('java -jar ' + java_jar + ' ' + custom_java_path + ' ' + conflines[:-1]).read()
            resolve_lines = resolve_res.split('\n')
            for line in resolve_lines[1:]:
                if '#' in line:
                    splits = line.split('#')
                    resolve_dict[splits[0]] += int(splits[1])
    return resolve_dict


def conflicts_type_resolve():
    conflict_base = './conflicts'
    resolve_out = './confresolve'
    resolve_dict = defaultdict(int)
    conflict_files = os.listdir(conflict_base)
    conflict_types = ''
    for conf in conflict_files:
        if conf.endswith('.java') or conf.endswith('.aidl'):
            conf_path = os.path.join(conflict_base, conf)
            conflines = conflict_first_line(conf_path)
            conf_resolve_path = os.path.join(resolve_out, conf)
            java_jar = './libs/classparser.jar'
            print(conf_resolve_path)
            resolveRes = os.popen('java -jar ' + java_jar + ' ' + conf_resolve_path + ' ' + conflines).read()
            resolve_lines = resolveRes.split('\n')
            for line in resolve_lines[1:]:
                if '#' in line:
                    splits = line.split('#')
                    resolve_dict[splits[0]] += int(splits[1])
    return resolve_dict


def custom_reset(custom_commit, custom_branch):
    '''Reset to the specific commit status'''
    custom_path = './platforms/resurrectionRemix/base'
    cwd = os.getcwd()
    os.chdir(custom_path)
    branch_checkout = os.popen('git checkout -f ' + custom_branch).read()
    reset_res = os.popen('git reset --hard ' + custom_commit).read()
    # os.popen('git pull').read()
    os.chdir(cwd)


def merge_from_reset(merge_from_commit, merge_from_branch):
    '''Reset to the specific commit status'''
    merge_from_path = './platforms/frameworks_base'
    cwd = os.getcwd()
    os.chdir(merge_from_path)
    branch_checkout = os.popen('git checkout -f ' + merge_from_branch).read()
    reset_res = os.popen('git reset --hard ' + merge_from_commit).read()
    # os.popen('git pull').read()
    os.chdir(cwd)


def custom_merge_diff(custom_commit, custom_branch, merge_from_commit, merge_from_branch):
    '''Merge android platform and check if there are some conflicts'''
    custom_reset(custom_commit, custom_branch)
    merge_from_reset(merge_from_commit, merge_from_branch)
    custom_path = './platforms/resurrectionRemix/base'
    conflicts_out = './conflicts'
    has_conflict = False
    cwd = os.getcwd()
    os.chdir(custom_path)
    upd_res = os.popen('git remote update').read()
    merge_res = os.popen('git merge android/' + merge_from_branch).read()
    conflicts = set()
    conf_javas = 0
    merges = merge_res.split('\n')
    for line in merges:
        if line.startswith('CONFLICT (content): Merge conflict in'):
            has_conflict = True
            splits = line.split(' ')
            conflicts.add(splits[-1])
            if splits[-1].endswith('.java'):
                conf_javas += 1
    print(conflicts)
    if has_conflict:
        os.popen('git merge --abort').read()
    os.chdir(cwd)

    return has_conflict, len(conflicts), conflicts, conf_javas


def last_commit_remove():
    resolve_out = './confresolve'
    conflict_base = './conflicts'
    resolves = os.listdir(resolve_out)
    conflicts = os.listdir(conflict_base)
    for f in resolves:
        f_path = os.path.join(resolve_out, f)
        os.remove(f_path)
    for f in conflicts:
        f_path = os.path.join(conflict_base, f)
        os.remove(f_path)


def custom_merge():
    merge_commit_base = './history/android_base/csvs/resurrectionRemix'
    csvs = os.listdir(merge_commit_base)
    conflict_info = []
    for idx, merge_file in enumerate(csvs):
        if merge_file.endswith('.csv') and '.android.' not in merge_file:
            merge_csv = os.path.join(merge_commit_base, merge_file)
            merge_out = os.path.join('./history/android_base/mergetypes/resurrectionRemix/', merge_file[:-4] + '-merge.csv')
            print(idx, len(csvs), merge_csv)
            total_merge, conflict_merge = custom_merge_impl(merge_csv, merge_out)
            conflict_info.append([merge_file[:-4], total_merge, conflict_merge])
    conflict_info_out = os.path.join('./history/android_base/mergetypes/resurrectionRemix/', 'conflict_info.csv')
    with open(conflict_info_out, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['branch', 'total', 'conflict'])
        writer.writerows(conflict_info)


def custom_merge_impl(merge_csv, out_csv):
    total_merge = 0
    conflict_merge = 0
    outs = []
    with open(merge_csv) as f:
        reader = csv.reader(f)
        for row in reader:
            last_commit_remove()
            total_merge += 1
            custom_commit = row[1]
            merge_from_commit = row[2]
            custom_brch = row[4]
            merge_from_brch = row[5]
            has_conflict, conf_len, conflicts, conf_java = custom_merge_diff(custom_commit, custom_brch, merge_from_commit, merge_from_brch)
            if has_conflict:
                conflict_merge += 1
                resolve_dict = conflicts_type_diff_resolve(conflicts)
                d_str = ''
                for merge_type, type_cnt in resolve_dict.items():
                    d_str += (merge_type + ':' + str(type_cnt) + ',')
                outs.append([row[0], conf_len, conf_java, d_str[:-1]])
    if outs:
        with open(out_csv, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['Merge', 'Conflicts', 'Javas', 'Merge_Type'])
            writer.writerows(outs)
    return total_merge, conflict_merge


if __name__ == '__main__':
    custom_merge()
