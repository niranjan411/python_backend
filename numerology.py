from datetime import date

def sum_digits(n: int) -> int:
    """
    Reduce number to single digit through digit sum
    """
    while n > 9 and n not in [11, 22, 33]:  # Master numbers
        n = sum(int(d) for d in str(n))
    return n

def get_life_path(dob: date) -> int:
    """
    Calculate Life Path Number (most important number in numerology)
    """
    day = dob.day
    month = dob.month
    year = dob.year
    
    # Reduce day, month, year to single digits
    day_number = sum_digits(day)
    month_number = sum_digits(month)
    year_number = sum_digits(year)
    
    # Sum and reduce to single digit or master number
    life_path = sum_digits(day_number + month_number + year_number)
    
    return life_path

def get_life_path_meaning(life_path: int) -> dict:
    """
    Get detailed meaning of life path number
    """
    meanings = {
        1: {
            "title": "The Leader",
            "traits": "Independent, ambitious, determined, innovative, courageous",
            "challenges": "Arrogance, impatience, dominance, selfishness",
            "career": "Entrepreneur, manager, inventor, pioneer"
        },
        2: {
            "title": "The Peacemaker", 
            "traits": "Cooperative, diplomatic, intuitive, patient, supportive",
            "challenges": "Oversensitivity, indecisiveness, shyness, dependency",
            "career": "Mediator, counselor, artist, team player"
        },
        3: {
            "title": "The Creative",
            "traits": "Expressive, imaginative, joyful, inspirational, communicative",
            "challenges": "Scattered energy, superficiality, exaggeration, moodiness",
            "career": "Writer, performer, artist, communicator"
        },
        4: {
            "title": "The Builder",
            "traits": "Practical, disciplined, reliable, organized, hardworking",
            "challenges": "Rigidity, stubbornness, narrow-mindedness, too serious",
            "career": "Engineer, architect, organizer, technician"
        },
        5: {
            "title": "The Freedom Seeker",
            "traits": "Adventurous, versatile, progressive, curious, adaptable",
            "challenges": "Restlessness, irresponsibility, inconsistency, impulsiveness",
            "career": "Explorer, salesperson, journalist, adventurer"
        },
        6: {
            "title": "The Nurturer",
            "traits": "Responsible, caring, compassionate, protective, idealistic",
            "challenges": "Worrying, meddling, self-righteousness, perfectionism",
            "career": "Teacher, healer, counselor, parent"
        },
        7: {
            "title": "The Seeker",
            "traits": "Analytical, spiritual, intuitive, philosophical, perceptive",
            "challenges": "Skepticism, isolation, secretiveness, cynicism",
            "career": "Researcher, philosopher, detective, spiritual guide"
        },
        8: {
            "title": "The Powerhouse",
            "traits": "Ambitious, authoritative, efficient, organized, successful",
            "challenges": "Materialism, workaholism, intolerance, power-hungry",
            "career": "Executive, banker, manager, leader"
        },
        9: {
            "title": "The Humanitarian",
            "traits": "Compassionate, generous, creative, tolerant, idealistic",
            "challenges": "Emotional, scattered, possessive, dreamy",
            "career": "Philanthropist, artist, healer, global worker"
        },
        11: {
            "title": "The Intuitive Master",
            "traits": "Inspirational, intuitive, idealistic, visionary, sensitive",
            "challenges": "Nervous energy, impracticality, perfectionism",
            "career": "Visionary, spiritual teacher, artist, counselor"
        },
        22: {
            "title": "The Master Builder", 
            "traits": "Practical visionary, powerful, disciplined, ambitious, idealistic",
            "challenges": "Pressure, extreme expectations, workaholism",
            "career": "Global leader, master architect, large-scale planner"
        },
        33: {
            "title": "The Master Teacher",
            "traits": "Inspirational, compassionate, healing, nurturing, enlightened",
            "challenges": "Pressure to be perfect, carrying others' burdens",
            "career": "Master teacher, spiritual leader, global healer"
        }
    }
    
    return meanings.get(life_path, {
        "title": "Unknown Number",
        "traits": "Traits not available",
        "challenges": "Challenges not available", 
        "career": "Career paths not available"
    })

def get_destiny_number(full_name: str) -> int:
    """
    Calculate Destiny Number from full name (not implemented in main app)
    """
    # Numerology chart: A=1, B=2, ..., I=9, J=1, etc.
    numerology_chart = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
    }
    
    total = 0
    for char in full_name.upper():
        if char in numerology_chart:
            total += numerology_chart[char]
    
    return sum_digits(total)