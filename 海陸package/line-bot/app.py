#https://github.com/MarkwwLiu/PythonBasicTeaching/blob/master/LineBot/Chapter_1/app.py
#https://markteaching.com/create-line-bot/
from flask import Flask, request, abort
import pandas as pd
import base64
import requests
import tempfile
import io
import random
from fuzzywuzzy import process, fuzz
import re
from datetime import datetime,timezone,timedelta
import numpy as np 
import matplotlib.pyplot as plt
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#import psycopg2
from pandas.plotting import table
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
plt.rcParams['font.family'] = 'Noto Sans Mono CJK TC'
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('*****')
# Channel Secret
handler = WebhookHandler('*****')

#open file 19$
scopes = ["https://spreadsheets.google.com/feeds"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scopes) 
client = gspread.authorize(credentials)
sheet = client.open_by_key("*******").worksheet("Part3D")
df = pd.DataFrame(sheet.get_all_values(),columns = ['帳戶名稱','分級','機會名稱','結帳日期','產品代碼','產品描述','產品名稱','數量','規格','總價貨幣','總價','循環天數']) 

#tools for text
def xxx_number(word_string):
    word_string = word_string.strip()
    try:
        if(len(re.findall(r"\d+", word_string))>=0 and len(re.findall(r"\d+", word_string))<=2):
            return [word_string]
        elif (len(re.findall(r"\d+", word_string))>2 and len(re.findall(r"\d+", word_string))<=4):
            return knife(word_string,2)
        elif (len(re.findall(r"\d+", word_string))>4 and len(re.findall(r"\d+", word_string))<=6):
            return knife(word_string,3)
        elif (len(re.findall(r"\d+", word_string))>6 and len(re.findall(r"\d+", word_string))<=8):
            return knife(word_string,4)
    except:
        print("out of bound (defult = 4 )")       

def knife(somestring,cut):
    try:
        if somestring.count(' ') == (cut-1):
            return somestring.split()
        elif somestring.count(' ') == (cut*2-1):
            temp = somestring.split()
            return [ temp[i*2]+" "+temp[i*2+1] for i in range(int(len(temp)/2)) ]
    except:
        print("Please enter your orders one by one!")
        
def cut_number(word_string):
    matches = ["桶", "(", ")",""]
    try:
        if any(x in word_string for x in matches):
            if len(re.findall(r"\d+", word_string)) >=2:
                return re.findall(r"\d+", word_string)[-1]
            else:
                return re.findall(r"\d+", word_string)[0]
        else:
            return word_string
    except:
        return "1"
        #print("Something wrong when cutting numbers!")

# finding product in text
def find_product(client_name, product_name):
    client_list = list(df.帳戶名稱.unique())
    if client_name in client_list or loop_for_menu(client_list, client_name)[1] > 50:
        smaller_list = [ j.lower() for j in list(df[df['帳戶名稱']==client_name].產品名稱.unique())]
        product_name = product_name.lower()
        result = loop_for_menu(smaller_list, product_name)
        if result[1] == 0 :
            smaller_list = [ j.lower() for j in list(df.產品名稱.unique()) ]
            result = loop_for_menu(smaller_list, product_name) 
        #短的都要有 + 數字段要一樣
        elif len({x for x in product_name if x not in result[0]}) != 0 or len(list(set(re.findall('[\d]+',product_name)).intersection(re.findall('[\d]+',result[0]))))== 0:
            smaller_list = [ j.lower() for j in list(df.產品名稱.unique()) ]
            smaller_list.remove("%s"%result[0])
            result = loop_for_menu(smaller_list, product_name) 
            
    else:
        smaller_list = [ j.lower() for j in list(df.產品名稱.unique()) ]
        result = loop_for_menu(smaller_list, product_name)
    return result[0]

def loop_for_menu(menu, something):
    temp_name = ""
    temp_scoreofsimilarity_partial = 0
    for word in menu:
        if temp_scoreofsimilarity_partial < fuzz.partial_ratio( something, word):
            temp_scoreofsimilarity_partial = fuzz.partial_ratio( something, word)
            temp_name = word
        elif temp_scoreofsimilarity_partial == fuzz.partial_ratio( something, word):
                if len({x for x in something if x not in word}) == 0:
                    temp_name = word
#         print(word,something,temp_scoreofsimilarity_partial,temp_name)
    return [temp_name,temp_scoreofsimilarity_partial]

#############google_business#############

# get company name
def client_company_relationship(client_id):
    #open file 1dem
    scopes = ["https://spreadsheets.google.com/feeds"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scopes) 
    client = gspread.authorize(credentials)
    sheet = client.open_by_key("*****").sheet1

    id_table = pd.DataFrame(sheet.get_all_values() ,columns = ['Client Name' , 'Contact Person'])
    return id_table[id_table['Contact Person'] == client_id]['Client Name'].values[0]

