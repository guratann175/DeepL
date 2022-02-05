#使用ライブラリ
import deepl_get
import openpyxl

book = openpyxl.load_workbook('English.xlsx')
#openpyxlでエクセルファイルの読み込み
sheet = book['Sheet1']
#エクセルのシートの指定
strings = sheet.cell(row=2,column=2).value
#読み込みたいシートのセルを指定
output = deepl_get.deepl(strings)
sheet.cell(row = 2, column = 3).value = output
#特定のセルへの書き込み
book.save('English.xlsx')
#シートの保存　これを行わないと反映されません





