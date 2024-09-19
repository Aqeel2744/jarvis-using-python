
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert the text into speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take a command and perform tasks based on that command
def processcommand(c):
    c = c.lower() 
    print(f"Processing command: {c}")  # For debugging

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("http://facebook.com")
    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("http://linkedin.com")
    elif "open github" in c:
        speak("Opening GitHub")
        webbrowser.open("http://github.com")
    elif c.startswith("play"):
        try:
           
            song = c.split(" ", 1)[1]  # Split the command and get the second word as the song name
            link = musiclibrary.music(song)  # Fetch the music link using the musiclibrary module
            speak(f"Playing {song}")
            webbrowser.open(link)
        except IndexError:
            speak("Please specify a song name.")
        except Exception as e:
            speak(f"Error playing song: {str(e)}")

if __name__ == '__main__':
    speak("Hello Aqeel, how can I help you?")
    
    while True:
        try:
            # Listening for the "Jarvis" command
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.3)  # Quick noise calibration
                print("Listening for 'Jarvis'...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            
            if word.lower() == "jarvis":
                speak("Yes, I am here to help you!")
                print("Jarvis activated!")
                
                # After Jarvis is activated, listen for the next command
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.3)  # Adjust for ambient noise
                    print("Listening for your command...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print(f"Command received: {command}")  # For debugging
                    processcommand(command)

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")
            speak("There was an issue with Google Speech Recognition service.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            speak("An error occurred, please try again.")


