import speech_recognition as sr
import pyttsx3
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
load_dotenv()

os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=100)
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, phrase_time_limit = 5)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print(" ")
    except sr.RequestError as e:
        print("Sorry, there was an error retrieving the audio:", str(e))
    
    return ""


def speak(text):
    
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 180)
        engine.say(text)
        engine.runAndWait()

    except Exception as ex:
        print("Errors: {}".format(ex))


def main():

    st.title("VOX Voice Assistant")

    st.markdown("""

        <style>
            .stFileUploader label {
                font-size: 40px; /* Adjust font size as needed */
            }

        </style>

    """, unsafe_allow_html=True)
    
    
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("voice_assistant_logo.webp", width=200)
    
    pdf_file = st.file_uploader("Upload Document", type=["pdf"])
    
    if ((pdf_file is not None) and ('pdf' in str(pdf_file))):
        bytes_data = pdf_file.read()
        
        with open("sample_document.pdf", 'wb') as f: 
            f.write(bytes_data)
            f.close()

    count = 0    
    if st.button("Start Voice Chat"):
                
        speak("This is your VOX Voice Assistant. How can I assist you today?")
        while True:
            
            audio_value = st.audio_input("Your voice message", key=count)
            st.audio(audio_value)
            count += 1
            
            command = listen()
            print(command)
        
            if "hello" in command.lower():
                speak("Hello! How can I assist you today?")
            elif (("good bye" in command.lower()) or ("goodbye" in command.lower())):
                speak("Goodbye!")
                break
            elif (("thank you" in command.lower()) or ("thankyou" in command.lower())):
                speak("You welcome")
                  
            elif "what's your name" in command.lower():
                speak("My name is VOX Voice Assistant")
            elif "how are you" in command.lower():
                speak("I am fine, thank you. Hope you are also fine")
            elif "information" in command.lower():
                speak("What specific information do you need?")        
            elif "help" in command.lower():
                speak("Sure, I am here to help you only")
            elif "VOX" == command.lower().rstrip():
                speak("How may I help you?")
            elif "bye" in command.lower():
                break
                
                        
            else:
                
                prompt = command
                
                if prompt:
                    speak("I am collecting information for you, please wait")
                
                pdf_file = "sample_document.pdf"
                data = PyPDFLoader(pdf_file).load()
                    
                data_chunks = text_splitter.split_documents(data)
                
                vectorstore = FAISS.from_documents(data_chunks, embeddings)

                conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever(), memory=memory)
            
                result = conversation_chain({"question": prompt})
                answer = result["answer"]
                speak(answer)                
                speak("Do you have any other question?") 
        
        st.success('Results: {}'.format(str("End of Voice Chat................")))


if __name__=='__main__':
    main()