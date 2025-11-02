class LifePathCalculator:
    def __init__(self):
        self.life_path_info = {
            1: {
                "number": 1,
                "title": "The Leader",
                "keywords": ["independence", "leadership", "innovation", "individuality"],
                "description": "You are a natural-born leader with strong individuality and creative energy. You excel at initiating projects and inspiring others.",
                "strengths": ["Independent", "Creative", "Ambitious", "Determined"],
                "challenges": ["Can be domineering", "Impatient", "Stubborn"],
                "career_paths": ["Entrepreneur", "Manager", "Inventor", "Pioneer"]
            },
            2: {
                "number": 2,
                "title": "The Diplomat",
                "keywords": ["cooperation", "sensitivity", "harmony", "partnership"],
                "description": "You are a peacemaker who thrives in partnerships and collaborative environments. Your intuition and empathy guide your decisions.",
                "strengths": ["Cooperative", "Intuitive", "Patient", "Supportive"],
                "challenges": ["Overly sensitive", "Indecisive", "Shy"],
                "career_paths": ["Mediator", "Counselor", "Teacher", "Team Player"]
            },
            3: {
                "number": 3,
                "title": "The Communicator",
                "keywords": ["creativity", "expression", "joy", "social"],
                "description": "You are blessed with creative talents and excellent communication skills. You bring joy and inspiration to others.",
                "strengths": ["Creative", "Expressive", "Optimistic", "Social"],
                "challenges": ["Scattered energy", "Superficial", "Exaggerative"],
                "career_paths": ["Writer", "Artist", "Performer", "Communicator"]
            },
            4: {
                "number": 4,
                "title": "The Builder",
                "keywords": ["stability", "practicality", "organization", "hard work"],
                "description": "You are the foundation of any project or relationship. Your practical approach and strong work ethic ensure lasting results.",
                "strengths": ["Reliable", "Practical", "Disciplined", "Organized"],
                "challenges": ["Rigid", "Stubborn", "Too conventional"],
                "career_paths": ["Engineer", "Architect", "Accountant", "Manager"]
            },
            5: {
                "number": 5,
                "title": "The Freedom Lover",
                "keywords": ["freedom", "adventure", "change", "versatility"],
                "description": "You thrive on change, adventure, and new experiences. Your adaptability and curiosity make you a natural explorer.",
                "strengths": ["Adaptable", "Adventurous", "Progressive", "Multitalented"],
                "challenges": ["Restless", "Impulsive", "Inconsistent"],
                "career_paths": ["Sales", "Travel", "Media", "Entrepreneur"]
            },
            6: {
                "number": 6,
                "title": "The Nurturer",
                "keywords": ["responsibility", "nurturing", "harmony", "service"],
                "description": "You are the caregiver and problem-solver who creates harmony in relationships and communities.",
                "strengths": ["Responsible", "Nurturing", "Compassionate", "Reliable"],
                "challenges": ["Worry too much", "Meddling", "Self-righteous"],
                "career_paths": ["Teacher", "Healer", "Counselor", "Parent"]
            },
            7: {
                "number": 7,
                "title": "The Seeker",
                "keywords": ["analysis", "wisdom", "intuition", "spirituality"],
                "description": "You are a deep thinker and spiritual seeker who values knowledge and inner wisdom above material possessions.",
                "strengths": ["Analytical", "Intuitive", "Spiritual", "Wise"],
                "challenges": ["Pessimistic", "Secretive", "Isolated"],
                "career_paths": ["Researcher", "Scientist", "Philosopher", "Mystic"]
            },
            8: {
                "number": 8,
                "title": "The Powerhouse",
                "keywords": ["ambition", "authority", "success", "abundance"],
                "description": "You have a natural talent for business and leadership, with the ability to manifest abundance and success.",
                "strengths": ["Ambitious", "Authoritative", "Efficient", "Successful"],
                "challenges": ["Workaholic", "Materialistic", "Intimidating"],
                "career_paths": ["Executive", "Banker", "Entrepreneur", "Leader"]
            },
            9: {
                "number": 9,
                "title": "The Humanitarian",
                "keywords": ["compassion", "universal love", "service", "completion"],
                "description": "You are here to serve humanity with your compassion, wisdom, and universal perspective.",
                "strengths": ["Compassionate", "Generous", "Humanitarian", "Artistic"],
                "challenges": ["Emotionally vulnerable", "Self-sacrificing", "Dreamy"],
                "career_paths": ["Healer", "Artist", "Philanthropist", "Teacher"]
            },
            11: {
                "number": 11,
                "title": "The Intuitive Illuminator",
                "keywords": ["intuition", "inspiration", "idealism", "enlightenment"],
                "description": "You are a highly intuitive and inspirational being with a special mission to bring light and enlightenment to others.",
                "strengths": ["Intuitive", "Inspirational", "Idealistic", "Visionary"],
                "challenges": ["Nervous energy", "Overly sensitive", "Unrealistic"],
                "career_paths": ["Visionary", "Spiritual Teacher", "Artist", "Healer"]
            },
            22: {
                "number": 22,
                "title": "The Master Builder",
                "keywords": ["practical dreams", "large-scale projects", "mastery", "manifestation"],
                "description": "You have the unique ability to turn dreams into reality on a large scale, combining vision with practical implementation.",
                "strengths": ["Practical visionary", "Master builder", "Ambitious", "Grounded"],
                "challenges": ["Overwhelmed by potential", "Workaholic", "Impatient"],
                "career_paths": ["Global Entrepreneur", "Architect", "World Leader", "Innovator"]
            },
            33: {
                "number": 33,
                "title": "The Master Teacher",
                "keywords": ["healing", "compassion", "service", "enlightenment"],
                "description": "You are here to uplift humanity through unconditional love, healing, and spiritual teaching.",
                "strengths": ["Healing", "Compassionate", "Inspirational", "Service-oriented"],
                "challenges": ["Self-sacrificing", "Overwhelmed", "Perfectionist"],
                "career_paths": ["Spiritual Leader", "Healer", "Teacher", "Counselor"]
            }
        }
    
    def calculate_life_path(self, birth_date):
        """Calculate life path number from birth date (YYYY-MM-DD)"""
        # Remove dashes and convert to string
        date_str = birth_date.replace("-", "")
        
        total = 0
        for char in date_str:
            total += int(char)
        
        # Reduce to single digit or master number
        while total > 9 and total not in [11, 22, 33]:
            total = sum(int(digit) for digit in str(total))
        
        return total
    
    def get_life_path_info(self, birth_date):
        life_path_number = self.calculate_life_path(birth_date)
        return self.life_path_info.get(life_path_number, {"error": "Life path number not found"})

# Example usage
if __name__ == "__main__":
    calculator = LifePathCalculator()
    life_path = calculator.calculate_life_path("1999-06-20")
    info = calculator.get_life_path_info("1999-06-20")
    print(f"Life Path Number: {life_path}")
    print(f"Title: {info['title']}")
    print(f"Description: {info['description']}")