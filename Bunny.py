import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use female voice

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        speak("Sorry, I didn't catch that. Please say it again.")
        return "None"
    return query.lower()

def main():
    greet()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                speak(results)
            except:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif 'who is the prime minister of india' in query:
            speak("The Prime Minister of India is Narendra Modi.")

        elif 'who is the president of india' in query:
            speak("The President of India is Droupadi Murmu.")

        elif 'play old hindi songs' in query:
            speak("Playing old Hindi songs on YouTube.")
            webbrowser.open("https://www.youtube.com/results?search_query=old+hindi+songs")

        elif 'open youtube' in query:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stack Overflow.")
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\imami\\Videos\\git-action\\New_folder\\Dataflow"  # Change this to your path
            try:
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("Playing your music.")
                else:
                    speak("No songs found in your music folder.")
            except:
                speak("Music folder not found or empty.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            code_path = "C:\\Users\\YourName\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            speak("Opening Visual Studio Code.")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("I didn't understand that. Try asking something else.")

if __name__ == "__main__":
    main()