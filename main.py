import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
import openai
import config

# Initialize OpenAI API Key
openai.api_key = "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"

# Text-to-Speech Setup
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech Recognition (Voice Input)
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Could not connect to the internet."

# Get Response from OpenAI GPT
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "You are a helpful AI assistant."},
              {"role": "user", "content": prompt}],
    max_tokens=500  # Lower this to reduce cost
)
    return response["choices"][0]["message"]["content"]


# Execute Commands Based on User Input
def execute_command(command):
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time_now}")

    elif "search wikipedia" in command:
        query = command.replace("search wikipedia", "").strip()
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)

    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        response = ask_gpt(command)
        speak(response)

# Run the Assistant
if __name__ == "__main__":
    while True:
        command = listen()
        execute_command(command)
