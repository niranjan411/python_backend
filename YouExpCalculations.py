from datetime import datetime, date

class LifeExperienceCalculator:
    def __init__(self, birth_date, birth_time):
        self.birth_date = birth_date
        self.birth_time = birth_time
        self.birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
        self.now = datetime.now()
        
    def calculate_age_in_seconds(self):
        age_delta = self.now - self.birth_datetime
        return int(age_delta.total_seconds())
    
    def calculate_heart_beats(self):
        # Average heart rate: 72 beats per minute
        seconds = self.calculate_age_in_seconds()
        beats_per_second = 72 / 60
        return int(seconds * beats_per_second)
    
    def calculate_breaths(self):
        # Average breathing rate: 16 breaths per minute
        seconds = self.calculate_age_in_seconds()
        breaths_per_second = 16 / 60
        return int(seconds * breaths_per_second)
    
    def calculate_blinks(self):
        # Average blinking: 15 blinks per minute
        seconds = self.calculate_age_in_seconds()
        blinks_per_second = 15 / 60
        return int(seconds * blinks_per_second)
    
    def calculate_milliseconds(self):
        age_delta = self.now - self.birth_datetime
        return int(age_delta.total_seconds() * 1000)
    
    def calculate_hours(self):
        age_delta = self.now - self.birth_datetime
        return int(age_delta.total_seconds() / 3600)
    
    def calculate_sunsets(self):
        # Approximate sunsets (one per day)
        age_days = (self.now.date() - self.birth_datetime.date()).days
        return age_days
    
    def calculate_days(self):
        return (self.now.date() - self.birth_datetime.date()).days
    
    def calculate_weeks(self):
        days = self.calculate_days()
        return days // 7
    
    def calculate_months(self):
        today = self.now.date()
        birth = self.birth_datetime.date()
        return (today.year - birth.year) * 12 + today.month - birth.month
    
    def calculate_seasons(self):
        months = self.calculate_months()
        return months // 3
    
    def calculate_leap_years(self):
        birth_year = self.birth_datetime.year
        current_year = self.now.year
        leap_years = 0
        
        for year in range(birth_year, current_year + 1):
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                leap_years += 1
        return leap_years
    
    def get_all_calculations(self):
        return {
            "heart_beats": self.calculate_heart_beats(),
            "breaths": self.calculate_breaths(),
            "blinks": self.calculate_blinks(),
            "milliseconds": self.calculate_milliseconds(),
            "seconds": self.calculate_age_in_seconds(),
            "hours": self.calculate_hours(),
            "sunsets": self.calculate_sunsets(),
            "days": self.calculate_days(),
            "weeks": self.calculate_weeks(),
            "months": self.calculate_months(),
            "seasons": self.calculate_seasons(),
            "leap_years": self.calculate_leap_years()
        }

# Example usage
if __name__ == "__main__":
    calculator = LifeExperienceCalculator("1999-06-20", "15:30")
    results = calculator.get_all_calculations()
    print("Life Experience Calculations:")
    for key, value in results.items():
        print(f"{key}: {value:,}")