from langchain_community.llms import ollama
import streamlit as st

txt_input = st.chat_input("Input Your Prompt")
# btn = st.button("Lets Cook")

if txt_input:

    llm = ollama.Ollama(model="qwen2.5")


    response = llm.invoke(txt_input)
    
    st.write(txt_input)

    st.markdown(response)




if __name__ == "__main__":
    print("Enter streamlit run connector.py to run")