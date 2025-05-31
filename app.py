from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Laat verzoeken toe van andere origins (zoals GitHub Pages)

# Interpretatie functie
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

# Originele route voor gebruik met render_template (lokale testing of fallback)
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		weight = float(request.form['weight'])
		height = float(request.form['height'])
		bmi = round(weight / (height ** 2), 2)
		interpretation = get_bmi_interpretation(bmi)
		return render_template('result.html', bmi=bmi, interpretation=interpretation)
	return render_template('index.html')

# Extra API-route voor GitHub Pages of andere frontends
@app.route('/api/calculate', methods=['POST'])
def api_calculate_bmi():
	data = request.get_json()
	weight = float(data['weight'])
	height = float(data['height'])
	bmi = round(weight / (height ** 2), 2)
	interpretation = get_bmi_interpretation(bmi)
	return jsonify({'bmi': bmi, 'interpretation': interpretation})

# Run de app
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
