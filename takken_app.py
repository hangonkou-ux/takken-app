
import streamlit as st
import pandas as pd

# CSVファイルの読み込み
df = pd.read_csv("宅建過去問.csv")

# ページタイトル（小さめ）
st.markdown("<h3 style='text-align: center;'>宅建 過去問カード（平成17年〜令和6年）</h3>", unsafe_allow_html=True)

# 年度と問題番号の一覧取得
years = df["年度"].unique()
years = sorted(years, reverse=True)
selected_year = st.sidebar.selectbox("年度を選択", years)

numbers = df[df["年度"] == selected_year]["問題番号"].unique()
selected_number = st.sidebar.selectbox("問題番号を選択", numbers)

# 対象の行を取得
row = df[(df["年度"] == selected_year) & (df["問題番号"] == selected_number)]

if not row.empty:
    st.markdown(f"### 【{row.iloc[0]['年度']}・問{row.iloc[0]['問題番号']}】")
    st.write(row.iloc[0]["問題文"])

    options = [row.iloc[0]["選択肢1"], row.iloc[0]["選択肢2"], row.iloc[0]["選択肢3"], row.iloc[0]["選択肢4"]]
    for i, option in enumerate(options, start=1):
        if pd.notna(option) and option.strip() != "":
            st.markdown(f"**{i}.** {option}")

  
import streamlit as st
import pandas as pd

# CSVファイルの読み込み
df = pd.read_csv("宅建過去問.csv")

# ページタイトル（小さめ）
st.markdown("<h3 style='text-align: center;'>宅建 過去問カード（平成17年〜令和6年）</h3>", unsafe_allow_html=True)

# 年度と問題番号の一覧取得
years = df["年度"].unique()
years = sorted(years, reverse=True)
selected_year = st.sidebar.selectbox("年度を選択", years)

numbers = df[df["年度"] == selected_year]["問題番号"].unique()
selected_number = st.sidebar.selectbox("問題番号を選択", numbers)

# 対象の行を取得
row = df[(df["年度"] == selected_year) & (df["問題番号"] == selected_number)]

if not row.empty:
    st.markdown(f"### 【{row.iloc[0]['年度']}年・問{row.iloc[0]['問題番号']}】")
    st.write(row.iloc[0]["問題文"])

    options = [row.iloc[0]["選択肢1"], row.iloc[0]["選択肢2"], row.iloc[0]["選択肢3"], row.iloc[0]["選択肢4"]]
    for i, option in enumerate(options, start=1):
        if pd.notna(option) and option.strip() != "":
            st.markdown(f"**{i}.** {option}")

    with st.expander("🔽 正解を見る"):
        correct = row.iloc[0]['正解']
        if pd.notna(correct):
            try:
                correct = int(float(correct))  # 小数点を整数に変換
            except:
                pass
            st.markdown(f"**正解：{correct}**")
else:
    st.warning("該当する問題が見つかりませんでした。")
