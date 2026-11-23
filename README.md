# FCIS - CSys - Digital Signal Processing [DSP] - Traditional DSP-Based Audio Event Detection [AED]

- **University:** Ain Shams University
- **Faculty:** FCIS - Faculty of Computer and Information Systems
- **Department:** CSys - Computer Systems
- **Course:** Digital Signal Processing [DSP]
- **Academic Year:** 2028 - First Term
- **Project Name:** Traditional DSP-Based Audio Event Detection [AED]
- **Project Details:** [You can find idea details in this document - Idea Number #5](Documentations/ideas.pdf)
- **Course Instructor:** Dr. Mirvat Al-Qutt

## Setup

- **Prerequisites:** Python 3.9+
- **Installation and Usage:** Open Powershell and Follow these steps

```text
git clone https://github.com/ahmedtaha808/FCIS_AudioEventDetection.git
cd AudioEventDetection
pip install -r requirements.txt
python main.py
```


## The Idea

Imagine a smart room that can listen to its surroundings and recognize important sound
events without using cameras or machine learning.

This project implements an **Audio Event Detection (AED)** GUI system using classical Digital Signal Processing techniques rather than deep learning models.

The system analyzes audio recordings and identifies events such as glass breaking, door knocking, footsteps, door slamming, and smoke alarms by extracting signal characteristics using **Time-Domain Analysis**, **Frequency-Domain Analysis**, and **Temporal Pattern Analysis** techniques.

## Dataset

- **Dataset Sources:**
  - [Kaggle - AASP](https://www.kaggle.com/competitions/sound-event-classification/data)
  - [Github - ESC-50](https://github.com/karolpiczak/ESC-50)
  - [freesound.org](https://freesound.org/)
- **For training:** a collection of labeled audio recordings(.wav files) containing the following events:
  - Glass breaking
  - Door knocking
  - Footsteps
  - Door slamming
  - Smoke alarm
- **For testing:** Unseen recordings
- Dataset Structure:

```text
Dataset/
├── Train/
│   ├── DoorKnicking/
│   ├── DoorSlaming/
│   ├── Footsteps/
│   ├── GlassBreaking/
│   └── SmokeAlarm/
└── Test/
    ├── DoorKnicking/
    ├── DoorSlaming/
    ├── Footsteps/
    ├── GlassBreaking/
    └── SmokeAlarm/
```

## Input and Output Data

- **Input:** An unknown audio recording.
- **Output:** For each test recording, your system should display:
  - The detected sound event.
  - A confidence or similarity score.
  - The processing time.
- For Example The system should return something like:

```text
Recording: unknown_001.wav

Detected Event: Glass Breaking
Similarity Score: 91%
Processing Time: 0.35 seconds
```

## Implementation Requirements

- The system must rely entirely on Digital Signal Processing (DSP) techniques.
- No machine learning or deep learning.
- No pre-trained models or external sound-classification systems.
- No ready-made audio feature extraction or classification libraries.
- Basic audio file loading and playback libraries are allowed.
- Your system should not simply memorize the supplied recordings.
- **Time-Domain Analysis:** Investigate signal characteristics that describe how the audio
signal behaves over time.
- **Frequency-Domain Analysis:** Investigate the frequency content of different sound
events and identify characteristics that can help distinguish them.
- **Temporal Pattern Analysis:** Investigate how sound events evolve and repeat over
time, including their duration, repetition, and timing patterns.
- **Feature Extraction:** Implement your own DSP-based feature extraction techniques
using the three analysis dimensions above.
- **Sound Recognition:** Design your own recognition and decision-making method to
identify the sound category. You must not use trained classifiers or machine learning.
- **Noise Robustness:** Investigate how background noise affects recognition and improve
your system to handle noisy recordings.
- **Testing:** Your system must recognize recordings that were not used during the initial
system design.
- **From-Scratch Implementation:** Implement the essential signal-processing and
recognition operations yourself.

## Evaluation Criteria

- Recognition accuracy across all sound categories.
- Ability to distinguish between similar sound events.
- Robustness to background noise.
- Performance on previously unseen recordings.
- Quality and correctness of the DSP implementation.
- Processing speed and computational efficiency.

## DSP Features Extraction Methods



