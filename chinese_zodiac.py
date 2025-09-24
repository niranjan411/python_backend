from datetime import date

def get_chinese_zodiac(year: int) -> str:
    """
    Calculate Chinese zodiac animal based on birth year
    """
    zodiac_animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", 
                     "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    
    # Chinese zodiac cycle starts from 1900 (Rat year)
    return zodiac_animals[(year - 1900) % 12]

def get_chinese_zodiac_emoji(animal: str) -> str:
    """
    Get emoji for Chinese zodiac animal
    """
    emojis = {
        "Rat": "🐀",
        "Ox": "🐂", 
        "Tiger": "🐅",
        "Rabbit": "🐇",
        "Dragon": "🐉",
        "Snake": "🐍",
        "Horse": "🐎",
        "Goat": "🐐",
        "Monkey": "🐒",
        "Rooster": "🐓",
        "Dog": "🐕",
        "Pig": "🐖"
    }
    return emojis.get(animal, "🐾")

def get_chinese_zodiac_element(year: int) -> str:
    """
    Calculate Chinese zodiac element based on birth year
    """
    elements = ["Metal", "Water", "Wood", "Fire", "Earth"]
    # Elements cycle every 2 years
    element_index = ((year - 1900) // 2) % 5
    return elements[element_index]

def get_chinese_zodiac_traits(animal: str) -> dict:
    """
    Get detailed traits for Chinese zodiac animal
    """
    traits = {
        "Rat": {
            "personality": "Quick-witted, resourceful, versatile, kind",
            "strengths": "Charming, intelligent, adaptable, leadership qualities",
            "weaknesses": "Manipulative, greedy, selfish, controlling",
            "compatibility": ["Dragon", "Monkey", "Ox"],
            "lucky_numbers": [2, 3],
            "lucky_colors": ["Blue", "Gold", "Green"]
        },
        "Ox": {
            "personality": "Diligent, dependable, strong, determined",
            "strengths": "Patient, reliable, honest, hardworking",
            "weaknesses": "Stubborn, dogmatic, hot-tempered, narrow-minded",
            "compatibility": ["Snake", "Rooster", "Rat"],
            "lucky_numbers": [1, 4],
            "lucky_colors": ["White", "Yellow", "Green"]
        },
        "Tiger": {
            "personality": "Brave, confident, competitive, unpredictable",
            "strengths": "Courageous, passionate, generous, charismatic",
            "weaknesses": "Aggressive, reckless, impatient, short-tempered",
            "compatibility": ["Horse", "Dog", "Pig"],
            "lucky_numbers": [1, 3, 4],
            "lucky_colors": ["Blue", "Grey", "Orange"]
        },
        "Rabbit": {
            "personality": "Quiet, elegant, kind, responsible",
            "strengths": "Gentle, compassionate, artistic, diplomatic",
            "weaknesses": "Timid, conservative, overly cautious, moody",
            "compatibility": ["Goat", "Pig", "Dog"],
            "lucky_numbers": [3, 4, 6],
            "lucky_colors": ["Red", "Pink", "Purple"]
        },
        "Dragon": {
            "personality": "Confident, intelligent, enthusiastic, lucky",
            "strengths": "Ambitious, energetic, charismatic, innovative",
            "weaknesses": "Arrogant, impatient, stubborn, demanding",
            "compatibility": ["Rat", "Monkey", "Rooster"],
            "lucky_numbers": [1, 6, 7],
            "lucky_colors": ["Gold", "Silver", "Gray"]
        },
        "Snake": {
            "personality": "Enigmatic, intelligent, wise, philosophical",
            "strengths": "Intuitive, graceful, mysterious, determined",
            "weaknesses": "Jealous, suspicious, manipulative, lazy",
            "compatibility": ["Ox", "Rooster", "Monkey"],
            "lucky_numbers": [2, 8, 9],
            "lucky_colors": ["Black", "Red", "Yellow"]
        },
        "Horse": {
            "personality": "Active, energetic, independent, free-spirited",
            "strengths": "Adventurous, cheerful, popular, perceptive",
            "weaknesses": "Impatient, reckless, stubborn, egoistic",
            "compatibility": ["Tiger", "Dog", "Goat"],
            "lucky_numbers": [2, 3, 7],
            "lucky_colors": ["Yellow", "Green", "Blue"]
        },
        "Goat": {
            "personality": "Calm, gentle, sympathetic, creative",
            "strengths": "Kind, artistic, peaceful, compassionate",
            "weaknesses": "Worrying, pessimistic, sensitive, dependent",
            "compatibility": ["Rabbit", "Horse", "Pig"],
            "lucky_numbers": [2, 7, 9],
            "lucky_colors": ["Green", "Red", "Purple"]
        },
        "Monkey": {
            "personality": "Sharp, smart, curious, inventive",
            "strengths": "Intelligent, witty, innovative, problem-solver",
            "weaknesses": "Arrogant, mischievous, impatient, manipulative",
            "compatibility": ["Rat", "Dragon", "Snake"],
            "lucky_numbers": [4, 5, 9],
            "lucky_colors": ["White", "Blue", "Gold"]
        },
        "Rooster": {
            "personality": "Observant, hardworking, courageous, talented",
            "strengths": "Honest, punctual, organized, confident",
            "weaknesses": "Critical, vain, opinionated, boastful",
            "compatibility": ["Ox", "Snake", "Dragon"],
            "lucky_numbers": [5, 7, 8],
            "lucky_colors": ["Gold", "Brown", "Yellow"]
        },
        "Dog": {
            "personality": "Loyal, honest, amiable, cautious",
            "strengths": "Faithful, responsible, caring, protective",
            "weaknesses": "Anxious, stubborn, cynical, pessimistic",
            "compatibility": ["Tiger", "Horse", "Rabbit"],
            "lucky_numbers": [3, 4, 9],
            "lucky_colors": ["Red", "Green", "Purple"]
        },
        "Pig": {
            "personality": "Compassionate, generous, diligent, sincere",
            "strengths": "Honest, reliable, caring, optimistic",
            "weaknesses": "Naive, gullible, materialistic, stubborn",
            "compatibility": ["Rabbit", "Goat", "Tiger"],
            "lucky_numbers": [2, 5, 8],
            "lucky_colors": ["Yellow", "Gray", "Brown"]
        }
    }
    
    return traits.get(animal, {
        "personality": "Traits not available",
        "strengths": "Strengths not available",
        "weaknesses": "Weaknesses not available",
        "compatibility": [],
        "lucky_numbers": [],
        "lucky_colors": []
    })

def get_chinese_zodiac_year_forecast(animal: str, current_year: int) -> str:
    """
    Get general forecast for the current year (simplified)
    """
    forecasts = {
        "Rat": "A year of opportunities and new beginnings",
        "Ox": "A stable year with steady progress",
        "Tiger": "An adventurous year with exciting changes",
        "Rabbit": "A peaceful year with harmonious relationships",
        "Dragon": "A lucky year with success and recognition",
        "Snake": "A transformative year with deep insights",
        "Horse": "An energetic year with travel and movement",
        "Goat": "A creative year with artistic inspiration",
        "Monkey": "A clever year with problem-solving opportunities",
        "Rooster": "An organized year with career advancement",
        "Dog": "A loyal year with strong relationships",
        "Pig": "A prosperous year with abundance and joy"
    }
    
    return forecasts.get(animal, "General forecast not available")