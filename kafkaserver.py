# ------------------------------------------------
# Kafka server containing six endpoints
#
# (C) 2021 Emmanuel Oyedeji, Lagos, Nigeria
# email emmanueloyedeji2086@gmail.com
# ------------------------------------------------

import os
from logging import log
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies
)

import functions
import variables
from controller.producers import Producers
from controller.consumers import Consumers
from log.logging_func import logger

producers = variables.producers
consumers = variables.consumers
assigner = variables.assigner

app = Flask(__name__)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_ACCESS_COOKIE_PATH'] = '/kafka/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
# The Jwt_secret_key is obtained from environment variables
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

jwt = JWTManager(app)
CORS(app)

producer_controller = Producers(producers)
consumer_controller = Consumers(consumers, assigner)


@app.route("/login/auth", methods=["POST"])
def login():
    """ Endpoint to login to the kafka server"""
    try:
        json_data = request.get_json()
        user_id = json_data["user_id"]
        logger.info(f'{user_id} tried to login')

    except Exception as e:
        logger.error("InputFailed occured", exc_info=True)
        return{"status": e}

    # This variable stores if the user is logged_in as a producer, consumer, or both.
    logged_in_as = []

    try:
        if user_id not in producers:
            if user_id not in consumers["topic1"] and user_id not in consumers["topic2"] and user_id not in consumers["topic3"]:
                logger.error(f'{user_id} not registered')
                return jsonify({"msg": "user not registered"}), 401

        if user_id in producers:
            logged_in_as.append("producer")

        if user_id in consumers["topic1"] or user_id in consumers["topic2"] or user_id in consumers["topic3"]:
            logged_in_as.append("consumer")

        access_token = create_access_token(identity={'user_id': user_id})
        refresh_token = create_refresh_token(identity={'user_id': user_id})

        resp = jsonify({'login': True, 'user_id': user_id,
                        "logged_in_as": logged_in_as})
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)\

        logger.info(f'{user_id} logged in as {logged_in_as}')
        return resp, 200

    except:
        logger.error("Exception occured", exc_info=True)
        return{"status": f"{user_id} failed to login"}


@app.route('/token/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    # Create the new access token
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)

    # Set the access JWT and CSRF double submit protection cookies
    # in this response
    resp = jsonify({'refresh': True})
    set_access_cookies(resp, access_token)
    return resp, 200


@app.route('/kafka/producer/add', methods=['POST'])
def add_producer():
    """ Endpoint to add a producer to the kafka server"""

    try:
        json_data = request.get_json()
        user_id = json_data["user_id"]
        logger.info(f'{user_id} tried to register as a producer')
    except Exception as e:
        logger.error("InputFailed occured", exc_info=True)
        return{"status": e}

    try:

        if not functions.is_valid_uuid(user_id):
            logger.error(
                f'{user_id} tried to register as a producer with invalid UUID')
            return {"status": "Invalid uuid"}, 400

        status = producer_controller.add(user_id)
        if status == "user already added":
            return {"status": status}, 409

        else:
            logger.info(f'{user_id} registered as producer successfully')
            return {"status": status}, 201

    except:
        logger.error("Exception occured", exc_info=True)
        return{"status": f"{user_id} invalid field"}


@app.route('/kafka/consumer/add', methods=['POST'])
def add_consumer():
    """ Endpoint to add a consumer to the kafka server"""
    try:
        json_data = request.get_json()
        consumer_id = json_data["consumer_id"]
        topic = json_data["topic"]
        logger.info(
            f'{consumer_id} tried to register as a consumer to topic: {topic}')

    except Exception as e:
        logger.error("InputFailed occured", exc_info=True)
        return{"status": e}

    try:
        if not functions.is_valid_uuid(consumer_id):
            logger.error(
                f'{consumer_id} tried to register as a consumer with invalid UUID')
            return {"status": "Invalid uuid"}, 400

        if topic not in ["topic1", "topic2", "topic3"]:
            logger.error(
                f'{consumer_id} tried to register to invalid topic: {topic}')
            return {"status": f"{topic} not valid"}, 400

        status = consumer_controller.add(consumer_id, topic)
        if status == "consumer already added":
            logger.error(f'consumer: {consumer_id} registered before')
            return {"status": status}, 409

        else:
            logger.info(f'{consumer_id} registered as consumer successfully')
            return {"status": status}, 201

    except:
        logger.error("Exception occured", exc_info=True)
        return{"status": "invalid field"}


if __name__ == '__main__':
    logger.info("Starting Server...")
    app.run(debug=True)
