import os
import keras
import json
from keras.models import model_from_json
import tensorflow as tf
from tensorflow import feature_column
from tensorflow.keras import layers
import tensorflow as tf

class IncomePredictionModel(object):
    def __init__(self, map_dict, model_json_path, model_weights_path):
        self.map_dict = map_dict

        # assert os.path.exists(model_json_path)
        # assert os.path.exists(model_weights_path)
        #
        # with open(model_json_path, 'r') as f:
        #     loaded_model = model_from_json(f.read())
        #
        # # load weights into new model
        # loaded_model.load_weights(model_weights_path)
        # print("Loaded model from disk")

        headers = ['age', 'workSector', 'education', 'educationNum', 'statusMarriage', 'career', 'relationship', 'race', 'sex', 'gainedCapital', 'lostCapital', 'hoursPerWeek', 'country']
        feature_columns = []
        for header in headers:
            feature_columns.append(feature_column.numeric_column(header))

        feature_layer = tf.keras.layers.DenseFeatures(feature_columns)

        loaded_model = tf.keras.Sequential([
            feature_layer,
            layers.Dense(128, activation='relu'),
            layers.Dense(128, activation='relu'),
            layers.Dense(1)
        ])

        loaded_model.compile(optimizer='adam',
                             loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                             metrics=['accuracy'])
        loaded_model.load_weights('../ckpts/model.h5')


with open('mapping.json', 'r') as f:
    map_dct = json.load(f)

model = IncomePredictionModel(map_dct, "../ckpts/model.json", "../ckpts/model.h5")
print('a')