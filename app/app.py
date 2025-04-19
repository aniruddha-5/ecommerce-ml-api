from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

# Load the trained model
model = joblib.load('model.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        # Extract input values
        features = [
            data['num_views'],
            data['num_cart_adds'],
            data['unique_categories']
        ]

        input_array = np.array(features).reshape(1, -1)

        prediction = model.predict(input_array)[0]

        return jsonify({'prediction': int(prediction)})

    except KeyError:
        return jsonify({'error': 'Invalid input'}), 400

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


import os

