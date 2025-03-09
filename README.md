# Tetris OpenCV Hand Controller

This project allows you to play **Tetris** using hand gestures! 🗨  
It utilizes **OpenCV, MediaPipe**, and **Python** to track hand movements and map them to in-game controls.

## **Play Tetris Here**
You can play the game at: [Tetris Official Website](https://tetris.com/play-tetris)  

## **Controls - Hand Gestures Mapping**
The following hand movements control the Tetris game:  

### **Right Hand (Piece Movement & Rotation)**
| **Gesture**  | **Action** |
|-------------|------------|
| **Index Finger Points Down** (Below wrist & base of fingers) | Soft Drop |
| **Index Finger Raised (Up)** | Rotate Right |
| **Thumbs Up (Index Forward, Thumb Raised)** | Rotate Left |
| **Swipe Right (Index Moves Right)** | Move Right |
| **Swipe Left (Index Moves Left)** | Move Left |

### **Left Hand (Piece Control)**
| **Gesture**  | **Action** |
|-------------|------------|
| **All Fingers Down (Fist Gesture)** | Hold Piece |
| **All Fingers Fully Extended** | Hard Drop |

---

## **⚙️ Setup Instructions**
Follow these steps to install and run the project:

### **1⃣ Create & Activate a Conda Environment**
```bash
conda create --name tetris-hand python=3.10 -y
conda activate tetris-hand
```
> **Make sure your Python interpreter is set to the newly created environment in your IDE.**

### **2⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3⃣ Run the Game Controller**
Make sure you have a **webcam** connected, then start the hand tracking:
```bash
python main.py
```
> You will have to manually open the tetris game and click start to start playing

---

