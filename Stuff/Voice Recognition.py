import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('Yokozo to soul society')

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print('listening...')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text = text.lower()

        talk(text)
        print('')
        print(text)

    except:
        print('Please Try Again!')
