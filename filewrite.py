import struct
import wave
import os


def save_results(input_audio, transcription):
    if not os.path.exists("./output/"):
        os.makedirs("./output/")
    
    new_folder = str(len(os.listdir("./output/")) + 1)
    new_folder_path = os.path.join("output", new_folder)
    os.makedirs(new_folder_path)

    sound_path = os.path.join(new_folder_path, "input_audio.wav")
    transcription_path = os.path.join(new_folder_path, "transcription")

    with wave.open(sound_path, "w") as f:
        f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        f.writeframes(struct.pack("h" * len(input_audio), *input_audio))

    with open(transcription_path, "w") as f:
        f.write(transcription)