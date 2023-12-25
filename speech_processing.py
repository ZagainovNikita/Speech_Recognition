from pvrecorder import PvRecorder
import keyboard
import wave
import struct


def record_from_microphone(save=False):
    recorder = PvRecorder(device_index=0, frame_length=512)
    audio = []

    recorder.start()

    while not keyboard.is_pressed("space"):
        frame = recorder.read()
        audio.extend(frame)

    recorder.stop()
    recorder.delete()
    
    if save:
        with wave.open("audio.wav", 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))
    return audio
