from flask import Flask, request, jsonify
from flask_cors import CORS
from YouExpCalculations import LifeExperienceCalculator
from AstroProfileInfo import LifePathCalculator
from PlanetWiseInfo_ModalityPolarity_Elements import AstrologicalCalculator
from Dict import astro_data
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Initialize calculators
life_exp_calculator = LifeExperienceCalculator
life_path_calculator = LifePathCalculator()
astro_calculator = AstrologicalCalculator(astro_data)

def format_life_experience_data(life_exp_data):
    """Format life experience numbers with commas"""
    formatted = {}
    for key, value in life_exp_data.items():
        formatted[key] = f"{value:,}"
    return formatted

@app.route('/api/calculate/formatted', methods=['POST'])
def calculate_complete_profile():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['date', 'time', 'latitude', 'longitude']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "error": f"Missing required field: {field}"
                }), 400
        
        birth_data = {
            "date": data['date'],
            "time": data['time'],
            "latitude": float(data['latitude']),
            "longitude": float(data['longitude'])
        }

        # Calculate Life Experience
        life_exp_calc = life_exp_calculator(birth_data['date'], birth_data['time'])
        life_exp_raw = life_exp_calc.get_all_calculations()
        life_experience = format_life_experience_data(life_exp_raw)
        
        # Calculate Life Path
        life_path = life_path_calculator.get_life_path_info(birth_data['date'])
        
        # Calculate Astrological Data
        astro_data = astro_calculator.get_astrological_data(
            birth_data['date'],
            birth_data['time'],
            birth_data['latitude'],
            birth_data['longitude']
        )
        
        # Combine all data into the exact structure you want
        result = {
            "life_experience": life_experience,
            "life_path": {
                "number": life_path['number'],
                "title": life_path['title'],
                "description": life_path['description'],
                "strengths": life_path['strengths'],
                "challenges": life_path['challenges'],
                "career_paths": life_path['career_paths']
            },
            "elements": astro_data['elements'],
            "modalities": astro_data['modalities'],
            "polarities": astro_data['polarities'],
            "planet_info": astro_data['planet_info']
        }
        
        return jsonify({
            "success": True,
            "data": result
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Astrological API is running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)