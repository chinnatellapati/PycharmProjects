# Read filename from input and process the XL. We can use this program to process many XL sheets. Use display files in a directory
#function and supply as input to this program

import openpyxl as xl
from openpyxl.chart import BarChart, Reference

def process_workbook(filename):
    work_book = xl.load_workbook('filename')
    sheet = work_book['Sheet1']
    cell = sheet['a1']

    for row in range(2, sheet.max_row + 1):
        cell = sheet.cell(row, 3)
        corrected_price = cell.value * 0.9
        corrected_price_cell = sheet.cell(row, 4)
        corrected_price_cell.value = corrected_price
    values = Reference(sheet,
              min_row=2,
              max_row=sheet.max_row,
              min_col=4,
              max_col=4)

    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart, 'e2')


    work_book.save('finename')


