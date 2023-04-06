import time
import pandas as pd
import streamlit as st


@st.cache_data(show_spinner=False)
def create_df(file: str):
    return pd.read_json(file)


@st.cache_data(show_spinner=False)
def convert_df(df):
    return df.to_csv().encode('utf-8')


def generate_file_name():
    # generate a file name
    date_time = time.strftime("%Y%m%d-%H%M%S")
    return f"json2csv-{date_time}.csv"


def app_config():
    st.set_page_config(
        page_title="JSON to CSV",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': "https://github.com/chankruze/json2csv",
            'Report a bug': "https://github.com/chankruze/json2csv/issues/new",
            'About': "https://github.com/chankruze/json2csv/blob/main/README.md",
        },
    )


def hide_menu_style():
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


if __name__ == '__main__':
    # configure the app
    app_config()
    # hide the menu and footer
    hide_menu_style()
    # ask the user for the file name
    uploaded_file = st.file_uploader("Choose a file")
    # check if the user uploaded a file
    if uploaded_file is not None:
        # convert json to a dataframe
        with st.spinner("Converting JSON to CSV..."):
            dataframe = create_df(uploaded_file)

            st.write("#### 📊 Data Preview")
            # show the dataframe in the app
            st.write(dataframe)
            # convert the dataframe to csv
            csv = convert_df(dataframe)

            st.write("#### 📥 Download")
            # show the download button in the app to download the csv file
            st.download_button(
                label="Download as CSV",
                data=csv,
                file_name=generate_file_name(),
                mime='text/csv',
            )

            st.write("#### 📝 Privacy & Security")
            st.write("1. The file is cached for 10 minutes.")
            st.write("2. The file is deleted after 10 minutes.")
            st.write("3. The file is not stored anywhere.")
            st.write("4. The file is not shared with anyone.")
            st.write("5. The file is not used for any other purpose.")
            st.write("")
            st.write("Made with ❤️ by [chankruze](https://github.com/chankruze)")

            # drop snow on the app
            st.snow()
