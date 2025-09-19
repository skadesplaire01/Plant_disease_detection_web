# Plant_disease_detection_web
# 🌱 LeafSense – AI-Powered Plant Disease Detection

A machine learning–based web application that detects **plant diseases** from leaf images and provides **disease details & treatment suggestions**.  
Built with **Random Forest Classifier** and **Flask**, achieving **85% accuracy**.

---

## 📌 Features
- 🌿 Upload a plant leaf image and get instant diagnosis  
- ✅ Detects if the plant is **Healthy** or **Diseased**  
- 💡 Provides **disease description** and **treatment suggestions**  
- 🎨 User-friendly interface with color-coded results  
- 🔥 Achieved **85% accuracy** using Random Forest  

---

## 🛠 Tech Stack
- **Programming & ML:** Python, Scikit-learn, NumPy, PIL (Pillow), Joblib  
- **Web Framework:** Flask  
- **Frontend:** HTML5, CSS3 (Jinja2 templates)  
- **Tools:** VS Code, Git  

---

## 📂 Project Structure
plant_disease_detection/
│── app.py # Flask backend
│── rf_model.pkl # Trained Random Forest model
│── class_names.json # Class labels
│── dataset/ # Dataset (images of leaves)
│── templates/
│ └── index.html # Frontend template


---

## 🚀 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/plant-disease-detection.git
   cd plant-disease-detection
   
2. **Create virtual environment & install dependencies**
    ```bash
       python -m venv venv
       source venv/bin/activate   # For Linux/Mac
       venv\Scripts\activate      # For Windows
        pip install -r requirements.txt
    
3.**Run the Flask app**
python app.py

4. **Open in browser → http://127.0.0.1:5000/**





