import deepl
import deepl_txt
import PySimpleGUI as sg
#GUIを作るためのライブラリ
import tkinter.filedialog
#GUIを構築するためのライブラリ


sg.theme('Dark')
layout = [  [sg.Text('DeepL翻訳ツールへようこそ')],
            [sg.Button('ファイルを選択',key = 'input_file')],
            [sg.Text('ファイルパス'), sg.InputText(key = 'filepath', readonly=True)],
            [sg.Button('Translate', key = 'translate')],
            [sg.Button('閉じる', key = 'close')]   ]

window = sg.Window('DeepL',layout,size=(300,150))

while True:
    event, values = window.read()
    file_path = 'English_input.txt'

    if event == sg.WIN_CLOSED:
#ループを抜けるための処理:これがないとウィンドウを閉じられない
        break
    
    if event == 'input_file':
        file_path = tkinter.filedialog.askopenfilename()
#ファイル選択画面を開き、選択されたpathを変数に代入
        window['filepath'].update(file_path, text_color = ('#000000'))
        deepl_txt.input_txt(file_path)
    
    if event == 'translate':
            print(file_path)
            deepl.main()   

    if event == 'close':
        break
   
window.close()