def write_google_sheet(which_sheet,add_stuff):
    #open file 19
    if which_sheet =="19":
        sheet_key = "*****"
    else:
        sheet_key = "*****"
    scopes = ["https://spreadsheets.google.com/feeds"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scopes) 
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(sheet_key).sheet1

    #lock_of_clinet_list
    if which_sheet =="19":
        sheet.append_rows([add_stuff[0]])
    else:
        id_table = pd.DataFrame(sheet.get_all_values() ,columns = ['Client Name' , 'Contact Person'])
        if add_stuff[1] in id_table['Contact Person'].values:
            sheet.update_cell(id_table[id_table["Contact Person"]==add_stuff[1]].index[0]+1, 1,  add_stuff[0])
        else:
            sheet.append_rows([add_stuff])

def welcome_new_client(comp,nickname):
    #open file 1dem
    scopes = ["https://spreadsheets.google.com/feeds"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scopes) 
    client = gspread.authorize(credentials)
    sheet = client.open_by_key("*****").worksheet("Part3D")
    
    result = loop_for_menu(sheet.col_values(1), comp)
    if len({x for x in comp if x not in result[0]}) ==0 and result[1]>50: 
        confirm_template_message = TemplateSendMessage(alt_text='是\"%s\"嗎?'%result[0],template=ConfirmTemplate(text='是\"%s\"嗎?'%result[0],actions=[PostbackAction(label='是',data='T&%s'%result[0]),PostbackAction(label='不是',data='F&%s$%s'%(comp,result[0]))]))
    else:
        confirm_template_message = TemplateSendMessage(alt_text='是\"%s\"嗎?'%comp,template=ConfirmTemplate(text='請問是\"%s\"嗎?'%comp,actions=[PostbackAction(label='是',data='T&%s'%comp),PostbackAction(label='不是',data='F')]))
    return confirm_template_message

def welcome_new_comp(comp,nickname):
    #open file 1dem
    scopes = ["https://spreadsheets.google.com/feeds"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scopes) 
    client = gspread.authorize(credentials)
    sheet = client.open_by_key("*****").worksheet("Part3D")

    confirm_template_message = TemplateSendMessage(alt_text='那是\"%s\"嗎?'%comp,template=ConfirmTemplate(text='是\"%s\"嗎?'%comp,actions=[PostbackAction(label='是',data='T&%s'%comp),PostbackAction(label='不是',data='x')]))
    return confirm_template_message

def check_my_order(Contact_Person_Name):
    #open file 19
    client_id = client_company_relationship(Contact_Person_Name)
    scopes = ["https://spreadsheets.google.com/feeds"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scopes) 
    client = gspread.authorize(credentials)
    sheet = client.open_by_key("*****").sheet1

    record_csv = pd.DataFrame(sheet.get_all_values(), columns = ['Client Name' ,'Contact Person', 'Order product', 'Quantity','Ordered time'])
    
    record_csv = record_csv[record_csv['Contact Person'] == Contact_Person_Name].tail(12)
    
    fig, ax = plt.subplots(figsize=(8, 3)) 
    ax.xaxis.set_visible(False)  
    ax.yaxis.set_visible(False)  
    ax.set_frame_on(False)  
    tab = table(ax, record_csv,loc = "upper left")  
    tab.auto_set_font_size(False)
    tab.set_fontsize(9) 
    tab.auto_set_column_width(col=list(range(len(record_csv.columns))))

    buf = io.BytesIO()
    fig.savefig( buf, format='png')
    buf.seek(0)
    headers = {'Authorization': '*****'}
    files = {'smfile': buf.getvalue()}
    url = 'https://sm.ms/api/v2/upload'
    res = requests.post(url, files=files, headers=headers).json()
    if res['success'] :
        return res['data']['url']
    else:
        return res['images']

    
def cope_with_text(Contact_Person_Name,text_content):
    client_id = client_company_relationship(Contact_Person_Name)
    stuff =""
    text_order = ""
    order_list = xxx_number(text_content)
    for order in order_list:
        order_number = cut_number(order)
        order = re.findall('[\w\d]+[\u4e00-\u9fff]?',order)[0]
        #print("start!------------------------------------",order,"+" ,order_number)
        order_product = find_product(client_id, order)
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt2 = dt1.astimezone(timezone(timedelta(hours=8)))
        dfNew=pd.DataFrame([(client_id,Contact_Person_Name, order_product, order_number,dt2.strftime("%Y-%m-%d %H:%M"))],columns = ['Client Name' ,'Contact Person' , 'Order product', 'Quantity','Ordered time'])
        #print("end$------------------------------------",order_product,"+" ,order_number) 
        newstuff = client_id+","+Contact_Person_Name+","+ order_product+","+ order_number+","+dt2.strftime("%Y-%m-%d %H:%M")+"$"
        stuff = stuff + newstuff
        text_order = text_order + "\n"+order_product+"*"+str(order_number)
    confirm_template_message = TemplateSendMessage(alt_text='請確認訂單如下',template=ConfirmTemplate(text='請確認訂單如下：%s'%text_order,actions=[PostbackAction(label='確認',data='Y&%s'%str(stuff)),PostbackAction(label='取消',data='N')]))
    return confirm_template_message

