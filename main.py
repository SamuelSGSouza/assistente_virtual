from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import json
import core

#TODO: Criar um arquivo separado para lidar com a sintetização de voz

# Configurando sintetizador de voz
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[-2].id)


def speak(texto):
    engine.say(texto)
    engine.runAndWait()


#TODO: Criar um arquivo separado para lidar com o reconhecimento de fala

# Configurando reconhecimento de fala
model = Model('model')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()


# Loop da escuta de áudio
while True:
    data = stream.read(2600)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        resultado = rec.Result()
        resultado = json.loads(resultado)

        if resultado is not None:
            text = resultado["text"]
            print(text)

            if text == "que horas são" or text == "me diga as horas":
                speak(core.SystemInfo.get_time())
