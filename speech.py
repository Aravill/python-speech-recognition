from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from os import remove

r = sr.Recognizer()


def say(say):
    tts = gTTS(say)
    tts.save('say.mp3')
    playsound('say.mp3')
    remove('say.mp3')


def listen(callback=False):
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            if callback:
                callback()
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            say('Sorry, I did not get that.')
        except sr.RequestError:
            say('Sorry, my speech service is down.')
        return voice_data
