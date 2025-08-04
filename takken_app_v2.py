
import streamlit as st
import pandas as pd
import random

# データ読み込み
df = pd.read_csv("宅建過去問.csv")

# ヘッダー
st.markdown("<h3 style='font-size:22px;'>宅建 過去問カード（平成17年〜令和6年）</h3>", unsafe_allow_html=True)

# 年度・問題番号選択UI
st.sidebar.header("🔍 問題を検索")
years = sorted(df['年度'].unique(), reverse=True)
selected_year = st.sidebar.selectbox("年度を選択", years)

filtered_df = df[df["年度"] == selected_year]
selected_qnum = st.sidebar.number_input("問題番号（1〜50）", min_value=1, max_value=50, step=1)

# 検索結果の抽出
row = filtered_df[filtered_df["問題番号"] == selected_qnum]
if row.empty:
    st.warning("該当する問題が見つかりません。")
else:
    row = row.iloc[0]
    st.markdown(f"#### {row['年度']} 第{row['問題番号']}問")
    st.write(row["問題文"])

    for i in range(1, 5):
        opt = row.get(f"選択肢{i}", "")
        if pd.notna(opt) and str(opt).strip():
            st.markdown(f"- {i}. {opt}")

    if st.button("正解を表示"):
        st.success(f"✅ 正解：{row['正解']}")

# トレーニングセクション（ランダム出題＋前後移動）
st.sidebar.header("🎯 トレーニングモード")

if "train_index" not in st.session_state:
    st.session_state.train_index = 0

if st.sidebar.button("ランダム出題"):
    st.session_state.train_index = random.randint(0, len(df) - 1)

if st.sidebar.button("前の問題"):
    st.session_state.train_index = (st.session_state.train_index - 1) % len(df)

if st.sidebar.button("次の問題"):
    st.session_state.train_index = (st.session_state.train_index + 1) % len(df)

train_row = df.iloc[st.session_state.train_index]
st.divider()
st.markdown("### 🎲 ランダム出題 or 順番出題")

st.markdown(f"#### {train_row['年度']} 第{train_row['問題番号']}問")
st.write(train_row["問題文"])

for i in range(1, 5):
    choice = train_row.get(f"選択肢{i}", "")
    if pd.notna(choice) and str(choice).strip():
        st.markdown(f"- {i}. {choice}")

if st.button("この問題の正解を見る", key="train_answer"):
    st.success(f"✅ 正解：{train_row['正解']}")
