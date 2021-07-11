import pandas as pd
import openpyxl
import os

def edit(files):

    #パスを作成
    edit_file_path = 'download/' + 'test' + '_result.xlsx'
    #作成したパスにエクセルファイルを保存
    edit_df.to_excel(edit_file_path)

    workbook = openpyxl.load_workbook(edit_file_path)
    worksheet = workbook.worksheets[0]

    #処理を保存
    workbook.save(edit_file_path)

    #パスを返す
    return edit_file_path[9:]