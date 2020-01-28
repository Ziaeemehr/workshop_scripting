import pandas as pd
import numpy as np


def method_1():
    # Create a Pandas dataframe from the data.
    df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


def method_2():

    # Create a Pandas dataframe from the data.
    df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')

    # Get the xlsxwriter objects from the dataframe writer object.
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.conditional_format('B2:B8',
                                 {'type':     'cell',
                                  'criteria': '>=',
                                  'value':    0,
                                  'format':   format1})
    writer.save()


def method_3():
    data = {'Numbers': [101000, 200140, 301550, 20210, 1125, 30140, 4521450],
            "Percentage": [0.10, 0.20, 0.30, 0.50, 0.44, 0.21, 0.14]}
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('pandas_simple.xlsx',
                            engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', header=False)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    header_format = workbook.add_format({
        "bold": True,
        "text_wrap": True,
        "valign": "top",
        "fg_color": "#D7E4BC",
        "border": 1
    })

    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num + 1, value, header_format)

    # Add some cell formats.
    format1 = workbook.add_format({'num_format': '#,##0.00'})
    format2 = workbook.add_format({'num_format': '0%'})

    # Set the column width and format.
    worksheet.set_column('B:B', 18, format1)
    # Set the format but not the column width.
    worksheet.set_column('C:C', 15, format2)
    writer.save()


def method_4():
    data = {'Numbers': np.random.uniform(100, 1000, 5),
            "Percentage": np.random.uniform(-5, 5, 5)}
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('pandas_simple.xlsx',
                            engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', header=True)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    # header_format = workbook.add_format({
    #     "bold": True,
    #     "text_wrap": True,
    #     "valign": "top",
    #     "fg_color": "#D7E4BC",
    #     "border": 1
    # })

    # for col_num, value in enumerate(df.columns.values):
    #     worksheet.write(0, col_num + 1, value, header_format)

    # Add some cell formats.
    format1 = workbook.add_format({'num_format': '#,##0.00'})
    format2 = workbook.add_format({'bg_color': '#C6EFCE',
                               'font_color': '#006100'})

    # Set the column width and format.
    worksheet.set_column('B:B', 18, format1)
    worksheet.conditional_format('C:C',
                                 {'type': 'cell',
                                  'criteria': '>0',
                                  'format': format2})
    # worksheet.conditional_format('C:C',
    #                              {'type':     'cell',
    #                               'criteria': '<=0',
    #                               'value':    0,
    #                               'format': format2_drop})
    writer.save()


method_4()
