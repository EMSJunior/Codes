# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 00:08:12 2020

@author: Luiz

"""


import os
import glob
import csv
from xlsxwriter.workbook import Workbook


def convertCSV(csvfile):
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()

