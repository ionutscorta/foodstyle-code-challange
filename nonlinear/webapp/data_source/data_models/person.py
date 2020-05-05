class Person:
    def __init__(self, name, age, work_sector,
                 status_marriage, career, relationship, sex, gained_capital, lost_capital,
                 education=None, education_num=None, race=None, hours_per_week=None, country=None):
        self.name = name
        self.age = age
        self.work_sector = work_sector
        self.education = education if education is not None else "HS-grad"
        self.education_num = education_num if education_num is not None else 9
        self.status_marriage = status_marriage
        self.career = career
        self.relationship = relationship
        self.race = race if race is not None else "Other"
        self.sex = sex
        self.gained_capital = gained_capital
        self.lost_capital = lost_capital
        self.hours_per_week = hours_per_week if hours_per_week is not None else 40
        self.country = country if country is not None else "United-States"


