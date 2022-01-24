from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import json


# Configurando sintetizador de voz
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[-2].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


# Configurando reconhecimento de fala
model = Model('model')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()


# Iniciando projeto
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        resultado = rec.Result()
        resultado = json.loads(resultado)

        if resultado is not None:
            text = resultado["text"]
            print(text)
            speak(text)
