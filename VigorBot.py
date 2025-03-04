import streamlit as stlit
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#additional NLTK data
nltk.download('punkt')
nltk.download('stopwords')

#pre-trained Hugging face model
chatbot = pipeline("text-generation", model="distilgpt2")

# # chatbot function
def healthCareBot(userInput):
    #simple rule based keywords to response
    if "symptom" in userInput :
        return 'Kindly consult doctor for more accurate advice'
    elif "appointment" in userInput:
        return "Would you like to schedule an appointment with the Doctor?"
    elif "medication" in userInput:
        return "Its important to take pescribed medicines regularly.\tIf you have more concerns, consult your Doctor"
    else:
        #show number of possible outputs
        response = chatbot(userInput, max_length = 200, num_return_sequences = 1)
        return response[0]['generated_text']

# # main function
def main():
    #web app title
    stlit.title("VigorBot : A Healthcare Assistant Chatbot")
    #user input area
    userInput = stlit.text_input("Namaste! I am VigorBot. \nHow can I assist you today ?", "")
    if stlit.button("Submit"):
        if userInput:
            stlit.write("User: ", userInput)
            with stlit.spinner("processing your query, wait fow few seconds..."):  #display command during loading
                response = healthCareBot(userInput)
            stlit.write("Vigor_Bot: ", response)
        else:
            stlit.write("Please Enter A Message To Get A Response.")

# if _name_ == '_main_':

main()