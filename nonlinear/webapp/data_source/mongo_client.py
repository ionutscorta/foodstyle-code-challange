from bson.objectid import ObjectId
import pymongo


class MongoClient:
    def __init__(self, host, db_name, collection):
        self.host = host
        self.db_name = db_name
        self.db_client = pymongo.MongoClient(self.host)
        self.person_db = self.db_client[self.db_name]
        self.collection = self.person_db[collection]
        self.prepare_db()

    def insert(self, data):
        self.collection.insert_one(data)

    def get(self, query):
        return self.collection.find_one(query)

    def prepare_db(self):
        if "DefaultDataSpecs" not in self.person_db.list_collection_names():
            default_data = {
                "workSector": ("Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"),
                "education": ("Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"),
                "statusMarriage": ("Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"),
                "career": (
                "Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv",
                "Armed-Forces"),
                "relationship": ("Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"),
                "race": ("Black", "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other"),
                "sex": ("Male", "Female"),
                "country": (
                    "United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany", "Outlying-US(Guam-USVI-etc)", "India", "Japan", "Greece", "South", "China", "Cuba", "Iran", "Honduras", "Philippines", "Italy", "Poland", "Jamaica",
                    "Vietnam", "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic", "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala", "Nicaragua", "Scotland", "Thailand", "Yugoslavia", "El-Salvador",
                    "Trinadad&Tobago",
                    "Peru", "Hong", "Holand-Netherlands")
            }
            self.person_db["DefaultDataSpecs"].insert_one(default_data)
