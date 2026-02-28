import tensorflow as tf
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import os

app = Flask(__name__)
CORS(app)

# Load the model (ensure skin_cancer_model.h5 is in the same folder)
model = tf.keras.models.load_model('skin_cancer_model.h5')
class_names = ['benign', 'malignant']

@app.route('/')
def home():
    return "Skin Cancer Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    try:
        file = request.files['file'].read()
        image = Image.open(io.BytesIO(file)).convert('RGB')

        # Matches the size your model expects
        image = image.resize((256, 256)) 
        img_array = tf.keras.preprocessing.image.img_to_array(image)
        img_array = np.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = float(np.max(tf.nn.softmax(predictions[0])))

        return jsonify({
            'prediction': predicted_class,
            'confidence': f"{confidence * 100:.2f}%"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Important for deployment: use the PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)