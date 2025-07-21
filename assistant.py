import speech_recognition as sr
import pyttsx3
import requests

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 160)  # Adjust speech speed

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Capture voice command from microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Speech recognition service unavailable."

def ask_ai(question):
    """Send user input to Flask API."""
    response = requests.post("http://127.0.0.1:5000/ask", json={"message": question})
    return response.json().get("response", "No response from AI.")

def main():
    while True:
        command = recognize_speech()
        print("User:", command)

        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        ai_response = ask_ai(command)
        print("Assistant:", ai_response)
        speak(ai_response)

if __name__ == "__main__":
    main()
