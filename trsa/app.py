import streamlit as st
import streamlit.components.v1 as components
import os

# --- PAGE CONFIGURATION ---
# Streamlit 페이지의 기본 설정을 구성합니다.
# page_title: 브라우저 탭에 표시될 제목입니다.
# page_icon: 브라우저 탭에 표시될 아이콘입니다.
# layout: 페이지 레이아웃을 'wide'로 설정하여 넓게 표시합니다.
st.set_page_config(
    page_title="DB MISSION: UNLOCK THE TRANSACTION",
    page_icon="🚀",
    layout="wide"
)

# --- HTML FILE LOADER ---
# 'htmls' 폴더에 있는 HTML 파일을 읽어옵니다.
try:
    # 현재 스크립트 파일의 디렉토리 경로를 가져옵니다.
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # HTML 파일의 전체 경로를 조합합니다.
    html_path = os.path.join(parent_dir, "htmls", "index.html")

    # HTML 파일을 열고 내용을 읽습니다.
    with open(html_path, 'r', encoding='utf-8') as f:
        html_code = f.read()

    # --- RENDER HTML ---
    # 읽어온 HTML 코드를 Streamlit 컴포넌트로 렌더링합니다.
    # height를 1200px로 설정하여 충분한 세로 공간을 확보합니다.
    # scrolling=True로 설정하여 내용이 길어질 경우 스크롤이 가능하도록 합니다.
    components.html(html_code, height=1200, scrolling=True)

except FileNotFoundError:
    # 만약 'htmls/db_mission_page.html' 파일을 찾지 못하면 에러 메시지를 표시합니다.
    st.error("오류: 'htmls' 폴더 내에 'index.html' 파일을 찾을 수 없습니다.")
    st.info("app.py 파일과 같은 위치에 'htmls' 폴더를 생성하고, 그 안에 HTML 파일을 넣어주세요.")
