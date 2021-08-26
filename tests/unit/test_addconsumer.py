# ------------------------------------------------
# Tests for AddConsumer
#
# (C) 2021 Emmanuel Oyedeji, Lagos, Nigeria
# email emmanueloyedeji2086@gmail.com
# ------------------------------------------------

import unittest
import logging
import json

from basecase import BaseCase
import variables

# Disable logging details. You can highlight code to include logging details back.
logging.disable(logging.CRITICAL)


class TestAddConsumer(BaseCase):

    def setUp(self):
        super(TestAddConsumer, self).setUp()
        self.consumers = variables.consumers
        self.assigner = variables.assigner

    def tearDown(self):
        self.consumers["topic1"].clear()
        self.consumers["topic2"].clear()
        self.consumers["topic3"].clear()
        self.assigner["topic1"][0]["p1"].clear()
        self.assigner["topic2"][0]["p1"].clear()
        self.assigner["topic2"][1]["p2"].clear()
        self.assigner["topic3"][0]["p1"].clear()
        self.assigner["topic3"][1]["p2"].clear()
        self.assigner["topic3"][2]["p3"].clear()

        # # Alternative implementation
        # self.consumers = variables.consumers
        # self.assigner = variables.assigner

    def test_valid_uuid_and_valid_topic(self):
        """Test for a valid UUID and valid topic"""

        url = "http://127.0.0.1:5000/kafka/consumer/add"
        payload = json.dumps({
            "consumer_id": "7c660ce4-8713-453a-b0d2-a7604de804b3",
            "topic": "topic1"
        })
        response = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload)

        statuscode = response.status_code
        self.assertEqual(statuscode, 201)
        self.assertEqual(response.content_type, "application/json")

        a = json.loads(response.data)
        self.assertEqual(
            a["status"], "7c660ce4-8713-453a-b0d2-a7604de804b3 added suucessfully to topic1")

    def test_invalid_uuid_and_valid_topic(self):
        """Test for invalid UUID and valid topic"""

        url = "http://127.0.0.1:5000/kafka/consumer/add"
        payload = json.dumps({
            "consumer_id": "7c660ce4-8713--b0d2-a7604de804b3",
            "topic": "topic3"
        })
        response = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload)

        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
        self.assertEqual(response.content_type, "application/json")

        a = json.loads(response.data)
        self.assertEqual(
            a["status"], "Invalid uuid")

    def test_valid_uuid_and_invalid_topic(self):
        """Test for valid UUID and invalid topic"""

        url = "http://127.0.0.1:5000/kafka/consumer/add"
        payload = json.dumps({
            "consumer_id": "7c660ce4-8713-453a-b0d2-a7604de804b3",
            "topic": "topic6"
        })
        response = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload)

        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
        self.assertEqual(response.content_type, "application/json")

        a = json.loads(response.data)
        self.assertEqual(
            a["status"], "topic6 not valid")

    def test_invalid_uuid_and_invalid_topic(self):
        """Test for invalid UUID and invalid topic"""

        url = "http://127.0.0.1:5000/kafka/consumer/add"
        payload = json.dumps({
            "consumer_id": "7c660ce4-8713--b0d2-a7604de804b3",
            "topic": "topic7"
        })
        response = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload)

        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
        self.assertEqual(response.content_type, "application/json")

        a = json.loads(response.data)
        self.assertEqual(
            a["status"], "Invalid uuid")

    def test_register_existing_consumer(self):
        """Test for re-registering an existing consumer"""

        url = "http://127.0.0.1:5000/kafka/consumer/add"

        payload = json.dumps({
            "consumer_id": "7c660ce4-8713-453a-b0d2-a7604de804b3",
            "topic": "topic2"
        })

        # registers consumer the first time.
        self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload)

        # tries to register same consumer again.
        response_2 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload)

        statuscode = response_2.status_code
        self.assertEqual(statuscode, 409)
        self.assertEqual(response_2.content_type, "application/json")

        a = json.loads(response_2.data)
        self.assertEqual(
            a["status"], "consumer already added")

    def test_missing_input_fields(self):
        """Test for valid UUID and invalid topic"""

        url = "http://127.0.0.1:5000/kafka/consumer/add"
        payload = json.dumps({

        })
        response = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload)

        statuscode = response.status_code
        self.assertEqual(statuscode, 500)


if __name__ == '__main__':
    unittest.main()
