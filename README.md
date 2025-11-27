# 🤖 Python OpenCV MyCobot Hand Tracking Control

This project uses **Python**, **OpenCV**, and **MediaPipe** to track hand movements in real time and control the **MyCobot** robotic arm.  
By detecting wrist position, the program converts hand movement into robot joint angles — enabling simple and intuitive **gesture-based robot control**.

---

## 🚀 Features

- Real-time hand tracking using Google MediaPipe
- OpenCV-based webcam video capture and display
- Wrist coordinates mapped to robot joint angles
- MyCobot robot updates its base/shoulder angle instantly
- Smooth and responsive motion control
- Easy to customize and expand

---

## 🎥 Demo Screenshot

<img width="476" height="444" alt="Hand Tracking Screenshot" src="https://github.com/user-attachments/assets/c128ba32-dad2-4ed7-a943-12e704dd6455" />

---

## 🧩 How It Works

The project works in three main steps:

                +----------------------+
                |   Webcam Captures    |
                |     Live Video       |
                +-----------+----------+
                            |
                            v
                +----------------------+
                |  MediaPipe Detects   |
                |   Hand Landmarks     |
                +-----------+----------+
                            |
                            v
                +----------------------+
                | Convert Wrist (x,y)  |
                |   → Robot Angles     |
                +-----------+----------+
                            |
                            v
                +----------------------+
                |   MyCobot Moves      |
                | According to Gesture |
                +----------------------+

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV**
- **MediaPipe**
- **MyCobot API (pymycobot)**

---

## 📦 Requirements

Install required libraries using:

```bash
pip install -r requirements.txt

