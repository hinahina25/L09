import streamlit as st
st.title("ユーザー情報入力")

if 'user_name' not in st.session_state:
    st.session_state.user_name =""

name = st.text_input("あなたの名前を入力してください")
if st.button("名前を記憶"):
    st.session_state.user_name=name
    st.success("名前を保存しました")

st.write(f"記憶している名前: {st.session_state.user_name}")