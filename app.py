import streamlit as st
import requests

apikey = "<APIキー>"

chat_logs = []

st.title("Chatbot with streamlit")

st.subheader("メッセージを入力してから送信をタップしてください")

message = st.text_input("メッセージ")


def send_pya3rt(endpoint, text, callback): # apikey, text, callback):
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
    ans_json = send_pya3rt('http://51f9-35-233-238-146.ngrok.io/Check',
                       message, None)
    #ans = ans_json['results'][0]['reply']
    #ans = ans_json['results'][0]['key1']
    #chat_logs.append('you: ' + message)
    #chat_logs.append('AI: ' + ans_json ) #ans)
    #for chat_log in chat_logs:
    #    st.write(chat_log)
    st.write(ans_json)

if st.button("送信"):
    generate_response()
