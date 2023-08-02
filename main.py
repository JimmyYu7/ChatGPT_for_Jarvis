import openai
import pyttsx3
import speech_recognition as sr
import sys
import threading
import os
from playsound import playsound

# Set up the ChatGPT API client
openai.api_key = "sk-*****"

# Set up the text-to-speech engine
engine = pyttsx3.init()

# Get the available voices
voice = engine.getProperty('voice')

# Set the voice to use
engine.setProperty('voice', voice[1])

# Set the volume
engine.setProperty('volume', 0.8)

# Set the rate at which the words are spoken
engine.setProperty('rate', 180)

# Set up the speech recognition engine
r = sr.Recognizer()

# Flag variable for the program status
running = True

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except Exception as e:
        print("Error: " + str(e))
        return None

def generate_response(prompt):
    try:
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2000,  # Reduced max tokens
            n=1,
            stop=None,
            temperature=0.3,  # Reduced temperature for more consistent output
        )

        message = completions.choices[0].text
        return message
    except Exception as e:
        print("Error: " + str(e))
        return "Sorry, I am currently unable to generate a response."

def play_audio(filename):
    try:
        playsound(filename)
    except Exception as e:
        print("Error: " + str(e))

audio_path = "/Users/jian.yu/Documents/Jimmy_github/j2.mp4"
play_audio(audio_path)
speak("Sir, Welcome home. How can I help you today?")

while running:
    prompt = listen()
    if prompt is not None:
        if prompt.lower() == "thank you for your help":
            # Exit the program
            running = False
        else:
            response = generate_response(prompt)
            speak(response)

            # Set up a timer to interrupt the text-to-speech engine after 10 seconds
            timer = threading.Timer(10.0, engine.stop)
            timer.start()

            # Speak the response
            response = generate_response(prompt)
            speak(response)

            # Cancel the timer if the response finishes speaking before it expires
            timer.cancel()
    else:
        speak("I'm sorry, I didn't understand that.")

