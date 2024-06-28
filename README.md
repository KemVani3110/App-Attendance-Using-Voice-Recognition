## App Attendance Using Voice Recognition

This project is ran on Visual Studio Code only.

## Overview

This project leverages voice recognition technology to manage attendance, developed using Python 3.12.2.

## Installation

To get started, install the necessary libraries by running the following commands:

    pip install numpy
    pip install sounddevice
    pip install librosa
    pip install scikit-learn
    pip install tkinter
    pip install scipy
    pip install pandas openpyxl
    
## Usage

To use the app, follow these steps:

1. Record voice samples:

    To record voice samples for the attendance system, run:

    `python record_voice.py`
    
    This script will help you record voice samples for the attendance system.

    You can record as many samples as you need—the more, the better for the accuracy of the model.

2. Train the model:
    Next, train the voice recognition model with the recorded samples by executing:

    `python train_model.py`
    
    This script will train the voice recognition model using the dataset provided.

3. Recognize voice:
    Finally, use the app to recognize voices and mark attendance by running:

    `python recognize_voice.py`
    
    This script will recognize the voice and mark the attendance.

## Preparing Training Data
To ensure optimal performance of the voice recognition system, follow these steps to prepare your training data:

1. Record at least 40 sound samples:

    Begin by recording a minimum of 40 distinct sound samples using the record_file.py script. These samples will form the core dataset required for offline testing.

2. Generate additional sound samples:

    Create more than 10 additional sound recordings. Place these extra samples in your initial_audio_files_yourname directory.

3. Organize your data for testing:

    The initial 40 sound files will be designated for Option 1: Offline Testing.
    The additional sound files will be allocated for Option 2: Online Testing.

By carefully preparing and organizing your audio samples, you will ensure a robust training dataset that enhances the accuracy and reliability of the voice recognition model.

## Conclusion

This voice recognition attendance app offers a convenient and innovative way to track attendance. By recording, training, and recognizing voices, you can efficiently manage attendance records with minimal hassle.