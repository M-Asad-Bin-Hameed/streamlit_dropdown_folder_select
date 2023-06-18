import streamlit as st
import os
import sys
import shutil
from pathlib import Path

st.set_page_config(layout = 'wide')
                   

if 'curr_directory' not in st.session_state:
    st.session_state['curr_directory'] = os.path.abspath('.')
    st.session_state['dir_list'] = \
        next(os.walk(st.session_state['curr_directory']))[1]

def run():
    files = \
        [file for file in os.listdir(st.session_state['curr_directory']) 
         if os.path.isfile(os.path.join(st.session_state['curr_directory'], file))]
    curr_dir_abs_path = os.path.abspath(st.session_state['curr_directory'])
    st.session_state['dir_list'] = next(os.walk(st.session_state['curr_directory']))[1]
    st.session_state['dir_list'] = sorted(st.session_state['dir_list'])
    st.session_state['dir_list'].insert(0,'.')
    st.session_state['dir_list'].insert(1,'..')
    st.markdown(
        f"**<font size=5>Currently in: {curr_dir_abs_path} </font>**",
        unsafe_allow_html=True,
    )
    
    option = st.selectbox(
        'Select Data folder', st.session_state['dir_list'],
        key='Folder_selector',index=0
        )

    if st.button('Change directory'):
        if option == '.':
            pass
        elif option == '..':
            path = Path(st.session_state['curr_directory'])
            st.session_state['curr_directory'] = \
                str(path.parent.absolute())
            st.session_state['dir_list'] = \
                next(os.walk(st.session_state['curr_directory']))[1]
        else:
            st.session_state['curr_directory'] = \
                            os.path.abspath(
                                os.path.join(
                                    st.session_state[
                                        'curr_directory'], option))

            st.session_state['dir_list'] = \
                next(os.walk(st.session_state['curr_directory']))[1]
        st.experimental_rerun()      

    st.markdown(
        f'**<font size=5>No. of files in the selected folder:'
        f'{len(files)} </font>**',
        unsafe_allow_html=True,
    )
    st.write(os.listdir(st.session_state['curr_directory']))

if __name__=='__main__':
    run()
