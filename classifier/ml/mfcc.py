import librosa
import numpy as np

def get_mfcc(y,sr):
    y = librosa.resample(y, sr, 8000);
    y = y[0:40000];
    y = np.concatenate((y, [0]* (40000 - y.shape[0])), axis=0);
    # Mel-frequency cepstral coefficients 
    mfcc=librosa.feature.mfcc(y=y, sr=sr, n_mfcc=10,hop_length=4000);
    mfcc_feature=np.reshape(mfcc, (1,110))
    return mfcc_feature