# https://xlsxwriter.readthedocs.io/index.html
# https://xlsxwriter.readthedocs.io/format.html#format
import numpy as np
import pandas as pd
import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Hello world')
workbook.close()
