# ------------------------------------------------
# Kafka server containing six endpoints
#
# (C) 2021 Emmanuel Oyedeji, Lagos, Nigeria
# email emmanueloyedeji2086@gmail.com
# ------------------------------------------------

from flask import Flask, request

import functions
import variables
from controller.producers import Producers
from controller.consumers import Consumers
from log.logging_func import logger

producers = variables.producers
consumers = variables.consumers
assigner = variables.assigner

app = Flask(__name__)


producer_controller = Producers(producers)
consumer_controller = Consumers(consumers, assigner)


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
