from datetime import date
from typing import Dict, Any

def get_astrology_info(dob: date, birth_time: str = None, place_of_birth: str = None) -> Dict[str, Any]:
    """
    Main astrology function that handles both Indian and international requests
    """
    try:
        # If place_of_birth contains Indian city names, use Indian astrology
        indian_cities = ["delhi", "mumbai", "chennai", "kolkata", "bangalore", 
                        "hyderabad", "pune", "ahmedabad", "jaipur", "lucknow",
                        "india", "indian"]
        
        if place_of_birth and any(city in place_of_birth.lower() for city in indian_cities):
            return get_simplified_indian_astrology(dob, birth_time, place_of_birth)
        else:
            return get_simplified_astrology(dob)
            
    except Exception as e:
        return {"error": f"Astrology calculation failed: {str(e)}"}

def get_simplified_indian_astrology(dob: date, birth_time: str = None, city: str = None) -> Dict[str, Any]:
    """
    Simplified Indian astrology without ephem dependency with detailed traits
    """
    month = dob.month
    day = dob.day
    year = dob.year
    
    # Sun sign calculation
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        sun_sign = "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        sun_sign = "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        sun_sign = "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        sun_sign = "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        sun_sign = "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        sun_sign = "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        sun_sign = "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        sun_sign = "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        sun_sign = "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        sun_sign = "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        sun_sign = "Aquarius"
    else:
        sun_sign = "Pisces"
    
    # Moon sign approximation
    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", 
             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    moon_sign_index = (month + day) % 12
    moon_sign = signs[moon_sign_index]
    
    # Mercury sign (usually near Sun but can be one sign before or after)
    sun_index = signs.index(sun_sign)
    mercury_offset = (day % 3) - 1  # -1, 0, or 1
    mercury_sign = signs[(sun_index + mercury_offset) % 12]
    
    # Venus sign (similar to Mercury logic)
    venus_offset = ((month + day) % 3) - 1
    venus_sign = signs[(sun_index + venus_offset) % 12]
    
    # Mars sign (moves slower, more variation)
    mars_offset = ((month * day) % 5) - 2  # -2 to +2
    mars_sign = signs[(sun_index + mars_offset) % 12]

    # Enhanced astrology data with detailed planet-specific traits
    astrology_data = {
        "Aries": {
            "house_focus": "Self, Leadership, Initiatives (1st House)",
            "element": "Fire",
            "modality": "Cardinal",
            "ruler": "Mars",
            "planet_traits": {
                "sun": "Pioneering spirit, courageous, enthusiastic, impulsive, competitive nature with strong leadership qualities",
                "moon": "Emotionally impulsive, quick to react, needs constant stimulation, independent in feelings",
                "mercury": "Direct communication, quick thinking, argumentative when challenged, innovative ideas",
                "venus": "Passionate in love, assertive in relationships, enjoys conquest and challenge",
                "mars": "Highly energetic, competitive, courageous, impulsive action-taker"
            }
        },
        "Taurus": {
            "house_focus": "Wealth, Values, Stability (2nd House)",
            "element": "Earth",
            "modality": "Fixed",
            "ruler": "Venus",
            "planet_traits": {
                "sun": "Reliable, patient, practical, sensual, stubborn, values security and comfort above all",
                "moon": "Emotionally stable, comfort-seeking, possessive in relationships, slow to change",
                "mercury": "Methodical thinking, practical communication, learns through experience",
                "venus": "Sensual, loyal, appreciates beauty and luxury, stable in relationships",
                "mars": "Persistent, determined, slow to anger but powerful when provoked"
            }
        },
        "Gemini": {
            "house_focus": "Communication, Learning, Travel (3rd House)",
            "element": "Air",
            "modality": "Mutable",
            "ruler": "Mercury",
            "planet_traits": {
                "sun": "Curious, adaptable, communicative, restless, intellectually versatile but scattered",
                "moon": "Emotionally changeable, needs mental stimulation, communicates feelings through words",
                "mercury": "Quick-witted, versatile mind, excellent communicator, loves learning",
                "venus": "Flirtatious, enjoys intellectual connection in relationships, needs variety",
                "mars": "Energetic in communication, quick to act mentally, physically restless"
            }
        },
        "Cancer": {
            "house_focus": "Home, Family, Emotions (4th House)",
            "element": "Water",
            "modality": "Cardinal",
            "ruler": "Moon",
            "planet_traits": {
                "sun": "Nurturing, protective, intuitive, moody, deeply connected to family and home",
                "moon": "Highly sensitive, intuitive, nurturing, moody, needs emotional security",
                "mercury": "Emotional thinking, good memory, cautious communication, imaginative",
                "venus": "Nurturing in love, seeks emotional security, protective of partners",
                "mars": "Defensive, protective actions, fights for family and home security"
            }
        },
        "Leo": {
            "house_focus": "Creativity, Romance, Self-Expression (5th House)",
            "element": "Fire",
            "modality": "Fixed",
            "ruler": "Sun",
            "planet_traits": {
                "sun": "Confident, creative, generous, proud, loves attention and recognition",
                "moon": "Dramatic emotions, proud, needs appreciation, generous with feelings",
                "mercury": "Expressive communication, creative thinking, authoritative speech",
                "venus": "Romantic, generous in love, enjoys drama and grand gestures",
                "mars": "Courageous, dramatic actions, loves challenges and showing off skills"
            }
        },
        "Virgo": {
            "house_focus": "Health, Service, Work (6th House)",
            "element": "Earth",
            "modality": "Mutable",
            "ruler": "Mercury",
            "planet_traits": {
                "sun": "Analytical, practical, helpful, critical, perfectionist with strong work ethic",
                "moon": "Emotionally analytical, service-oriented, needs order and routine",
                "mercury": "Detail-oriented, analytical mind, precise communication, practical thinking",
                "venus": "Practical in love, shows affection through service, selective in partnerships",
                "mars": "Efficient, hard-working, precise actions, critical of imperfections"
            }
        },
        "Libra": {
            "house_focus": "Relationships, Partnerships, Harmony (7th House)",
            "element": "Air",
            "modality": "Cardinal",
            "ruler": "Venus",
            "planet_traits": {
                "sun": "Diplomatic, charming, fair-minded, indecisive, seeks balance and harmony",
                "moon": "Emotionally balanced, seeks partnership, avoids conflict, pleasant demeanor",
                "mercury": "Diplomatic communication, sees all sides, indecisive but fair-minded",
                "venus": "Charming, romantic, seeks harmony in relationships, appreciates beauty",
                "mars": "Actions consider others, fights for justice, avoids direct confrontation"
            }
        },
        "Scorpio": {
            "house_focus": "Transformation, Power, Secrets (8th House)",
            "element": "Water",
            "modality": "Fixed",
            "ruler": "Pluto/Mars",
            "planet_traits": {
                "sun": "Intense, passionate, secretive, transformative, powerful presence",
                "moon": "Deep emotions, secretive feelings, intense attachments, transformative",
                "mercury": "Investigative mind, penetrating thoughts, secretive communication",
                "venus": "Intense in love, passionate, possessive, transformative relationships",
                "mars": "Powerful actions, determined, secretive motives, intense energy"
            }
        },
        "Sagittarius": {
            "house_focus": "Adventure, Philosophy, Expansion (9th House)",
            "element": "Fire",
            "modality": "Mutable",
            "ruler": "Jupiter",
            "planet_traits": {
                "sun": "Optimistic, adventurous, philosophical, freedom-loving, truth-seeking",
                "moon": "Emotionally optimistic, needs freedom, adventurous feelings, philosophical",
                "mercury": "Philosophical thinking, honest communication, big-picture focus",
                "venus": "Adventurous in love, optimistic, enjoys freedom in relationships",
                "mars": "Energetic explorer, optimistic actions, loves physical challenges"
            }
        },
        "Capricorn": {
            "house_focus": "Career, Ambition, Structure (10th House)",
            "element": "Earth",
            "modality": "Cardinal",
            "ruler": "Saturn",
            "planet_traits": {
                "sun": "Ambitious, disciplined, responsible, practical, achieves through hard work",
                "moon": "Emotionally controlled, ambitious feelings, responsible, needs achievement",
                "mercury": "Practical thinking, organized communication, strategic planning",
                "venus": "Serious in love, responsible partner, values stability and commitment",
                "mars": "Ambitious actions, disciplined energy, persistent, achieves goals methodically"
            }
        },
        "Aquarius": {
            "house_focus": "Innovation, Friends, Ideas (11th House)",
            "element": "Air",
            "modality": "Fixed",
            "ruler": "Uranus/Saturn",
            "planet_traits": {
                "sun": "Innovative, independent, humanitarian, unconventional, forward-thinking",
                "moon": "Emotionally detached, innovative feelings, needs freedom and friendship",
                "mercury": "Original thinking, innovative ideas, unconventional communication",
                "venus": "Unconventional in love, values friendship, detached but loyal",
                "mars": "Innovative actions, fights for causes, energetic in group activities"
            }
        },
        "Pisces": {
            "house_focus": "Spirituality, Compassion, Dreams (12th House)",
            "element": "Water",
            "modality": "Mutable",
            "ruler": "Neptune/Jupiter",
            "planet_traits": {
                "sun": "Compassionate, dreamy, artistic, spiritual, sensitive to surroundings",
                "moon": "Highly sensitive emotions, compassionate, dreamy, psychic intuition",
                "mercury": "Imaginative thinking, intuitive communication, creative ideas",
                "venus": "Romantic, compassionate in love, idealistic, self-sacrificing",
                "mars": "Compassionate actions, dreamy energy, fights for spiritual causes"
            }
        }
    }

    # Get traits for each planet based on their sign
    planet_traits = {}
    for planet, sign in [("sun", sun_sign), ("moon", moon_sign), 
                         ("mercury", mercury_sign), ("venus", venus_sign), 
                         ("mars", mars_sign)]:
        planet_traits[planet] = astrology_data[sign]["planet_traits"][planet]

    # Calculate aspect influences (simplified)
    def get_aspect_influence(planet1_sign: str, planet2_sign: str) -> str:
        signs_diff = abs(signs.index(planet1_sign) - signs.index(planet2_sign)) % 12
        if signs_diff == 0: return "Conjunction: Strong combined energy"
        elif signs_diff == 3 or signs_diff == 9: return "Square: Challenging but motivating"
        elif signs_diff == 4 or signs_diff == 8: return "Trine: Harmonious flow"
        elif signs_diff == 6: return "Opposition: Balancing tension"
        else: return "Sextile: Opportunities for growth"

    # Get important aspects
    aspects = {
        "sun_moon": get_aspect_influence(sun_sign, moon_sign),
        "mercury_venus": get_aspect_influence(mercury_sign, venus_sign),
        "mars_venus": get_aspect_influence(mars_sign, venus_sign)
    }

    # Element balance analysis
    elements_count = {
        "Fire": len([s for s in [sun_sign, moon_sign, mercury_sign, venus_sign, mars_sign] 
                    if astrology_data[s]["element"] == "Fire"]),
        "Earth": len([s for s in [sun_sign, moon_sign, mercury_sign, venus_sign, mars_sign] 
                     if astrology_data[s]["element"] == "Earth"]),
        "Air": len([s for s in [sun_sign, moon_sign, mercury_sign, venus_sign, mars_sign] 
                   if astrology_data[s]["element"] == "Air"]),
        "Water": len([s for s in [sun_sign, moon_sign, mercury_sign, venus_sign, mars_sign] 
                     if astrology_data[s]["element"] == "Water"])
    }

    dominant_element = max(elements_count, key=elements_count.get)

    return {
        "type": "Indian Astrology" if city else "Western Astrology",
        "planets": {
            "sun": sun_sign,
            "moon": moon_sign,
            "mercury": mercury_sign,
            "venus": venus_sign,
            "mars": mars_sign
        },
        "traits": planet_traits,
        "house_focus": astrology_data[moon_sign]["house_focus"],
        "element_balance": f"Dominant {dominant_element} energy",
        "element_distribution": elements_count,
        "aspects": aspects,
        "chart_details": {
            "dominant_element": dominant_element,
            "modality": astrology_data[sun_sign]["modality"],
            "ruling_planet": astrology_data[sun_sign]["ruler"]
        },
        "special_features": [
            "Moon Sign Focus", 
            "Five Planet Analysis",
            "Element Balance",
            "Aspect Influences",
            "Nakshatra Based" if city else "Tropical Zodiac"
        ]
    }

def get_simplified_astrology(dob: date) -> Dict[str, Any]:
    """
    Simplified western astrology calculation with enhanced traits
    """
    result = get_simplified_indian_astrology(dob)
    result["type"] = "Western Astrology"
    result["special_features"] = ["Sun Sign Focus", "Tropical Zodiac", "Five Planet Analysis", "Element Balance"]
    return result