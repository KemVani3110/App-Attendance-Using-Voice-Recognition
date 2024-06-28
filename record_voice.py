import sounddevice as sd
import scipy.io.wavfile as wav
import os

def record_voice(folder_path, file_name, duration=5, sample_rate=44100):
    print("Recording...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()  # Wait until recording is finished
    file_path = os.path.join(folder_path, file_name + ".wav")
    wav.write(file_path, sample_rate, recording)
    print(f"Recording saved to {file_path}")

if __name__ == "__main__":
    user_name = input("Enter the user name: ")
    folder_path = os.path.join("voice_samples", user_name)
    os.makedirs(folder_path, exist_ok=True)

    while True:
        file_name = input("Enter the file name: ")
        record_voice(folder_path, file_name)

        another = input("Do you want to record another sample? (y/n): ").strip().lower()
        if another != 'y':
            break
