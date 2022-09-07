#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Objective: used to resolve the update type of
every conflict single line.
'''

import os
import csv
import json

import shutil

from collections import defaultdict
import difflib

# platform_frameworks_base
merge_from_platform_name = 'frameworks_base'
merge_from_name = 'android'
out_base_name = 'android_base'
custom_name = 'resurrectionRemix'
merge_from_path = '/data1/ENRE/dyt/DataExtraction/CustomizedAndroid/platforms/' + merge_from_platform_name
custom_path = '/data1/ENRE/dyt/DataExtraction/CustomizedAndroid/platforms/resurrectionRemix/base'
conf_dir = '/data1/ENRE/dyt/DataExtraction/CustomizedAndroid/history/astconffiles'

visited_commits = set()

def java_name_extract(java_path):
    slash_pos = java_path.rfind('/')
    return java_path[slash_pos + 1:]

def conf_line_retrieve(conf):
    confs = []
    if conf.endswith('.java'):
        rslash_pos = conf.rfind('/')
        java_name = conf[rslash_pos + 1:]
        conf_path = os.path.join(conf_dir, java_name)
        print(conf_path)
        with open(conf_path) as f:
            lines = [line.strip() for line in f.readlines()]
        idx = 0
        length = len(lines)
        while idx < length:
            curr_rm = []
            curr_add = []
            if lines[idx].startswith('<<<<<<<'):
                print(idx, conf, lines[idx])
                idx += 1
                while not lines[idx].startswith('======='):
                    curr_rm.append(lines[idx])
                    idx += 1
                idx += 1
                while not lines[idx].startswith('>>>>>>>'):
                    curr_add.append(lines[idx])
                    idx += 1
                idx += 1
                confs.append([curr_rm, curr_add])
            else:
                idx += 1
        return origin_file_lines(confs, conf)
    return confs

def origin_file_lines(confs, conf_name):
    line_outs = []
    conf_merge_from_path = os.path.join(merge_from_path, conf_name)
    conf_custom_path = os.path.join(custom_path, conf_name)
    if not os.path.exists(conf_merge_from_path) or not os.path.exists(conf_custom_path):
        return line_outs
    with open(conf_merge_from_path) as f:
        merge_from_lines = [line.strip() for line in f.readlines()]
    with open(conf_custom_path) as f:
        custom_lines = [line.strip() for line in f.readlines()]
    for conf in confs:
        curr = []
        conf_rm = conf[0]
        conf_add = conf[1]
        if conf_rm:
            cstart, cend, clength = origin_file_lines_impl(conf_rm, custom_lines)
            curr.append([cstart, cend, clength])
        else:
            curr.append([0, 0, 0])
        if conf_add:
            mstart, mend, mlength = origin_file_lines_impl(conf_add, merge_from_lines)
            curr.append([mstart, mend, mlength])
        else:
            curr.append([0, 0, 0])
        line_outs.append(curr)
    return line_outs

def origin_file_lines_impl(lines, merge_lines):
    idx = 0
    jdx = 0
    start = 0
    end = 0
    merge_len = len(merge_lines)
    while idx < merge_len:
        if merge_lines[idx] == lines[jdx]:
            start = idx + 1
            inner_idx = idx
            inner_jdx = jdx
            while inner_idx < merge_len and inner_jdx < len(lines):
                if merge_lines[inner_idx] == lines[inner_jdx]:
                    inner_idx += 1
                    inner_jdx += 1
                else:
                    break
            if inner_jdx < len(lines):
                start = 0
                idx += 1
                jdx = 0
            else:
                end = inner_idx
        else:
            idx += 1
        if start != 0:
            break
    return start, end, len(lines)

def diff_union_lines(conf):
    confs = dict()
    if conf.endswith('.java'):
        merge_from_java = os.path.join(merge_from_path, conf)
        custom_java = os.path.join(custom_path, conf)
        diff_res = os.popen('diff -U 0 ' + custom_java + ' ' + merge_from_java).read()
        # diff_res = '\n'.join(difflib.unified_diff(open(custom_java, "r").readlines(), open(merge_from_java, "r").readlines(), lineterm=''))
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

def ast_node_cnt(lineNum, ast_nodes):
    node_cnt = 0
    methods = set()
    for node in ast_nodes:
        if node.strip():
            if '#' in node:
                start = int(node.split('#')[0].strip())
                end = int(node.split('#')[1].strip())
                method = node.split('#')[2].strip()
                m_start = node.split('#')[3].strip()
                m_end = node.split('#')[4].strip()
                if start >= int(lineNum[0]) and end <= int(lineNum[1]):
                    node_cnt += 1
                    methods.add(method + '#' + m_start + '#' + m_end)
    return node_cnt, methods

def conflicts_type_diff_resolve(conflicts):
    java_jar = './libs/astmethodparser.jar'
    resolve_dict = defaultdict(int)
    outs = []
    for conf in conflicts:
        if conf.endswith('.java'):
            curr = [conf]
            conf_lines = conf_line_retrieve(conf)
            print(conf_lines)
            custom_java = os.path.join(custom_path, conf)
            merge_from_java = os.path.join(merge_from_path, conf)
            if not os.path.exists(custom_java) or not os.path.exists(merge_from_java):
                continue
            custom_nodes = os.popen('java -jar ' + java_jar + ' ' + custom_java).readlines()
            merge_from_nodes = os.popen('java -jar ' + java_jar + ' ' + merge_from_java).readlines()
            conf_custom_curr = []
            conf_merge_from_curr = []
            for conf_line in conf_lines:
                custom_node_cnt, custom_methods = ast_node_cnt(conf_line[0], custom_nodes)
                merge_from_cnt, merge_from_methods = ast_node_cnt(conf_line[1], merge_from_nodes)
                tmp_custom = conf_line[0]
                tmp_custom.append(custom_node_cnt)
                tmp_custom.append(list(custom_methods))
                tmp_merge_from = conf_line[1]
                tmp_merge_from.append(merge_from_cnt)
                tmp_merge_from.append(list(merge_from_methods))
                conf_custom_curr.append(tmp_custom)
                conf_merge_from_curr.append(tmp_merge_from)
            curr.append(conf_custom_curr)
            curr.append(conf_merge_from_curr)
            outs.append(curr)
    return outs

def custom_reset(custom_commit, custom_branch):
    '''Reset to the specific commit status'''
    cwd = os.getcwd()
    os.chdir(custom_path)
    branch_checkout = os.popen('git checkout -f ' + custom_branch).read()
    reset_res = os.popen('git reset --hard ' + custom_commit).read()
    os.chdir(cwd)

def merge_from_reset(merge_from_commit, merge_from_branch):
    '''Reset to the specific commit status'''
    cwd = os.getcwd()
    os.chdir(merge_from_path)
    branch_checkout = os.popen('git checkout -f ' + merge_from_branch).read()
    reset_res = os.popen('git reset --hard ' + merge_from_commit).read()
    os.chdir(cwd)

def conf_dir_empty():
    fs = os.listdir(conf_dir)
    for f in fs:
        f_path = os.path.join(conf_dir, f)
        os.remove(f_path)

def custom_merge_diff(custom_commit, custom_branch, merge_from_commit, merge_from_branch):
    '''Merge android platform and check if there are some conflicts'''
    custom_reset(custom_commit, custom_branch)
    merge_from_reset(merge_from_commit, merge_from_branch)
#    custom_path = '/Users/pliu0032/AndroidVersion/platforms/cyanogenmod'
    has_conflict = False
    cwd = os.getcwd()
    conf_dir_empty()
    os.chdir(custom_path)
    upd_res = os.popen('git remote update').read()
    merge_res = os.popen('git merge ' + merge_from_name + '/' + merge_from_branch).read()
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
            conf_path = os.path.join(custom_path, splits[-1])
            shutil.copy2(conf_path, conf_dir)
    print(conflicts)
    if has_conflict:
        os.popen('git merge --abort').read()
    os.chdir(cwd)

    return has_conflict, len(conflicts), conflicts, conf_javas

def custom_merge():
    merge_commit_base = './history/' + out_base_name + '/csvs/' + custom_name
    csvs = os.listdir(merge_commit_base)
    conflict_info = []
    for idx, merge_file in enumerate(csvs):
        if merge_file.endswith('.csv') and '.android.' not in merge_file:
            merge_csv = os.path.join(merge_commit_base, merge_file)
            merge_out = os.path.join('./history/' + out_base_name + '/ast/' + custom_name, merge_file[:-4] + '-merge.csv')
            print(idx, len(csvs), merge_csv)
            total_merge, conflict_merge = custom_merge_impl(merge_csv, merge_out)
            conflict_info.append([merge_file[:-4], total_merge, conflict_merge])
    conflict_info_out = os.path.join('./history/' + out_base_name + '/ast/' + custom_name, 'conflict_info.csv')
    with open(conflict_info_out, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['branch', 'total', 'conflict'])
        writer.writerows(conflict_info)

def custom_merge_impl(merge_csv, out_csv):
    global visited_commits
    total_merge = 0
    conflict_merge = 0
    outs = []
    with open(merge_csv) as f:
        reader = csv.reader(f)
        for row in reader:
            if not visited_commits or row[0] not in visited_commits:
                visited_commits.add(row[0])
            else:
                continue
            total_merge += 1
            custom_commit = row[1]
            merge_from_commit = row[2]
            custom_brch = row[4]
            merge_from_brch = row[5]
            has_conflict, conf_len, conflicts, conf_java = custom_merge_diff(custom_commit, custom_brch, merge_from_commit, merge_from_brch)
            if has_conflict:
                conflict_merge += 1
                resolve_outs = conflicts_type_diff_resolve(conflicts)
                outs.append([row[0], conf_len, conf_java, resolve_outs])
    if outs:
        with open(out_csv, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['Merge', 'Conflicts', 'Javas', 'AST'])
            writer.writerows(outs)
    print(total_merge, conflict_merge)
    return total_merge, conflict_merge

if __name__ == '__main__':
    custom_merge()
