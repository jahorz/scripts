# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:13:18 2023

@author: jakob
"""

import json

coverage_file = "PATH/TO/INPUT/COVERAGE/file.txt"
counts_file = "PATH/TO/OUTPUT/file.json"


def count_cov(input_file, output_file):
    count_dct = {}
    with open(input_file, "r") as coverage:
        line = coverage.readline()
        while line:
            c = line.split("\t")[2]
            if c in count_dct.keys():
                count_dct[c] = count_dct[c]+1
            else:
                count_dct[c] = 1
            line = coverage.readline()
    coverage.close()
    
    with open(output_file, "w") as out:
        out.write(json.dumps(count_dct))
        out.close()
    return count_dct

c = count_cov(coverage_file, counts_file)
