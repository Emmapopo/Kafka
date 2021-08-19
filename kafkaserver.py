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
from log.logging_func import logger

producers = variables.producers

app = Flask(__name__)

producer_controller = Producers(producers)


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


if __name__ == '__main__':
    logger.info("Starting Server...")
    app.run(debug=True)
