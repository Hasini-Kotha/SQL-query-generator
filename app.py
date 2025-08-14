import streamlit as st
import google.generativeai as genai

# 1. Set your Gemini API key
GOOGLE_API_KEY = "AIzaSyBNPnYC7bpK2J9YPD6SNkGTAPl-x-2-J-g"
genai.configure(api_key=GOOGLE_API_KEY)

# 2. Choose your working Gemini model
MODEL_NAME = "gemini-2.5-pro"

# 3. Save the model in session to reuse between interactions
if "model" not in st.session_state:
    st.session_state.model = genai.GenerativeModel(model_name=MODEL_NAME)

def main():
    # 4. Configure your Streamlit page
    st.set_page_config(page_title="SQL Query Generator 🔵", page_icon=":robot:")

    # 5. Introductory header
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>SQL Query Generator 🔵</h1>
            <h3>I can generate SQL Queries for you</h3>
            <p>Just type your request in plain English, and I’ll do the rest.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 6. Input box for user to type their question
    user_query = st.text_input("Enter your query in plain English:")

    # 7. Button to activate SQL generation
    if st.button("Generate SQL Query") and user_query:
        with st.spinner("Generating your SQL query..."):
            response = st.session_state.model.generate_content(user_query)
            st.subheader("Generated SQL Query & Explanation:")
            st.write(response.text)

if __name__ == "__main__":
    main()
