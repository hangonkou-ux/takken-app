
import streamlit as st
import pandas as pd

# CSVファイルの読み込み
df = pd.read_csv("宅建過去問.csv")

# セッション状態で現在の問題番号を管理
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0

# 表示対象の行
row = df.iloc[st.session_state.q_index]

# ヘッダー表示
st.title("宅建 過去問カード（平成17年〜令和6年）")
st.markdown(f"#### {row['年度']} 第{row['問題番号']}問")
st.write(row['問題文'])

# 選択肢
for i in range(1, 5):
    choice = row.get(f'選択肢{i}', "")
    if choice and str(choice).strip():
        st.button(f"{i}. {choice}")

# 正解表示
if st.button("正解を見る"):
    st.success(f"正解：{row['正解']}")

# 次の問題へ
if st.button("次の問題へ"):
    st.session_state.q_index = (st.session_state.q_index + 1) % len(df)
    st.experimental_rerun()
