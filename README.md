## App Attendance Using Voice Recognition

## Overview

This project leverages voice recognition technology to manage attendance, developed using Python 3.12.2.

## Installation

To get started, install the necessary libraries by running the following commands:

    `pip install numpy`
    `pip install sounddevice`
    `pip install librosa`
    `pip install scikit-learn`
    `pip install tkinter`
    `pip install scipy`
    `pip install pandas openpyxl`
    
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

## Conclusion

This voice recognition attendance app offers a convenient and innovative way to track attendance. By recording, training, and recognizing voices, you can efficiently manage attendance records with minimal hassle.