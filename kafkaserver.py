# ------------------------------------------------
# Kafka server containing six endpoints
#
# (C) 2021 Emmanuel Oyedeji, Lagos, Nigeria
# email emmanueloyedeji2086@gmail.com
# ------------------------------------------------

from flask import Flask, request
import sys
from log.logging_func import logger

app = Flask(__name__)


@app.route("/")
def main():
    return '''
     <form action="/echo" method="POST">
         <input name="text">
         <input type="submit" value="Echo">
     </form>
     '''


@app.route("/echo", methods=['POST'])
def echo():
    if 'text' in request.form:
        return "You said: " + request.form['text']
    else:
        return "Nothing to say?"


if __name__ == '__main__':
    logger.info("Starting Server...")
    app.run()
