import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import initialize_agent, AgentType, Tool
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import os
from dotenv import load_dotenv


## Create the arxiv and wiki tools
api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

search = GoogleSerperAPIWrapper(serper_api_key="18281fef750b82a35f57104bf0a037b43a3ff5bc")
search_tool = Tool(
    name="Google Search",
    func=search.run,
    description="Useful for when you need to answer questions about current events or general knowledge.",
)

st.set_page_config(page_title="AI Search Engine", page_icon=":mag:")
st.title("AI Search Engine :mag:") 

#''' In this example, we are using streamlitcallbackhandler to display the thoughts and actions of the agent in the streamlit app.'''

## Sidebar settings
st.sidebar.title("Settings")
groq_api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")

if not groq_api_key:
    st.info("Please add your groq api key to continue")
    st.stop()

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi I am a conversational search engine. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt:=st.chat_input(placeholder="What is machine Learning?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key=groq_api_key, model="llama3-8b-8192", streaming=True)
    tools = [wiki, arxiv, search_tool]

    search_agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handling_parsing_errors=True,
        handle_parsing_errors=True,
    )

    with st.chat_message("assistant"):
        # Create a callback to handle the streaming response
        with st.spinner("Going online..."):
            callback = StreamlitCallbackHandler(st.container(), expand_new_thoughts=True)
            response = search_agent.invoke({'input':prompt}, callbacks=[callback])
            answer = response['output']
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.write(answer)
    st.rerun()
        