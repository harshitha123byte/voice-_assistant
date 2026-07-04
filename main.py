import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You:", command)
        return command
    except:
        speak("Sorry, I didn't understand.")
        return ""

speak("Hello! I am your Python Voice Assistant.")

while True:
    command = take_command()

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + today)

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "")
        speak("Searching Wikipedia")
        try:
            result = wikipedia.summary(topic, sentences=2)
            speak(result)
        except:
            speak("No results found.")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        song = command.replace("play", "")
        speak("Playing on YouTube")
        pywhatkit.playonyt(song)

    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "calculator" in command:
        os.system("calc")

    elif "notepad" in command:
        os.system("notepad")

    elif "exit" in command or "stop" in command:
        speak("Goodbye. Have a nice day.")
        break

    else:
        speak("Please say the command again.")
