# ⚽ Football Analysis using Machine Learning and OpenCV

This project presents an intelligent football match analysis system that uses Machine Learning and OpenCV to automatically detect, track, and analyze players, referees, and the ball from match footage. The system generates real-time statistics, visual insights, and tactical analytics from standard broadcast videos.

## 🎥 Demo

![Football Analysis Demo](assets/ezgif-8327c2b8846f86.gif)

*Example: Real-time player detection, ball tracking, and speed estimation on a football pitch.*

## 📌 Key Features

- 🧍 **Player & Referee Detection**: Detects and distinguishes players, referees, and the ball using YOLOv5.
- 🏃 **Player Tracking & Speed Estimation**: Tracks players across frames and estimates their speed using positional data.
- ⚽ **Ball Position Tracking**: Continuously identifies and maps ball position throughout the match.
- 🟨 **Referee Differentiation**: Uses model class labels or color-based filtering to distinguish referees from players.
- 🧠 **Team Classification**: Assigns players to clubs by analyzing jersey color with clustering.
- 📍 **Pitch Keypoints & Mapping**: Detects key field markings to enable accurate homography and 2D pitch mapping.
- 🗺️ **Zone-Based Analysis**: Identifies player positions within key pitch zones for tactical analysis.
- 🔄 **Voronoi Diagrams**: Generates spatial control zones for each player.
- 📊 **Statistical Outputs**: Provides data on possession, movement heatmaps, and zone occupancy.

## 🚀 How to Run

1. Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/your-username/football_analysis.git
cd football_analysis

-------

2.Install Requirements.txt


```bash
pip install -r requirements.txt

------

3. Place your input video in the `input_videos/` directory.
4. Run the main script:

```bash
python main.py
