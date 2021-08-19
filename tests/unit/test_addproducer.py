# ------------------------------------------------
# Tests for AddProducers
#
# (C) 2021 Emmanuel Oyedeji, Lagos, Nigeria
# email emmanueloyedeji2086@gmail.com
# ------------------------------------------------

import unittest
import logging
import json

from basecase import BaseCase

# Disable logging details. You can highlight code to include logging details back.
logging.disable(logging.CRITICAL)


class TestAddProducer(BaseCase):

    def test_valid_uuid(self):
        """Test for a valid UUID"""

        url = "http://127.0.0.1:5000/kafka/producer/add"
        payload = json.dumps({
            "user_id": "7c660ce4-8713-453a-b0d2-a7604de804b3"
        })
        response = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload)

        statuscode = response.status_code
        self.assertEqual(statuscode, 201)
        self.assertEqual(response.content_type, "application/json")

        a = json.loads(response.data)
        self.assertEqual(
            a["status"], "7c660ce4-8713-453a-b0d2-a7604de804b3 added")

    def test_invalid_uuid(self):
        """Test for an invalid UUID"""

        url = "http://127.0.0.1:5000/kafka/producer/add"
        payload = json.dumps({
            "user_id": "7c660ce4-8713-453a-b0d2-a7604de804"
        })
        response = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload)

        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
        self.assertEqual(response.content_type, "application/json")

        a = json.loads(response.data)
        self.assertEqual(
            a["status"], "Invalid uuid")

    def test_register_existing_user(self):
        """Test for re-registering an existing user"""

        url = "http://127.0.0.1:5000/kafka/producer/add"

        payload = json.dumps({
            "user_id": "7c660ce4-8713-453a-b0d2-a7604de804b3"
        })

        # registers user the first time.
        response_1 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload)

        # tries to register same user again.
        response_2 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload)

        statuscode = response_2.status_code
        self.assertEqual(statuscode, 409)
        self.assertEqual(response_2.content_type, "application/json")

        a = json.loads(response_2.data)
        self.assertEqual(
            a["status"], "user already added")


if __name__ == '__main__':
    unittest.main()
