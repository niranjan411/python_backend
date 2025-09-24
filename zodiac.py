from datetime import date

def get_zodiac_sign(dob: date) -> str:
    """
    Calculate Western zodiac sign based on date of birth
    """
    month = dob.month
    day = dob.day
    
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries ♈"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus ♉"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini ♊"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer ♋"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo ♌"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo ♍"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra ♎"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio ♏"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius ♐"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn ♑"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius ♒"
    else:
        return "Pisces ♓"

def get_zodiac_element(sign: str) -> str:
    """
    Get the element associated with a zodiac sign
    """
    elements = {
        "Aries": "Fire", "Leo": "Fire", "Sagittarius": "Fire",
        "Taurus": "Earth", "Virgo": "Earth", "Capricorn": "Earth",
        "Gemini": "Air", "Libra": "Air", "Aquarius": "Air",
        "Cancer": "Water", "Scorpio": "Water", "Pisces": "Water"
    }
    
    # Remove emoji for matching
    clean_sign = sign.split(' ')[0]
    return elements.get(clean_sign, "Unknown")

def get_zodiac_modality(sign: str) -> str:
    """
    Get the modality (cardinal, fixed, mutable) of a zodiac sign
    """
    modalities = {
        "Aries": "Cardinal", "Cancer": "Cardinal", "Libra": "Cardinal", "Capricorn": "Cardinal",
        "Taurus": "Fixed", "Leo": "Fixed", "Scorpio": "Fixed", "Aquarius": "Fixed",
        "Gemini": "Mutable", "Virgo": "Mutable", "Sagittarius": "Mutable", "Pisces": "Mutable"
    }
    
    clean_sign = sign.split(' ')[0]
    return modalities.get(clean_sign, "Unknown")

def get_zodiac_traits(sign: str) -> str:
    """
    Get key personality traits for a zodiac sign
    """
    traits = {
        "Aries": "Courageous, determined, confident, enthusiastic, optimistic, honest, passionate",
        "Taurus": "Reliable, patient, practical, devoted, responsible, stable, sensual",
        "Gemini": "Gentle, affectionate, curious, adaptable, ability to learn quickly and exchange ideas",
        "Cancer": "Tenacious, highly imaginative, loyal, emotional, sympathetic, persuasive",
        "Leo": "Creative, passionate, generous, warm-hearted, cheerful, humorous",
        "Virgo": "Loyal, analytical, kind, hardworking, practical, helpful",
        "Libra": "Cooperative, diplomatic, gracious, fair-minded, social, idealistic",
        "Scorpio": "Resourceful, brave, passionate, stubborn, a true friend, intelligent",
        "Sagittarius": "Generous, idealistic, great sense of humor, adventurous, open-minded",
        "Capricorn": "Responsible, disciplined, self-control, good managers, determined",
        "Aquarius": "Progressive, original, independent, humanitarian, inventive",
        "Pisces": "Compassionate, artistic, intuitive, gentle, wise, musical"
    }
    
    clean_sign = sign.split(' ')[0]
    return traits.get(clean_sign, "Traits not available")