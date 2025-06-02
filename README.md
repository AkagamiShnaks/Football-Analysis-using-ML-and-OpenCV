# ⚽ Football Analysis Project

This is a computer vision–based football analysis application that detects and tracks players, the ball, and referees from match videos. It estimates player speed, maps ball possession, and generates tactical field insights using Python, OpenCV, and YOLOv5.

---

## 📦 Features

- Real-time player, referee, and ball detection (YOLOv5)
- Player speed estimation
- Ball tracking & possession analysis
- Referee differentiation
- Team classification via jersey color clustering
- Tactical zone mapping using pitch keypoints
- Visualized output with overlays
- Compatible with any standard match footage

---

## ⚙️ Environment Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/football_analysis.git
cd football_analysis
```

### Step 2: Create and activate a virtual environment (optional but recommended)

```bash
# For virtualenv
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Project Workflow

### 📘 Phase 1: Prepare Input

Add your football match video to the `input_videos/` directory.

---

### 🎯 Phase 2: Run the Analysis

Execute the main script to process the video:

```bash
python main.py
```

---

### 📊 Phase 3: View Output

The annotated video and stats will be saved in:

```bash
output_videos/
```

You can also explore player speed, possession data, and positional maps from the output.

---

## 🎥 Demo

![Football Analysis Demo](assets/ezgif-8327c2b8846f86.gif)

---

## 📌 Requirements

- Python 3.7+
- All required packages in `requirements.txt`

Install with:

```bash
pip install -r requirements.txt
```

---

## 👤 Author

**Ayon Sen**  
[GitHub](https://github.com/AkagamiShnaks)  
[LinkedIn](https://linkedin.com/in/yourprofile)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🛡️ Badges

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![YOLOv5](https://img.shields.io/badge/YOLOv5-Object--Detection-red)
![OpenCV](https://img.shields.io/badge/OpenCV-Tracking-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)
