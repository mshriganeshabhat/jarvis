import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Adjust voice index (0 for male/Jarvis style, 1 for female depending on your OS)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170) # Speed of speech

def speak(text):
    """Makes the assistant speak."""
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listens to the user microphone and converts speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.WaitTimeoutError:
            return "none"
        except Exception:
            print("Could not understand audio, please try again.")
            return "none"

def run_jarvis():
    """Main logic to process commands."""
    speak("Jarvis is online. How can I help you today?")
    
    while True:
        query = take_command()
        
        if query == "none":
            continue
            
        # 1. Play songs on YouTube
        if 'play' in query:
            song = query.replace('play', '').strip()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
            
        # 2. Tell the current time
        elif 'time' in query:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {current_time}")
            
        # 3. Search Wikipedia
        elif 'who is' in query or 'what is' in query:
            search_query = query.replace('who is', '').replace('what is', '').strip()
            speak(f"Searching Wikipedia for {search_query}...")
            try:
                summary = wikipedia.summary(search_query, sentences=2)
                speak("According to Wikipedia:")
                speak(summary)
            except Exception:
                speak("I couldn't find any results on Wikipedia.")

        # 4. Say hello
        elif 'hello' in query or 'hi jarvis' in query:
            speak("Hello sir, everything is running smoothly.")

        # 5. Shut down Jarvis
        elif 'stop' in query or 'exit' in query or 'bye' in query:
            speak("Goodbye sir. Shutting down systems.")
            break
            
        else:
            speak("I didn't quite catch that. Could you repeat?")

if __name__ == "__main__":
    run_jarvis()
