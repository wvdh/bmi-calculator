from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Allow CORS requests from your GitHub Pages domain only
CORS(app, resources={r"/api/*": {"origins": "https://wvdh.github.io"}})

# Function to interpret BMI value
def get_bmi_interpretation(bmi):
    if bmi <= 18.4:
        return 'You are underweight.'
    elif bmi <= 24.9:
        return 'Your weight is normal.'
    elif bmi <= 29.9:
        return 'You are slightly overweight.'
    elif bmi <= 34.9:
        return 'You are severely overweight.'
    elif bmi <= 39.9:
        return 'You are obese.'
    else:
        return 'You are severely obese.'

# API route for frontend apps (GitHub Pages)
@app.route('/api/calculate', methods=['POST'])
def api_calculate_bmi():
    data = request.get_json()
    weight = float(data['weight'])
    height = float(data['height'])
    bmi = round(weight / (height ** 2), 2)
    interpretation = get_bmi_interpretation(bmi)
    return jsonify({'bmi': bmi, 'interpretation': interpretation})

# Start the app (used by Render or local dev)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)