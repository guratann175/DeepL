#使用ライブラリ
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

browser = Service(executable_path="chromedriver.exe")
#使用ドライバの選択 (ブラウザのバージョンに留意)
url = "https://www.deepl.com/ja/translator"

options = Options()
options.add_argument('--headless')
#ブラウザの非表示

#importした際にここの処理を実行されないようにする
driver = webdriver.Chrome(service = browser, options=options)
#設定したオプションを引数に代入する　ブラウザ非表示

#ブラウザの立ち上げ
#Serviceオブジェクトにpathを渡してから、webdriverに渡す
driver.implicitly_wait(3)
driver.get(url)
time.sleep(5)
#相手のサーバーに負荷をかけないためにも必須な処理
input = driver.find_element(By.XPATH,'/html/body/div[3]/main/div[3]/div[3]/section[1]/div[3]/div[2]/textarea')
#XPATHで取得したい情報の場所の指定
print("アクセス成功")

def deepl(string):
#html(検証)から取得する関数
    input.clear()
#テキストエリアの中身を削除
    input.send_keys(string)
    print("キーワード入力完了")
    time.sleep(5)
    output = driver.find_element(By.ID,'target-dummydiv').get_attribute('textContent')
#.textだとなぜか帰ってこない。
#画面上に存在しないものは操作不可能な為無いモノとみなされる
#非表示文字列の取得 .get_attribute('textContent')
#deepLでは出力文字にボタンタグがつけられている
#get_attribute 属性名の指定
    print("翻訳完了")
    time.sleep(3)
    return output

def close():
    driver.close()
#ブラウザを閉じる

