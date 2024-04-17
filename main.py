import pandas as pd
import pandas as pd
import time
import streamlit as st
from datetime import datetime
from time import sleep
import csv

st.markdown("""
試作として作成した勉強時間記録アプリです。
勉強開始ボタンもしくはを押すと時間の計測を開始します。
終了ボタンを押すと、計測を終了し、スコアとして経過時間を表示します。

計測した時間は該当する日付に追加されグラフ化されます。勉強時間が青、水色が休憩時間です。            
""")

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

if 'btntype' not in st.session_state:#もしcountがsession_stateに追加されていなかったら
    st.session_state.btntype='no'#countを(key)として、valueに０を入れる

btnstart=st.sidebar.button("勉強開始")
btnbreak=st.sidebar.button('息抜き開始')
kakufin=st.sidebar.button("終了")
timest=st.title("")

def btn():
    timest=st.title("")
    if btnstart==True:
        st.session_state.btntype='btnstart'
                
    elif btnbreak==True:
        st.session_state.btntype='btnbreak'


    #秒数から時間と分と秒を割り出して表示
    for i in range(st.session_state.count,36000):
        st.session_state.count=i
        sleep(1)
        if kakufin:
            break

if btnstart:
    btn()
    

if btnbreak:
    btn()

if kakufin:
    df = pd.read_csv(path)
    matubi=df.tail(1).values.tolist()
    matubi=matubi[0]


    if str(matubi[0])==str(now.date()):
        df2 = pd.read_csv(path)

        # 末尾の行を削除する
        df2 = df2.drop(df2.index[-1])
        new_data=[]

        # 新しいデータを作成する
        if st.session_state.btntype=='btnstart':
            new_data = [ datetime.now().date(),st.session_state.count / 60+matubi[1],matubi[2]]

        elif st.session_state.btntype=='btnbreak':
            new_data = [ datetime.now().date(),matubi[1],st.session_state.count / 60+matubi[2]]

        #new_row = pd.Series(new_data)

        # 新しいデータを末尾に追加する
        #df2 = df2.append(new_row, ignore_index=True)
        df2.loc[len(df2)] = new_data

        
        # 新しいCSVファイルに書き込む
        df2.to_csv(path, index=False)

    else:
        with open(path, 'a') as f:
           writer = csv.writer(f)
        if st.session_state.btntype=='btnstart':
            dataa = [ datetime.now().date(),st.session_state.count / 60,0]
        
        elif st.session_state.btntype=='btnbreak':
           dataa=[now.date(),0,st.session_state.count/60]

    hours=st.session_state.count/3600
    minutes=(st.session_state.count/60)%60
    seconds=st.session_state.count%60
    timeha=("{:02}時間{:02}分{:02}秒".format(int(hours), int(minutes), int(seconds)))
    timest=st.title(f"スコア：{timeha}")
    st.session_state.count=0
