# AR Application using ArUco Markers

An Augmented Reality (AR) application built with Python and OpenCV that detects ArUco markers in real-time via webcam and overlays virtual images or videos onto them using homography and computer vision techniques.

---

## 📸 Demo

### Image Augmentation
![Image AR Demo](demo/screenshots/ar_image_demo.png)

### Video Augmentation
![Video AR Demo](demo/screenshots/ar_video_demo.png)

---

## 🚀 Features

- Real-time ArUco marker detection using webcam
- Overlay custom **images** onto detected markers (Version 1)
- Overlay **video frames** onto detected markers (Version 2)
- Supports multiple markers simultaneously (IDs 0–3)
- Perspective-correct image warping using homography

---

## 🗂️ Project Structure

```
AR-Application-using-ArUco-Markers/
│
├── src/
│   ├── image_augmentation.py      # Version 1 – overlays images on markers
│   └── video_augmentation.py      # Version 2 – overlays video on markers
│
├── markers/
│   ├── marker_0.jpg               # ArUco marker ID 0 (print & use)
│   ├── marker_1.jpg               # ArUco marker ID 1
│   ├── marker_2.jpg               # ArUco marker ID 2
│   └── marker_3.jpg               # ArUco marker ID 3
│
├── images/
│   └── augmentation/
│       ├── 00.jpg                 # Augmentation image for marker 0
│       ├── 01.jpg                 # Augmentation image for marker 1
│       ├── 02.jpg                 # Augmentation image for marker 2
│       └── 03.jpg                 # Augmentation image for marker 3
│
├── demo/
│   ├── screenshots/
│   │   ├── ar_image_demo.png
│   │   └── ar_video_demo.png
│   └── videos/
│       ├── SCREEN_RECORDED.mp4    # Demo – image augmentation
│       └── VIDEO__EX_.mp4         # Demo – video augmentation
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

- Python 3.10
- PyCharm (recommended IDE)

### Module Versions

| Module | Version |
|--------|---------|
| opencv-contrib-python | 4.9.0.80 |
| numpy | 1.26.4 |

---

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-org>/AR-Application-using-ArUco-Markers.git
   cd AR-Application-using-ArUco-Markers
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### Version 1 — Image Augmentation

Overlays images onto ArUco markers detected by your webcam.

```bash
python src/image_augmentation.py
```

- Place your augmentation images inside `images/augmentation/`
- Name them `00.jpg`, `01.jpg`, etc. (matching marker IDs)
- Print the markers from the `markers/` folder
- Point your webcam at a marker — the corresponding image appears on it!
- Press `Q` to quit

### Version 2 — Video Augmentation

Overlays video frames onto a detected ArUco marker.

```bash
python src/video_augmentation.py
```

- Update the video path inside `video_augmentation.py` before running
- Point your webcam at a marker — the video plays on top of it!
- Press `Q` to quit

---

## 🖨️ Printing Markers

Print the marker images from the `markers/` folder on paper. Hold them in front of your webcam — the app will detect them and overlay the corresponding image or video in real time.

---

## 📋 Notes

- Make sure your webcam is connected and accessible
- Use good lighting for better marker detection
- Uses `DICT_4X4_50` dictionary for image augmentation and `DICT_6X6_250` for video augmentation

---

## 🛠️ Built With

- [OpenCV](https://opencv.org/) — Computer vision & ArUco detection
- [NumPy](https://numpy.org/) — Matrix operations & homography
- Python 3.10

---

## 👩‍💻 Author

**Tanuja Devi. M** 

---

## 📄 License

This project was developed as an academic assignment. All rights reserved.
