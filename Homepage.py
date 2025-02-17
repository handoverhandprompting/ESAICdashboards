import streamlit as st
from models import baseline_model, prediction_model
from layout_css import expander_layout
from streamlit_extras.stylable_container import stylable_container

if '_language' not in st.session_state:
    st.session_state['_language'] = 'chinese'


def run():
    st.set_page_config(layout="wide")
    expander_layout()

    # Set default language
    if '_language' not in st.session_state:
        st.session_state['_language'] = 'chinese'
    with st.container():
        col, but_col = st.columns([5, 1])
        with but_col:
            language_button = st.button('Language')
            if language_button:
                if st.session_state['_language'] == 'chinese':
                    st.session_state['_language'] = 'english'
                elif st.session_state['_language'] == 'english':
                    st.session_state['_language'] = 'chinese'

    st.header('國立臺灣大學醫學院附設醫院 心臟衰竭藥事照護服務
')
    st.write('- 您知道為什麼要吃這些藥嗎？ -
- 您對於藥品有很多疑問嗎？ -
- 您想要看懂自己的抽血報告嗎？ -
- 您希望更瞭解自己目前心臟衰竭的情況嗎？ -

您的需求，我們都聽到了
藥師通通都可以耐心為您解答

有了這個互動式數位工具之後，您可以用更簡單的方式來瞭解這些問題
')

if __name__ == '__main__':
    run()
