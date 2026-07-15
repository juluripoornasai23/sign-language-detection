# AI-Powered Sign Language Detection using AI + Full Stack

## Project Overview

The **AI-Powered Sign Language Detection System** is a full-stack application designed to bridge communication gaps between the hearing/speech-impaired community and the general public. The system uses computer vision and deep learning to detect and interpret hand gestures (sign language) in real time, converting them into readable text and, eventually, speech.

This repository is being built incrementally across multiple versions. **Version 0 (this release)** establishes the foundational AI microservice and project documentation only — it does not yet include real-time detection, the frontend, or the backend. It exists to provide a clean, scalable starting point that future versions will build upon.

## Features Planned

The following features are planned for upcoming versions:

- 🖐️ **Real-time Sign Detection** — Live webcam-based hand gesture recognition using MediaPipe + TensorFlow
- 📝 **Sentence Formation** — Combine sequential detected signs into coherent sentences
- 🔊 **Text-to-Speech** — Convert recognized text into spoken audio output
- 🔐 **User Authentication** — Secure login/signup with session/token management
- 🕘 **History** — Store and review past detection sessions per user
- 📊 **Dashboard** — Visual analytics of usage, accuracy, and detection history
- 🌐 **Multiple Language Support** — Support for multiple sign languages and spoken/text output languages

## Tech Stack

| Layer                | Technology                          | Status in V0 |
|-----------------------|--------------------------------------|--------------|
| AI Service            | Python, Flask                       | ✅ Implemented |
| Computer Vision       | OpenCV, MediaPipe                   | 📦 Installed only (not used yet) |
| Machine Learning      | TensorFlow                          | 📦 Installed only (not used yet) |
| Frontend              | React.js                            | 🔜 Future version |
| Backend API           | Node.js + Express                   | 🔜 Future version |
| Database              | MongoDB                             | 🔜 Future version |
| Version Control       | Git / GitHub                        | ✅ In use |
| Deployment            | Gunicorn, Docker (planned)          | 🔜 Future version |

## Folder Structure

The structure below represents the **target folder layout for the complete project** once all versions are implemented. In Version 0, only the AI service root files exist (marked accordingly).

```
sign-language-detection/
│
├── ai-service/                  # Python Flask AI microservice
│   ├── app.py                   # ✅ V0 - Flask entry point
│   ├── requirements.txt         # ✅ V0 - Python dependencies
│   ├── .env.example             # ✅ V0 - Environment variable template
│   ├── models/                  # 🔜 Trained ML models (.h5 files)
│   ├── utils/                   # 🔜 Landmark extraction, preprocessing helpers
│   └── routes/                  # 🔜 Modular Flask blueprints
│
├── backend/                     # Node.js + Express REST API (future)
│   ├── src/
│   │   ├── controllers/
│   │   ├── models/               # MongoDB schemas
│   │   ├── routes/
│   │   └── middleware/
│   ├── package.json
│   └── .env.example
│
├── frontend/                    # React.js client application (future)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/             # API call helpers
│   │   └── App.jsx
│   └── package.json
│
├── docs/                         # Project documentation, diagrams
├── .gitignore
├── README.md                     # ✅ V0 - Project documentation
└── LICENSE
```

> **Note:** In this Version 0 release, `app.py`, `requirements.txt`, `.env.example`, and `README.md` are provided at the project root for simplicity. They will be relocated into `ai-service/` once the backend and frontend are introduced in later versions.

## Version Roadmap

### ✅ Version 0 — Project Starter (Current)
- Initialize Flask AI microservice
- Add health-check (`/`) and placeholder prediction (`/predict`) routes
- Set up dependency management (`requirements.txt`)
- Set up environment variable template (`.env.example`)
- Write complete project documentation (`README.md`)
- No real AI inference, frontend, or backend yet

### 🔜 Version 1 — Core AI Detection
- Integrate MediaPipe for hand landmark extraction
- Integrate OpenCV for webcam frame capture and preprocessing
- Train and load an initial TensorFlow model for static sign classification
- Implement real inference logic in `/predict`

### 🔜 Version 2 — Full Stack Integration
- Build Node.js + Express backend as an API gateway between frontend and AI service
- Connect MongoDB for user data and detection history
- Build React.js frontend with a live camera feed and detection UI
- Implement sentence formation from sequential predictions

### 🔜 Version 3 — Advanced Features & Deployment
- Add user authentication (JWT-based)
- Add text-to-speech conversion
- Add analytics dashboard and multi-language support
- Containerize services with Docker and set up CI/CD pipelines
- Deploy to cloud infrastructure

## Installation

Follow these steps to run the **Version 0 AI service** locally.

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/sign-language-detection.git
cd sign-language-detection
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure environment variables
```bash
cp .env.example .env
```
Then edit `.env` if needed (defaults will work for local development).

### 6. Run the application
```bash
python app.py
```

### Expected Output
```
 * Serving Flask app 'app.py'
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://0.0.0.0:5000
Press CTRL+C to quit
```

Visit `http://127.0.0.1:5000/` in your browser or API client to confirm the service is running.

## API Documentation

### `GET /`
Health-check endpoint to confirm the service is running.

**Example Response:**
```json
{
    "status": "success",
    "service": "AI Sign Language Detection Service",
    "message": "Service is up and running",
    "version": "0.1.0"
}
```

### `GET|POST /predict`
Placeholder prediction endpoint. Does not perform inference in Version 0.

**Example Response:**
```json
{
    "status": "success",
    "message": "Prediction endpoint is under development",
    "version": "0.1.0"
}
```

## Environment Variables

| Variable      | Description                                              | Default          |
|---------------|------------------------------------------------------------|-------------------|
| `FLASK_APP`   | Entry-point file Flask uses to run the app                | `app.py`          |
| `FLASK_ENV`   | Application environment (`development` or `production`)  | `development`     |
| `PORT`        | Port the Flask server listens on                          | `5000`            |
| `MODEL_PATH`  | Filesystem path to the trained ML model (used from V1)   | `models/model.h5` |

## Future Improvements

- 🐳 **Dockerize** the AI service, backend, and frontend for consistent environments
- ⚙️ **CI/CD pipelines** (GitHub Actions) for automated testing and deployment
- 🧠 **Model training pipeline** with a labeled sign language dataset and experiment tracking
- ☁️ **Cloud deployment** (AWS / GCP / Azure / Render) with autoscaling
- 🕶️ **Smart glasses integration** for wearable, hands-free sign translation
- 📱 **Mobile application** (React Native / Flutter) for on-the-go accessibility
- 🧪 Unit and integration test coverage across all services

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
