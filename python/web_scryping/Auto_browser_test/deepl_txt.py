import openpyxl

def input_txt(textfile):
    f = open(textfile, 'r', encoding = 'UTF-8')
    sentence = f.read()
    lists = sentence.split('.')

    book = openpyxl.load_workbook('English.xlsx')
    sheet = book['Sheet1']
#エクセルファイル、シートの読み込み
    sheet.delete_cols(2,2)
#特定のセル行列を削除、2列目から数えて2つの列を削除

    for i in range(len(lists)):
#for文と配列の組み合わせ 配列の要素数を求める関数lenと併用
        sheet.cell(row=i+2, column=2).value = lists[i]
    book.save('English.xlsx')
    print("エクセルファイルへの書き込みが完了しました")