import streamlit as st
import requests
import json

apikey = "<APIキー>"

chat_logs = []



st.title("文章チエック！！")

st.subheader("確認したいメッセージを入力してから送信！！")

message = st.text_input("メッセージ")


def send_pya3rt(endpoint, text, callback): # apikey, text, callback):
    data = {
        "text": "string",
        "key1": text,
    }
    
    if callback is not None:
        params['callback'] = callback
        
    url = "https://www.interlab-api.com:8001/"
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, headers=headers, data=json.dumps(data))

    return res.json()

def send_pya3rt_old(endpoint, text, callback): # apikey, text, callback):
    params = {#'apikey': apikey,
              #'query': text,
              'key1': text,
              }
    if callback is not None:
        params['callback'] = callback

    response = requests.post(endpoint, params)
    #response = requests.get(endpoint, params)

    return response.json()


def generate_response():
  
    #ans_json = send_pya3rt('https://api.a3rt.recruit.co.jp/talk/v1/smalltalk',
    #apikey, message, None)
    ans_json = send_pya3rt('http://ec2-44-205-107-207.compute-1.amazonaws.com:8000/Check',
                       message, None)
    #ans = ans_json['results'][0]['reply']
    ans = ans_json['key1']
    chat_logs.append('対象文章　　　:　 ' + message)
    chat_logs.append('この文章では？: 　' + ans)
    for chat_log in chat_logs:
        st.write(chat_log)
    #st.write(ans_json)

if st.button("送信"):
    generate_response()
