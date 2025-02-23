import streamlit as stlit
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

chatbot = pipeline("text-generation", model="distilgpt2")

# # chatbot function
def healthCareBot(userInput):
    if "symptom" in userInput :
        return 'Kindly consult doctor for accurate advice'
    elif "appintment" in userInput:
        return "Would you like to schedule an appointment with the Doctor?"
    elif "medication" in userInput:
        return "Its important to take pescribed medicines regularly.\tIf you have more concerns, consult your Doctor"
    else:
        response = chatbot(userInput, max_length = 500, num_return_sequences = 1)
        return response[0]['generated_text']

# # main function
def main():
    stlit.title("VigorBot : A Healthcare Assistant Chatbot")
    userInput = stlit.text_input("How can I assist you today ?")
    if stlit.button("Submit"):
        if userInput:
            stlit.write("User: ", userInput)
            with stlit.spinner("processing your query, wait fow few seconds..."):
                response = healthCareBot(userInput)
            stlit.write("Healthcare Assistant: ", response)
        else:
            stlit.write("Please Enter A Message To Get A Response.")

# if _name_ == '_main_':

main()