#tools stop here

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    profile = line_bot_api.get_profile(user_id)
    if  event.message.text == "馬上訂購":      
        try:
            client_company_relationship(profile.display_name)
            message = TextSendMessage(text="%s您好，請開始下單"%profile.display_name)
            line_bot_api.reply_message(event.reply_token, message)
        except IndexError:
            message = TextSendMessage(text="你好%s，或許我們是第一次接觸，請告訴我您公司的全名是?"%profile.display_name)
            line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == "訂單查詢":      
        try:
            pictur_url = check_my_order(profile.display_name)
            table_img = ImageSendMessage(pictur_url, pictur_url)
            line_bot_api.reply_message(event.reply_token, table_img)
            message = TextSendMessage(text="若需刪除訂單，請聯絡客服人員")
            line_bot_api.reply_message(event.reply_token, message)
        except IndexError:  
            message = TextSendMessage(text="你好%s，或許我們是第一次接觸，請告訴我您公司的全名是?"%profile.display_name)
            line_bot_api.reply_message(event.reply_token, message)
        else:
            message = TextSendMessage(text="未找到相關訂單，若有問題，請聯絡客服人員")
            line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == "聯絡客服人員": 
        message = TextSendMessage(text="已通知客服人員，我們會在最短時間內與您聯絡~")
        line_bot_api.reply_message(event.reply_token, message)
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt2 = dt1.astimezone(timezone(timedelta(hours=8)))

        try:
            line_bot_api.push_message('*****', TextSendMessage(text='代表%s的%s於%s要求客服，請盡速與他聯絡'%(client_company_relationship(profile.display_name),profile.display_name,dt2.strftime("%Y-%m-%d %H:%M"))))
        except IndexError:
            line_bot_api.push_message(user_id, TextSendMessage(text="你好%s，或許我們是第一次接觸，請告訴我您公司的全名是?"%profile.display_name))
            line_bot_api.push_message('*****', TextSendMessage(text='%s於%s要求客服，請盡速與他聯絡'%(profile.display_name,dt2.strftime("%Y-%m-%d %H:%M"))))


    elif len(set(event.message.text).intersection(set("公司廠行社")))!=0:
        message2 = welcome_new_client(event.message.text,profile.display_name)
        line_bot_api.reply_message(event.reply_token, message2)
    else:
        try:
            message2 = cope_with_text(profile.display_name,event.message.text)
            line_bot_api.reply_message(event.reply_token, message2)
        except IndexError:
            sticker_list = [52002738, 52002763, 52002742, 52002736, 52002768]
            message3 = StickerMessage(package_id=11537,sticker_id=random.choice(sticker_list))
            message = TextSendMessage(text="%s你好，若須聯絡客服、查詢訂單、開始訂購，請用選單按鈕~"%profile.display_name)
            line_bot_api.reply_message(event.reply_token, [message3, message])

@handler.add(PostbackEvent)
def handle_postback(event):
    user_id = event.source.user_id
    profile = line_bot_api.get_profile(user_id)
    if event.postback.data[0:1] == "T":
        add_str = (event.postback.data[2:],profile.display_name)
        write_google_sheet("1dem",add_str)
        message = TextSendMessage(text="好的%s，我記住了!"%profile.display_name)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.postback.data[0:1] == "Y":
        add_str =  tuple(tuple(i.split(",")) for i in tuple(event.postback.data[2:][:-1].split("&")))
        write_google_sheet("19",add_str)
        message = TextSendMessage(text="好的%s，我下單了!"%profile.display_name)
        line_bot_api.reply_message(event.reply_token, message)

    elif event.postback.data[0:1] == "F":
        if len(event.postback.data) ==1:
            message3 = StickerMessage(package_id=11538,sticker_id=51626519)
            message2 = TextSendMessage(text="咦!不對嗎?公司名稱可能要打詳細點喔~")
            line_bot_api.reply_message(event.reply_token, [message3, message2])

        elif event.postback.data[2:].split("$")[0] == event.postback.data[2:].split("$")[1]:
            message3 = StickerMessage(package_id=11537,sticker_id=52002758)
            message2 = TextSendMessage(text="%s的%s，給我記住!明明就一樣，我要牙起來喽~"%(event.postback.data[2:].split("$")[0],profile.display_name))
            add_str = (event.postback.data[2:].split("$")[0],profile.display_name)
            write_google_sheet("1dem",add_str)
            line_bot_api.reply_message(event.reply_token, [message3, message2])
        else:
            message2 = welcome_new_comp(event.postback.data[2:].split("$")[0],profile.display_name)
            line_bot_api.reply_message(event.reply_token, message2)

    elif event.postback.data[0:1] == "x":
        message3 = StickerMessage(package_id=11538,sticker_id=51626519)
        message2 = TextSendMessage(text="咦!不對嗎?公司名稱可能要打詳細點喔~")
        line_bot_api.reply_message(event.reply_token, [message3, message2])

    elif event.postback.data[0:1] == "N":
        message3 = StickerMessage(package_id=11538,sticker_id=51626506)
        message2 = TextSendMessage(text="咦!不對嗎?商品名稱可能要打詳細點，或聯絡客服喔~")
        line_bot_api.reply_message(event.reply_token, [message3, message2])
        

@app.route('/')
def index():
    return 'Hello World!'

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)