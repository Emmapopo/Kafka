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
   pass
if __name__ == '__main__':
    logger.info("Starting Server...")
    app.run(debug=True)
