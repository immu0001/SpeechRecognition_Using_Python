import speech_recognition as sr
from speech_recognition import Microphone, RequestError, Recognizer, UnknownValueError

dir(sr)
import pyaudio
import webbrowser as wb

r1 = Recognizer()  # this is the recognizer class from speechRecognition
r2 = Recognizer()
r3 = Recognizer()

with sr.Microphone as source:
    print('[search Google: search YouTube]')
    print('Speak Now!!')
    audio = r3.listen(source)

    if 'video' in r1.recognize_google(audio):
        r1 = Recognizer()
        url = 'https://www.youtube.com/results?search_query='
        with sr.Microphone() as source:
            print('search your query')
            audio = r1.listen(source)

            try:
                get = r1.recognize_google(audio)
                print(get)
                wb.get().open_new(url + get)
            except UnknownValueError:
                print('error ')
            except RequestError as e:
                print('failed'.format(e))
