import os
import json
import numpy as np
from tensorflow.keras.models import load_model as load_keras_model


class Formatter:
    def __init__(self, map_dict):
        self.map_dict = map_dict
        self.target_inv_map = {v: k for k, v in self.map_dict['income'].items()}

    def parse_dict(self, dct):
        age = int(dct['age'])
        workSector = self.map_dict['workSector'][dct['work_sector'].lower()]
        education = self.map_dict['education'][dct['education'].lower()]
        educationNum = int(dct['education_num'])
        statusMarriage = self.map_dict['statusMarriage'][dct['status_marriage'].lower()]
        career = self.map_dict['career'][dct['career'].lower()]
        relationship = self.map_dict['relationship'][dct['relationship'].lower()]
        race = self.map_dict['race'][dct['race'].lower()]
        sex = self.map_dict['sex'][dct['sex'].lower()]
        gainedCapital = int(dct['gained_capital'])
        lostCapital = int(dct['lost_capital'])
        hoursPerWeek = int(dct['hours_per_week'])
        country = self.map_dict['country'][dct['country'].lower()]

        return np.array([[age, workSector, education, educationNum, statusMarriage, career, relationship,
                          race, sex, gainedCapital, lostCapital, hoursPerWeek, country]])


class IncomePredictionModel(object):
    def __init__(self, map_dict, ckpt_path):
        self.map_dict = map_dict
        self.target_inv_map = {v: k for k, v in self.map_dict['income'].items()}
        assert os.path.exists(ckpt_path)

        self.ckpt_path = ckpt_path

    def predict(self, dct_to_pred):
        input_data = self.parse_dict(dct_to_pred)

        if input_data is not None:
            # TODO workaround for multithreading issue, should be fixed
            prediction = load_keras_model(self.ckpt_path).predict(input_data)

            score = prediction[0][np.argmax(prediction)]
            pred_cls = self.target_inv_map[np.argmax(prediction)]

            return {"score": score,
                    "prediction": pred_cls}
        else:
            return {"Error! input_data is None"}

    def parse_dict(self, dct):
        age = int(dct['age'])
        workSector = self.map_dict['workSector'][dct['workSector'].lower()]
        education = self.map_dict['education'][dct['education'].lower()]
        educationNum = int(dct['educationNum'])
        statusMarriage = self.map_dict['statusMarriage'][dct['statusMarriage'].lower()]
        career = self.map_dict['career'][dct['career'].lower()]
        relationship = self.map_dict['relationship'][dct['relationship'].lower()]
        race = self.map_dict['race'][dct['race'].lower()]
        sex = self.map_dict['sex'][dct['sex'].lower()]
        gainedCapital = int(dct['gainedCapital'])
        lostCapital = int(dct['lostCapital'])
        hoursPerWeek = int(dct['hoursPerWeek'])
        country = self.map_dict['country'][dct['country'].lower()]

        return np.array([[age, workSector, education, educationNum, statusMarriage, career, relationship,
                          race, sex, gainedCapital, lostCapital, hoursPerWeek, country]])


def load_model(model_root):
    with open(os.path.join(model_root, 'mapping.json'), 'r') as f:
        map_dct = json.load(f)

    model = IncomePredictionModel(map_dct, os.path.join(model_root, "../ckpts/model_v2/my_net_save.h5"))
    return model
