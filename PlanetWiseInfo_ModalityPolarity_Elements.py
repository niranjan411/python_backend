import swisseph as swe
from datetime import datetime

class AstrologicalCalculator:
    def __init__(self, dict_data):
        self.dict_data = dict_data
        self.elements = {
            "Fire": ["Aries", "Leo", "Sagittarius"],
            "Earth": ["Taurus", "Virgo", "Capricorn"],
            "Air": ["Gemini", "Libra", "Aquarius"],
            "Water": ["Cancer", "Scorpio", "Pisces"]
        }
        
        self.modalities = {
            "Cardinal": ["Aries", "Cancer", "Libra", "Capricorn"],
            "Fixed": ["Taurus", "Leo", "Scorpio", "Aquarius"],
            "Mutable": ["Gemini", "Virgo", "Sagittarius", "Pisces"]
        }
        
        self.polarities = {
            "Yang": ["Aries", "Gemini", "Leo", "Libra", "Sagittarius", "Aquarius"],
            "Yin": ["Taurus", "Cancer", "Virgo", "Scorpio", "Capricorn", "Pisces"]
        }

    def get_zodiac_sign(self, degree):
        signs = [
            "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
        ]
        return signs[int(degree // 30)]

    def get_planet_signs(self, date, time, latitude, longitude):
        datetime_str = f"{date} {time}"
        dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

        jd = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute/60, swe.GREG_CAL)
        swe.set_topo(latitude, longitude, 0)

        planets = {
            "Sun": swe.SUN,
            "Moon": swe.MOON,
            "Mercury": swe.MERCURY,
            "Venus": swe.VENUS,
            "Mars": swe.MARS,
            "Jupiter": swe.JUPITER,
            "Saturn": swe.SATURN,
            "Uranus": swe.URANUS,
            "Neptune": swe.NEPTUNE,
            "Pluto": swe.PLUTO,
        }

        result = {}
        for name, code in planets.items():
            pos, _ = swe.calc(jd, code)
            result[name] = self.get_zodiac_sign(pos[0])

        return result

    def calculate_elements_distribution(self, planet_signs):
        element_count = {"Fire": 0, "Earth": 0, "Air": 0, "Water": 0}
        
        for planet, sign in planet_signs.items():
            for element, signs in self.elements.items():
                if sign in signs:
                    element_count[element] += 1
                    break
        
        total_planets = len(planet_signs)
        element_percentages = {}
        for element, count in element_count.items():
            element_percentages[element] = int((count / total_planets) * 100) if total_planets > 0 else 0
        
        return element_percentages

    def calculate_modality_distribution(self, planet_signs):
        modality_count = {"Cardinal": 0, "Fixed": 0, "Mutable": 0}
        
        for planet, sign in planet_signs.items():
            for modality, signs in self.modalities.items():
                if sign in signs:
                    modality_count[modality] += 1
                    break
        
        total_planets = len(planet_signs)
        modality_percentages = {}
        for modality, count in modality_count.items():
            modality_percentages[modality] = int((count / total_planets) * 100) if total_planets > 0 else 0
        
        return modality_percentages

    def calculate_polarity_distribution(self, planet_signs):
        polarity_count = {"Yang": 0, "Yin": 0}
        
        for planet, sign in planet_signs.items():
            for polarity, signs in self.polarities.items():
                if sign in signs:
                    polarity_count[polarity] += 1
                    break
        
        total_planets = len(planet_signs)
        polarity_percentages = {}
        for polarity, count in polarity_count.items():
            polarity_percentages[polarity] = int((count / total_planets) * 100) if total_planets > 0 else 0
        
        return polarity_percentages

    def get_planet_wise_info(self, planet_signs):
        planet_info = []
        
        for planet, sign in planet_signs.items():
            planet_data_key = f"{planet.lower()}_data"
            if planet_data_key in self.dict_data and sign in self.dict_data[planet_data_key]:
                # Get the planet data from Dict.py
                planet_data = self.dict_data[planet_data_key][sign]
                
                # Format the data for the frontend as a list of objects
                planet_info.append({
                    "planet": planet,
                    "sign": sign,
                    "element": planet_data["element"],
                    "modality": planet_data["mode"],  # Note: using "mode" from your data
                    "polarity": planet_data["polarity"],
                    "description": planet_data["meaning"],
                    "keywords": planet_data["keywords"].split(", ")
                })
            else:
                # Fallback information if specific data not found
                planet_info.append({
                    "planet": planet,
                    "sign": sign,
                    "element": next((elem for elem, signs in self.elements.items() if sign in signs), "Unknown"),
                    "modality": next((mod for mod, signs in self.modalities.items() if sign in signs), "Unknown"),
                    "polarity": next((pol for pol, signs in self.polarities.items() if sign in signs), "Unknown"),
                    "description": f"{planet} in {sign} brings its unique influence to this placement. This planetary position affects your personality and life path in distinctive ways.",
                    "keywords": ["unique", "influence", "placement"]
                })
        
        return planet_info

    def get_astrological_data(self, date, time, latitude, longitude):
        planet_signs = self.get_planet_signs(date, time, latitude, longitude)
        
        return {
            "planet_info": self.get_planet_wise_info(planet_signs),
            "elements": self.calculate_elements_distribution(planet_signs),
            "modalities": self.calculate_modality_distribution(planet_signs),
            "polarities": self.calculate_polarity_distribution(planet_signs)
        }