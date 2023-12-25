from decoding import transcribe_audio
from speech_processing import record_from_microphone
import keyboard
import time
from filewrite import save_results


while True:
    if keyboard.is_pressed("space"):
        while keyboard.is_pressed("space"):
            time.sleep(0.5)
        print("talk now. when you finish, press space again", end="\r")

        audio = record_from_microphone()

        print(end="\x1b[2K")
        print("processing audio...", end="\r")

        transcription = transcribe_audio(audio=audio)

        print(end="\x1b[2K")
        print(transcription)
        
        save_results(input_audio=audio, transcription=transcription)

    if keyboard.is_pressed("q"):
        break