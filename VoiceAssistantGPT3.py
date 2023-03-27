import pandas as pd
import numpy as np
import subprocess
import sys
import os
import subprocess
import sys
import openai


openai.api_key = <Get you Key from OpenAI>


# Import necessary packages and modules, check if they are installed and install them if not
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import speech_recognition as sr
    import pyttsx3
    import nltk
except ImportError:
    install('SpeechRecognition')
    install('pyttsx3')
    install('nltk')
    import speech_recognition as sr
    import pyttsx3
    import nltk

# Define a function to listen to user input via microphone
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
    except Exception as e:
        print("Sorry, I could not understand that.")
        return None
    return text.lower()

# Define a function to speak a given text out loud using pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Define a function to process user input using GPT-3 API
def process(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{text}\n\nAnswer:",
        temperature=0.5,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    answer = response.choices[0].text.strip()
    return answer

# Define the main function
def main():
    # Greet the user
    speak("Hello, I am your voice assistant with GPT-3 integration. How can I help you today?")
    while True:
        # Listen to user input and convert it to text
        text = listen()
        if text:
            # Process the user input using GPT-3 API
            answer = process(text)
            # Speak the answer out loud
            speak(answer)
            # If the user says "exit" or "bye", break out of the loop and end the program
            if "exit" in text or "bye" in text:
                break

# Run the main function if this module is being run directly
if __name__ == "__main__":
    main()
