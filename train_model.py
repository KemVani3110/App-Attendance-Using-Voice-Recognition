import os
import numpy as np
import librosa
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
from collections import Counter
from sklearn.preprocessing import LabelEncoder

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=60)
    return np.mean(mfccs.T, axis=0)

def load_data(data_path='voice_samples'):
    X, y = [], []
    for user_name in os.listdir(data_path):
        user_path = os.path.join(data_path, user_name)
        if os.path.isdir(user_path):
            for file_name in os.listdir(user_path):
                file_path = os.path.join(user_path, file_name)
                try:
                    features = extract_features(file_path)
                    X.append(features)
                    y.append(user_name)
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")
    return np.array(X), np.array(y)

def check_data_balance(y):
    counter = Counter(y)
    print("Data balance check:")
    for user, count in counter.items():
        print(f"User: {user}, Count: {count}")
    return all(count > 5 for count in counter.values())

def train_model(X, y):
    if len(X) < 2:
        raise ValueError("Need at least two samples to train the model.")
    if not check_data_balance(y):
        raise ValueError("Each user needs at least 5 samples for training.")

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    test_size = 0.5 if len(X) < 10 else 0.2
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=test_size, random_state=42)

    print("Training data shape:", X_train.shape)
    print("Test data shape:", X_test.shape)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model accuracy: {accuracy * 100:.2f}%")

    return model, le

if __name__ == "__main__":    
    X, y = load_data()
    try:
        model, le = train_model(X, y)
        with open('voice_recognition_model.pkl', 'wb') as f:
            pickle.dump({'model': model, 'label_encoder': le}, f)
        print("Model saved to voice_recognition_model.pkl")
    except ValueError as e:
        print(e)
        print("Please add more voice samples and try again.")

