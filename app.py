from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

from langchain_community.vectorstores import InMemoryVectorStore
import streamlit as st
from time import sleep

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

if "vector_db" not in st.session_state:
    st.session_state.vector_db = None


#these two lines to show the messages on ui
if "messages" not in st.session_state:
    st.session_state.messages=[]

def document_process(path):
    #DOCUMENT LOADING
    loader = PyPDFLoader(path)
    docs = loader.load()

    #print(len(docs))

    #SPLITTING THE DOCUMENT

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(docs)

    #print(len(docs))

    #EMBEDDING AND VECTOR STORING

    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    vector_db = InMemoryVectorStore.from_documents(documents=docs, embedding=embeddings)

    st.session_state.vector_db = vector_db
    st.session_state.document_uploaded = True

    # USER QUERY TESTING
    #query = "is the patient has any health issues to concern?"

     #documents = vector_db.similarity_search(question=query, k=2)

    #print(len(documents))                  #gives length of documents variable i.e no of chunks
    #print(len(documents), documents[0])    #gives exact content particular indexed chunk
    #print(len(documents[1].page_content))  #gives the no of characters(size) of particular indexed chunk

    # CONTEXT GENERATION

    #context = ""
    #for doc in documents:
    #context = context + doc.page_content + "\n\n"

    # COMBINING CONTEXT AND ORIGINAL QUESTION

    #prompt = f"""YOU ARE A HELPFUL ASSISTANT AND PROVIDE ANSWER BASED ON THE PROVIDED context. context={context}, question={query}"""
    
    #llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
    #answer = llm.invoke(prompt)

    #print(answer.content[0]['text'])



# BUILDING USER INTERFACE

st.subheader("📑 Document Q&A Chatbot - Ask Anything")

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

#document upload
if not st.session_state.document_uploaded:
    file = st.file_uploader(label="Select Your PDF File", type="pdf")
    if file:
        with open("uploaded_document.pdf", "wb") as f:
            f.write(file.getvalue())
            st.markdown("Document Uploaded Successfully")

        with st.spinner("Processing...."):
          document_process("./uploaded_document.pdf")


        st.markdown("Document Processed Successfully")
        sleep(2)
        st.rerun()
             

# MAKING CHAT UI
if st.session_state.document_uploaded and st.session_state.vector_db:
    #these 4 lines for showing the stored data on ui
    for oneMessage in st.session_state.messages:
        role = oneMessage["role"]
        content = oneMessage["content"]
        st.chat_message(role).markdown(content)


    query = st.chat_input("Ask Anything...")
    if query:
        ##these two line to show whose message and what content
        st.session_state.messages.append({"role": "user","content": query})
        st.chat_message("user").markdown(query)

        documents = st.session_state.vector_db.similarity_search(query)
        context = ""

        for doc in documents:
            context += doc.page_content + "\n\n"


        prompt = f"""You are a helpful assistant and you provide answers for user questions based on the provided context, context: {context} and question is: {query}"""
        result = llm.invoke(prompt)

        #this one line to show whose message and what content
        st.session_state.messages.append({"role": "ai","content": result.content})

        st.chat_message("ai").markdown(result.content)



           
