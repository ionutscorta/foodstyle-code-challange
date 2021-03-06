from flask import Flask, request, Response, jsonify
from flask_jwt import JWT, jwt_required
from nonlinear.webapp.utils import init_logging
from nonlinear.webapp.data_source.identity_store import IdentityStore
from nonlinear.webapp.data_source.person_store import PersonStore
from nonlinear.webapp.data_source.data_models.person import Person
from nonlinear.webapp.config import Config
from nonlinear.ml.model.model import load_model
import sys
import os


import logging


init_logging()


def identity(payload):
    api_key = payload['identity']
    return IdentityStore.get_instance().get_identity(api_key)


prediction_model = load_model(os.path.dirname(sys.modules[load_model.__module__].__file__))

app = Flask(__name__)

app.config.from_pyfile('config_file.cfg')
app.config['JWT_AUTH_URL_RULE'] = None

for k, v in app.config.items():
    Config[k] = v

jwt = JWT(app, identity_handler=identity)


@app.route('/auth', methods=['POST'])
def authenticate():
    try:
        req_json = request.get_json()

        assert 'api_key' in req_json, 'Missing API Key'

        api_key = req_json['api_key']

        api_resp = IdentityStore.get_instance().get_identity(api_key)

        if api_resp is None:
            return Response('Unauthorized API Key!', status=401)

        return jsonify({'access_token': jwt.jwt_encode_callback(api_resp).decode()})
    except Exception as e:
        logging.exception('Error running auth')
        return Response(str(e), status=500)


@app.route('/generateApiKey', methods=['POST'])
def generate_api_key():
    try:
        if request.remote_addr != '127.0.0.1':
            return Response('Not allowed', status=401)

        api_key = IdentityStore.get_instance().generate_api_key()

        return jsonify({'api_key': api_key})
    except Exception as e:
        logging.exception('Error running generateApiKey')
        return Response(str(e), status=500)


@app.route('/insertPerson', methods=['POST'])
@jwt_required()
def insert_person():
    try:
        req_json = request.get_json()
        person = Person.from_json(req_json).__dict__
        PersonStore.get_instance().insert_person(person)
        return jsonify({'Status': 'Done',
                        'PersonID': person['id']})
    except ValueError as e:
        logging.exception('Error running insertPerson')
        return Response(str(e), status=400)
    except Exception as e:
        logging.exception('Error running insertPerson')
        return Response(str(e), status=500)


@app.route('/getPerson/<person_id>', methods=['GET'])
@jwt_required()
def get_person(person_id):
    try:
        person = PersonStore.get_instance().get_person(person_id)

        person_object = person.to_rest_object()
        prediction = prediction_model.predict(person_object)

        person_object['predictedIncome'] = prediction['prediction']
        person_object['predictionScore'] = str(prediction['score'])

        return jsonify(person_object)
    except Exception as e:
        logging.exception('Error running getPerson')
        return Response(str(e), status=500)


@app.route('/listPersons', methods=['GET'])
def list_persons():
    try:
        person_ids = PersonStore.get_instance().list_persons()
        return jsonify({'person_ids': person_ids})
    except Exception as e:
        logging.exception('Error running getPerson')
        return Response(str(e), status=500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=False)
