import pandas as pd
import numpy as np
import pandas as pd
from PIL import Image
import time
import streamlit as st
from datetime import datetime
from time import sleep
import csv

path='data.csv'
df3=pd.read_csv(path)

st.bar_chart(df3.set_index('date'))




# 現在の日時を取得
now=datetime.now()
toda = str(now.date())
nowtime=now.time()
nowtime=str(nowtime.replace(microsecond=0))


        

if 'count' not in st.session_state:#もしcountがsession_stateに追加されていなかったら
    st.session_state.count=0#countを(key)として、valueに０を入れる

if 'arat' not in st.session_state:#もしcountがsession_stateに追加されていなかったら
    st.session_state.arat=40000#countを(key)として、valueに０を入れる

btnstart=st.button("開始")
kakufin=st.button("終了")
timest=st.title("")

if btnstart:
    timest=st.title("")
    #秒数から時間と分と秒を割り出して表示
    for i in range(st.session_state.count,36000):
        st.session_state.count=i
        sleep(1)
        if kakufin:
            break

if kakufin:
    df = pd.read_csv(path)
    matubi=df.tail(1).values.tolist()
    matubi=matubi[0]
    
    print(matubi)
    print(now.date())


    if str(matubi[0])==str(now.date()):
        df2 = pd.read_csv(path)

        # 末尾の行を削除する
        df2 = df2.drop(df2.index[-1])

        # 新しいデータを作成する
        new_data = [ datetime.now().date(),st.session_state.count / 60+matubi[1]]

        #new_row = pd.Series(new_data)

        # 新しいデータを末尾に追加する
        #df2 = df2.append(new_row, ignore_index=True)
        df2.loc[len(df2)] = new_data

        
        # 新しいCSVファイルに書き込む
        df2.to_csv(path, index=False)
        print('true')

    else:
        

        with open(path, 'a') as f:
           writer = csv.writer(f)
           dataa=[now.date(),st.session_state.count/60]
           writer.writerow(dataa)
           print('false')

    hours=st.session_state.count/3600
    minutes=(st.session_state.count/60)%60
    seconds=st.session_state.count%60
    timeha=("{:02}時間{:02}分{:02}秒".format(int(hours), int(minutes), int(seconds)))
    timest=st.title(f"スコア：{timeha}")
    st.session_state.count=0
