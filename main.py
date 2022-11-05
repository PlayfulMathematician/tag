"""
The goal of this code is interpret .fl files

An .fl file is a file that contains a list of folders and files in a
directory.
If a file is within a folder it will be indented by 4 spaces.
"""

import os
import sys
import re


def remove_tabs(file_list) -> list:
    """Removes the tabs from the file_list
    :type file_list: list[str]
    :usage:
    """
    new_list = []

    for line in file_list:
        tabs_len = line.count('\t')
        new_list.append((line.replace('\t', ''), tabs_len))
    return new_list


def get_fl_contents(file_name) -> list:
    """Returns the directories and file of a .fl file
    :usage:

    """
    file_list = []
    with open(file_name, 'r') as f:
        for line in f:

            file_list.append(line.replace('\n', ''))

    return process_tabs_file_list_pairs(remove_tabs(file_list))


def process_tabs_file_list_pairs(file_list) -> list:
    """Processes the file_list and returns a list of tuples
    :type file_list: list[tuple[str, int]]
    :usage:
    >>> process_tabs_file_list_pairs([('hello', 0), ('world', 1), ('!', 0)])
    [['hello', ['world', None]], ['!', None]]
    """
    new_list = []
    for i, line in enumerate(file_list):
        if line[1] == 0:
            if i == len(file_list) - 1:
                new_list.append([line[0], None])
                continue

            if file_list[i + 1][1] == 1:
                start = i + 1
                end = list(map(lambda x: x[1], file_list[i + 2:])).index(0) + i + 1
                recur_list = file_list[start:end+1]
                recur_list = list(map(lambda x: (x[0], x[1] - 1), recur_list))
                new_list.append([line[0]] + process_tabs_file_list_pairs(recur_list))
            else:
                new_list.append([line[0], None])

    return new_list


def _revert_processing(file_list) -> list:
    """Reverts the processing done to the file_list
    :type file_list: list
    """
    new_list = []
    for line in file_list:
        if line[1] is None:
            new_list.append(line[0])
        else:
            new_list.append(line[0])
            new_list += list(map(lambda x: '\t' + x, (_revert_processing(line[1:]))))

    return new_list


def revert_processing(file_list):
    """Reverts the processing done to the file_list
    :type file_list: list
    """
    new_list = _revert_processing(file_list)
    str_list = ""
    for line in new_list:
        str_list += line + '\n'

    return str_list




