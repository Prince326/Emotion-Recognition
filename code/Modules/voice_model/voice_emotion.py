import librosa
import joblib
import soundfile
import os, glob, pickle
import numpy as np
import soundfile as soundfile


import warnings
warnings.filterwarnings("ignore")



#Extract features values like (mfcc, chroma, mel) from a single sound file



#DataFlair - Extract features (mfcc, chroma, mel) from a sound file
def extract_feature(file_name):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate

        stft=np.abs(librosa.stft(X))
        result=np.array([])

        mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        result=np.hstack((result, mfccs))

        chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
        result=np.hstack((result, chroma))

        #mel=np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T,axis=0)
        mel = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate, n_fft=2048).T, axis=0)

        result=np.hstack((result, mel))

    return result



neutral = ['calm', 'neutral', 'surprised']
negative = ['angry','fearful','disgust','sad']

def three_emotion(emotion):
    if neutral.count(emotion)==1: #we return neutral if we find any emotion in the neutral list
        return 'neutral'
    elif negative.count(emotion) == 1:  # same but for negative list
        return 'negative'
    else:
        return 'positive' #we return positive as it is only left

def voice_emotion_pred():

    vc_model = joblib.load("C:/Users/princ/PycharmProjects/EmoReg/Modules/voice_model/voice_model.sav")
    path = "C:/Users/princ/PycharmProjects/EmoReg/Modules/voice_model/recorded_audio.wav"

    data = []
    data.append(extract_feature(path))


    emo = vc_model.predict(data)
    emo = three_emotion(emo)


    return emo

#print('Voice Emotion: ' + voice_emotion_pred())