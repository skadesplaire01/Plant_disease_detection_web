from flask import Flask, render_template, request
import joblib
from PIL import Image
import numpy as np
import json

app = Flask(__name__)

# Load model and class names
model = joblib.load('rf_model.pkl')
with open('class_names.json', 'r') as f:
    class_names = json.load(f)

# Disease info dictionary
disease_info = {
    "Pepperbell_healthy": {
        "status": "Healthy",
        "description": "The plant is healthy and shows no signs of disease."
    },
    "Pepperbell_bacteriaspot": {
        "status": "Diseased",
        "description": "Bacterial spot causes dark, water-soaked lesions on leaves and fruits."
    },
    "Potato_healthy": {
        "status": "Healthy",
        "description": "The plant is healthy and shows no signs of disease."
    },
    "Potato_earlybight": {
        "status": "Diseased",
        "description": "Early blight causes dark spots on leaves and may reduce yield."
    },
    "Tomato_mosaic_virus": {
        "status": "Diseased",
        "description": "Tomato mosaic virus causes leaf mottling and reduced growth."
    },
    "Tomato_healthy": {
        "status": "Healthy",
        "description": "The plant is healthy and shows no signs of disease."
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', result="No file uploaded")
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', result="No file selected")
        
        # Process image
        img = Image.open(file).convert('RGB').resize((64,64))
        img_array = np.array(img).flatten().reshape(1, -1)
        pred_class = class_names[model.predict(img_array)[0]]
        
        # Get disease info
        info = disease_info.get(pred_class, {"status": "Unknown", "description": "No info available."})
        result = {
            "class": pred_class,
            "status": info['status'],
            "description": info['description']
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
