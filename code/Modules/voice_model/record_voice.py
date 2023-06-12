import os
import pyaudio
import wave

def record_audio(filename=None, duration=5):
    chunk = 1024  # Number of frames per buffer
    format = pyaudio.paInt16  # Sample size and format
    channels = 1  # Mono audio
    rate = 44100  # Sample rate (samples/second)

    p = pyaudio.PyAudio()

    # Open audio stream
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording started...")
    frames = []

    # Record audio data
    for i in range(int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded audio as a WAV file
    if not filename:
        default_filename = "recorded_audio.wav"
        default_path = os.path.join(os.getcwd(), default_filename)
        filename = default_path

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

#print(record_audio())