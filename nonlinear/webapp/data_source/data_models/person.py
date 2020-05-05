import uuid

mandatory_fields = ['name', 'age', 'workSector', 'statusMarriage', 'career', 'relationship', 'sex', 'gainedCapital', 'lostCapital']


class Person:
    def __init__(self, id, name, age, work_sector,
                 status_marriage, career, relationship, sex, gained_capital, lost_capital,
                 education=None, education_num=None, race=None, hours_per_week=None, country=None):
        self.id = id
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

    def to_rest_object(self):
        return {
            "age": self.age,
            "workSector": self.work_sector,
            "education": self.education,
            "educationNum": self.education_num,
            "statusMarriage": self.status_marriage,
            "career": self.career,
            "relationship": self.relationship,
            "race": self.race,
            "sex": self.sex,
            "gainedCapital": self.gained_capital,
            "lostCapital": self.lost_capital,
            "hoursPerWeek": self.hours_per_week,
            "country": self.country,
            "name": self.name
        }

    @staticmethod
    def from_json(data):
        for i in mandatory_fields:
            if i not in data.keys():
                raise ValueError("Invalid person data! Missing {}".format(i))
        return Person(str(uuid.uuid4()),
                      data['name'],
                      data['age'],
                      data['workSector'],
                      data['statusMarriage'],
                      data['career'],
                      data['relationship'],
                      data['sex'],
                      data['gainedCapital'],
                      data['lostCapital'],
                      data['education'] if data.get('education') is not None else None,
                      data['educationNum'] if data.get('educationNum') is not None else None,
                      data['race'] if data.get('race') is not None else None,
                      data['hoursPerWeek'] if data.get('hoursPerWeek') is not None else None,
                      data['country'] if data.get('country') is not None else None)

    @staticmethod
    def to_person_object(data):
        return Person(data['id'],
                      data['name'],
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
                      data['country'] if data.get('country') is not None else None)
