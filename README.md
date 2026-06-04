<div align="center">

# 🌾 SmartFarm

### AI-Powered Smart Farming Assistant

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.58-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.21-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.9-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Firebase](https://img.shields.io/badge/Firebase-Auth%20%26%20Hosting-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

**SmartFarm** is a full-stack agricultural intelligence platform that combines **Machine Learning**, **Deep Learning**, and **Real-Time Weather Data** to help farmers make data-driven decisions for optimal crop selection, disease management, fertilizer usage, and farming practices.

[🚀 Getting Started](#-getting-started) · [✨ Features](#-features) · [🏗️ Architecture](#️-system-architecture) · [📊 Datasets](#-datasets) · [🤝 Contributing](#-contributing)

</div>

---



## ✨ Features

| Feature | Description | Model |
|---------|-------------|-------|
| 🌾 **Crop Recommendation** | Predicts the optimal crop based on soil nutrients (N, P, K), temperature, humidity, pH, and rainfall | Random Forest Classifier |
| 🔬 **Plant Disease Detection** | Identifies 38 plant diseases across 14 crop species from leaf images | CNN (Keras/TensorFlow) |
| 🧪 **Fertilizer Recommendation** | Suggests the best fertilizer based on soil type, crop type, and nutrient levels | Random Forest Classifier |
| 🌤️ **Weather Forecast** | Real-time weather data integration for precision farming decisions | Weather API |
| 📖 **Smart Farming Guide** | Step-by-step cultivation guides, pest control, and harvest timing | Knowledge Base |
| 🔐 **User Authentication** | Firebase-based login/signup for personalized user experience | Firebase Auth |

---

## 🏗️ System Architecture

```
smartfarm/
├── smartfarm-web-app/          # 🌐 Frontend (HTML/CSS/JS)
│   ├── index.html              #    Landing page
│   ├── css/style.css           #    Design system (Inter font, CSS variables)
│   ├── js/
│   │   ├── main.js             #    Animations, scroll-reveal, menu
│   │   ├── firebaseConfig.js   #    Firebase initialization
│   │   └── auth.js             #    Authentication logic
│   ├── login.html              #    Login page
│   ├── signup.html             #    Registration page
│   ├── weather-forecast/       #    Weather module
│   ├── guide/                  #    Farming guide module
│   ├── explore/                #    Explore section
│   └── images/                 #    Media assets
│
├── CROP-RECOMMENDATION/        # 🌾 ML Service (Port 8501)
│   ├── webapp.py               #    Streamlit app
│   ├── Crop_recommendation.csv #    Training dataset (2,200 samples)
│   ├── RF.pkl                  #    Trained Random Forest model
│   ├── DecisionTree.pkl        #    Decision Tree model
│   ├── KNeighborsClassifier.pkl#    KNN model
│   ├── XGBoost.pkl             #    XGBoost model
│   └── Crop_reccom(final).ipynb#    Training notebook
│
├── PLANT-DISEASE-IDENTIFICATION/ # 🔬 DL Service (Port 8502)
│   ├── main.py                 #    Streamlit app
│   ├── trained_plant_disease_model.keras  # Trained CNN (~94MB)
│   ├── Train_plant_disease.ipynb#    Training notebook
│   ├── Test_plant_disease.ipynb #    Testing notebook
│   ├── test/                   #    33 test images
│   └── training_hist.json      #    Training metrics
│
├── FERTILIZER-RECOMMENDATION/  # 🧪 ML Service (Port 8503)
│   ├── fertilizer_app.py       #    Streamlit app
│   ├── fertilizer_data.csv     #    Training dataset
│   ├── fertilizer_model.pkl    #    Trained model
│   └── fertilizer_model_train.py #  Training script
│
├── Datasets/                   # 📊 Dataset documentation
│   ├── Fertilizer_recommendation.csv
│   └── README.md
│
├── DISEASE-GUIDE.md            # 📖 Disease encyclopedia (38 diseases)
└── SystemArchitecture.md       # 📐 Architecture diagram
```

---

## 🚀 Getting Started

### Prerequisites

- **Python** 3.10+
- **Node.js** 18+ (for serving the frontend)
- **Git**

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/smartfarm.git
cd smartfarm/smartfarm-main/smartfarm
```

### 2️⃣ Set Up Python Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate     # Linux/macOS
# .venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
# Core ML dependencies
pip install streamlit numpy pandas scikit-learn pillow

# Deep Learning (for Disease Detection)
pip install tensorflow
```

### 4️⃣ Launch All Services

Open **4 terminal windows** and run:

```bash
# Terminal 1 — Frontend (Port 3000)
npx -y serve smartfarm-web-app -l 3000

# Terminal 2 — Crop Recommendation (Port 8501)
cd CROP-RECOMMENDATION
streamlit run webapp.py --server.port 8501

# Terminal 3 — Plant Disease Detection (Port 8502)
cd PLANT-DISEASE-IDENTIFICATION
streamlit run main.py --server.port 8502

# Terminal 4 — Fertilizer Recommendation (Port 8503)
cd FERTILIZER-RECOMMENDATION
streamlit run fertilizer_app.py --server.port 8503
```

### 5️⃣ Open in Browser

| Service | URL |
|---------|-----|
| 🌐 **Main Website** | [http://localhost:3000](http://localhost:3000) |
| 🌾 **Crop Recommendation** | [http://localhost:8501](http://localhost:8501) |
| 🔬 **Disease Detection** | [http://localhost:8502](http://localhost:8502) |
| 🧪 **Fertilizer Guide** | [http://localhost:8503](http://localhost:8503) |

---

## 📊 Datasets

### Crop Recommendation Dataset
| Property | Details |
|----------|---------|
| **Samples** | 2,200 |
| **Features** | Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall |
| **Classes** | 22 crop types (rice, wheat, maize, chickpea, banana, mango, etc.) |
| **Target** | Crop label |

### Plant Disease Dataset
| Property | Details |
|----------|---------|
| **Training Images** | 70,295 |
| **Validation Images** | 17,572 |
| **Crops Covered** | 14 (Apple, Corn, Grape, Tomato, Potato, etc.) |
| **Disease Classes** | 38 (including healthy) |
| **Source** | [Kaggle — Plant Disease Classification](https://www.kaggle.com/code/vad13irt/plant-disease-classification) |

### Fertilizer Recommendation Dataset
| Property | Details |
|----------|---------|
| **Features** | N, P, K, Temperature, Humidity, Moisture, Soil Type, Crop Type |
| **Output** | Fertilizer name recommendation |
| **Soil Types** | Loamy, Clay, Sandy, Black, Red, Alluvial |
| **Crop Types** | Barley, Cotton, Maize, Paddy, Wheat, Sugarcane, etc. |

---

## 🧠 ML Models & Performance

### Crop Recommendation

| Model | Accuracy |
|-------|----------|
| **Random Forest** ⭐ | ~99.5% |
| Decision Tree | ~97.8% |
| K-Nearest Neighbors | ~97.2% |
| Naive Bayes | ~99.0% |
| XGBoost | ~99.3% |

> The **Random Forest** classifier with 20 estimators is used in production.

### Plant Disease Detection

| Property | Details |
|----------|---------|
| **Architecture** | Convolutional Neural Network (CNN) |
| **Framework** | TensorFlow / Keras |
| **Input Size** | 128 × 128 px |
| **Model Size** | ~94 MB (`.keras` format) |
| **Classes** | 38 |
| **Accuracy** | ~95% |

### Fertilizer Recommendation

| Property | Details |
|----------|---------|
| **Model** | Random Forest Classifier |
| **Encoding** | One-Hot (Soil Type + Crop Type) |
| **Input Features** | 6 numeric + categorical features |

---

## 🛠️ Tech Stack

<table>
  <tr>
    <th>Layer</th>
    <th>Technology</th>
  </tr>
  <tr>
    <td><strong>Frontend</strong></td>
    <td>HTML5, CSS3 (Custom Design System), Vanilla JavaScript, Font Awesome 6</td>
  </tr>
  <tr>
    <td><strong>ML Backend</strong></td>
    <td>Python, Streamlit, scikit-learn, TensorFlow/Keras, NumPy, Pandas</td>
  </tr>
  <tr>
    <td><strong>Authentication</strong></td>
    <td>Firebase Auth (Email/Password)</td>
  </tr>
  <tr>
    <td><strong>Hosting</strong></td>
    <td>Firebase Hosting (Frontend), Streamlit Cloud (ML Services)</td>
  </tr>
  <tr>
    <td><strong>Data</strong></td>
    <td>CSV datasets, Pickle serialized models, Keras H5/SavedModel</td>
  </tr>
  <tr>
    <td><strong>Design</strong></td>
    <td>Inter font, CSS Custom Properties, Scroll-reveal animations, Glassmorphism</td>
  </tr>
</table>

---

## 🌿 Supported Crops

<details>
<summary>Click to expand — <strong>22 Crop Types</strong> for Recommendation</summary>

| # | Crop | Emoji |
|---|------|-------|
| 1 | Rice | 🌾 |
| 2 | Maize | 🌽 |
| 3 | Chickpea | 🫘 |
| 4 | Kidney Beans | 🫘 |
| 5 | Pigeon Peas | 🫛 |
| 6 | Moth Beans | 🫘 |
| 7 | Mung Bean | 🫛 |
| 8 | Black Gram | 🫘 |
| 9 | Lentil | 🫘 |
| 10 | Pomegranate | 🍎 |
| 11 | Banana | 🍌 |
| 12 | Mango | 🥭 |
| 13 | Grapes | 🍇 |
| 14 | Watermelon | 🍉 |
| 15 | Muskmelon | 🍈 |
| 16 | Apple | 🍏 |
| 17 | Orange | 🍊 |
| 18 | Papaya | 🥭 |
| 19 | Coconut | 🥥 |
| 20 | Cotton | 🧶 |
| 21 | Jute | 🪢 |
| 22 | Coffee | ☕ |

</details>

<details>
<summary>Click to expand — <strong>38 Disease Classes</strong> for Detection</summary>

| # | Disease | Crop |
|---|---------|------|
| 1 | Apple Scab | Apple |
| 2 | Black Rot | Apple |
| 3 | Cedar Apple Rust | Apple |
| 4 | Healthy | Apple |
| 5 | Healthy | Blueberry |
| 6 | Powdery Mildew | Cherry |
| 7 | Healthy | Cherry |
| 8 | Gray Leaf Spot | Corn |
| 9 | Common Rust | Corn |
| 10 | Northern Leaf Blight | Corn |
| 11 | Healthy | Corn |
| 12 | Black Rot | Grape |
| 13 | Esca (Black Measles) | Grape |
| 14 | Leaf Blight | Grape |
| 15 | Healthy | Grape |
| 16 | Huanglongbing (Citrus Greening) | Orange |
| 17 | Bacterial Spot | Peach |
| 18 | Healthy | Peach |
| 19 | Bacterial Spot | Bell Pepper |
| 20 | Healthy | Bell Pepper |
| 21 | Early Blight | Potato |
| 22 | Late Blight | Potato |
| 23 | Healthy | Potato |
| 24 | Healthy | Raspberry |
| 25 | Healthy | Soybean |
| 26 | Powdery Mildew | Squash |
| 27 | Leaf Scorch | Strawberry |
| 28 | Healthy | Strawberry |
| 29 | Bacterial Spot | Tomato |
| 30 | Early Blight | Tomato |
| 31 | Late Blight | Tomato |
| 32 | Leaf Mold | Tomato |
| 33 | Septoria Leaf Spot | Tomato |
| 34 | Spider Mites | Tomato |
| 35 | Target Spot | Tomato |
| 36 | Yellow Leaf Curl Virus | Tomato |
| 37 | Mosaic Virus | Tomato |
| 38 | Healthy | Tomato |

</details>

---

## 📁 Key Files Reference

| File | Purpose |
|------|---------|
| `smartfarm-web-app/index.html` | Main landing page |
| `smartfarm-web-app/css/style.css` | Complete design system |
| `smartfarm-web-app/js/main.js` | Animations & interactivity |
| `CROP-RECOMMENDATION/webapp.py` | Crop recommendation Streamlit app |
| `CROP-RECOMMENDATION/RF.pkl` | Production Random Forest model |
| `PLANT-DISEASE-IDENTIFICATION/main.py` | Disease detection Streamlit app |
| `PLANT-DISEASE-IDENTIFICATION/trained_plant_disease_model.keras` | Trained CNN model |
| `FERTILIZER-RECOMMENDATION/fertilizer_app.py` | Fertilizer recommendation app |
| `DISEASE-GUIDE.md` | Comprehensive disease encyclopedia |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Commit** your changes: `git commit -m "Add my feature"`
4. **Push** to the branch: `git push origin feature/my-feature`
5. **Open** a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.


