#!/usr/bin/python
import heapq
import os
import shutil

TOPK_FOLDER="top_k/"
INPUT_FILENAME="unsorted_file.txt"

def highest_k(input_file_path, output_file_path, k):
    with open(input_file_path) as input_file:
        with open(output_file_path, 'w+') as output_file:
            output_file.writelines('\n'.join(map(str, heapq.nlargest(k, map(int, input_file)))))

def input_file_select(input_file_path, k):
    input_file_name = input_file_path
    k_calculated = []
    for f in os.listdir("top_k"):
        k_calculated.append(int(os.path.splitext(f)[0]))
    k_calculated.sort()
    for k_cal in k_calculated:
        if k <= k_cal:
            input_file_name = TOPK_FOLDER + str(k_cal) + ".txt"
    return input_file_name

def file_has_changed(input_file_path):
    input_file = os.stat(input_file_path).st_mtime
    if os.listdir(TOPK_FOLDER):
        if input_file - os.stat(TOPK_FOLDER + os.listdir(TOPK_FOLDER)[0]).st_mtime > 0:
            shutil.rmtree(TOPK_FOLDER)
            os.mkdir(TOPK_FOLDER)


def calculate_k(k):
    if not os.path.isdir(TOPK_FOLDER):
        os.mkdir(TOPK_FOLDER)
    file_has_changed(INPUT_FILENAME)
    if not os.path.isfile(TOPK_FOLDER + str(k) + ".txt"):
        input_file = input_file_select(INPUT_FILENAME, k)
        highest_k(input_file, TOPK_FOLDER + str(k) + ".txt", k)
    return TOPK_FOLDER + str(k) + ".txt"


