import pandas as pd
import openpyxl
import os

def edit(files):
    print('sono1')
    print(files)
    #パスを作成
    edit_file_path = 'download/' + 'test' + '_result.xlsx'
    print('sono2')
    print(edit_file_path)
    #作成したパスにエクセルファイルを保存
    files[0].to_excel(edit_file_path)
    print('sono3')
    print(edit_file_path)
    workbook = openpyxl.load_workbook(edit_file_path)
    print('sono4')
    print(workbook)
    worksheet = workbook.worksheets[0]
    print('sono5')
    print(worksheet)

    #処理を保存
    workbook.save(edit_file_path)

    #パスを返す
    return edit_file_path[9:]