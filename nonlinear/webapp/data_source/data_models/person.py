mandatory_fields = ['name', 'age', 'work_sector', 'status_marriage', 'career', 'relationship', 'sex', 'gained_capital', 'lost_capital']

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


    @staticmethod
    def from_json(data):
        for i in mandatory_fields:
            if i not in data.keys():
                raise ValueError("Invalid person data.")
        return Person(data['name'],
                      data['age'],
                      data['work_sector'],
                      data['status_marriage'],
                      data['career'],
                      data['relationship'],
                      data['sex'],
                      data['gained_capital'],
                      data['lost_capital'],
                      data['education'] if data.get('education') is not None else None,
                      data['education_num'] if data.get('education_num') is not None else None,
                      data['race'] if data.get('race') is not None else None,
                      data['hours_per_week'] if data.get('hours_per_week') is not None else None,
                      data['country'] if data.get('hours_per_week') is not None else None)