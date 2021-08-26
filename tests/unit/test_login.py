# ------------------------------------------------
# Tests for Login
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
        self.producers = variables.producers
        self.consumers = variables.consumers
        self.populate_producers()
        self.populate_consumers()

    def tearDown(self):
        self.producers.clear()
        self.consumers["topic1"].clear()
        self.consumers["topic2"].clear()
        self.consumers["topic3"].clear()

    def populate_producers(self):
        self.producers.extend(
            ["18d52316-f15e-45b0-9ddd-a08ce4643f03",
             "e3717879-1aa8-42ff-83ae-6c6058f70ebb", "89bde096-8f7b-4ae8-aac2-9c20797713d1",
             "9fa403b0-a3bc-43a6-b557-4667667703fc"])

    def populate_consumers(self):
        self.consumers["topic1"].extend(
            ["18d52316-f15e-45b0-9ddd-a08ce4643f03",
             "e3717879-1aa8-42ff-83ae-6c6058f70ebb"])

        self.consumers["topic2"].extend(
            ["36efadc1-5bc9-4b5d-a1e8-9f8235e57d84", "73650010-6127-47f1-b03f-5cec89112ff6", ])

        self.consumers["topic3"].extend(
            ["cd91d68f-b8b9-451b-ac8f-a4d1f8035ea7",
                "bf319111-f533-4494-9d41-87a249a5b78c", "ceb9dec8-fae6-4b7d-bbb1-9bb00331edcd"])

    def test_login_for_valid_producer(self):
        """Test login for valid producer"""
        url = "http://127.0.0.1:5000/login/auth"
        payload_1 = json.dumps({
            "user_id": "e3717879-1aa8-42ff-83ae-6c6058f70ebb",
        })
        payload_2 = json.dumps({
            "user_id": "36efadc1-5bc9-4b5d-a1e8-9f8235e57d84",
        })

        response_1 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload_1)
        response_2 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload_2)

        statuscode_1 = response_1.status_code
        statuscode_2 = response_2.status_code

        self.assertEqual(statuscode_1, 200)
        self.assertEqual(statuscode_2, 200)

        a_1 = json.loads(response_1.data)
        a_2 = json.loads(response_2.data)

        self.assertEqual(a_1["login"], True)
        self.assertEqual(a_2["login"], True)

    def test_login_for_valid_consumer(self):
        """Test login for valid producer"""
        url = "http://127.0.0.1:5000/login/auth"

        payload_1 = json.dumps({
            "user_id": "e3717879-1aa8-42ff-83ae-6c6058f70ebb",
        })
        payload_2 = json.dumps({
            "user_id": "36efadc1-5bc9-4b5d-a1e8-9f8235e57d84",
        })
        payload_3 = json.dumps({
            "user_id": "ceb9dec8-fae6-4b7d-bbb1-9bb00331edcd",
        })

        response_1 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload_1)
        response_2 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload_2)
        response_3 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload_3)

        statuscode_1 = response_1.status_code
        statuscode_2 = response_2.status_code
        statuscode_3 = response_3.status_code

        self.assertEqual(statuscode_1, 200)
        self.assertEqual(statuscode_2, 200)
        self.assertEqual(statuscode_3, 200)

        a_1 = json.loads(response_1.data)
        a_2 = json.loads(response_2.data)
        a_3 = json.loads(response_3.data)

        self.assertEqual(a_1["login"], True)
        self.assertEqual(a_2["login"], True)
        self.assertEqual(a_3["login"], True)

    def test_login_for_invalid_user(self):
        url = "http://127.0.0.1:5000/login/auth"

        url = "http://127.0.0.1:5000/login/auth"
        payload_1 = json.dumps({
            "user_id": "e3717879-1aa8-42ff-83ae-6c6058f70ebb",
        })
        payload_2 = json.dumps({
            "user_id": "36efadc1-5bc9-4b5d-a1e8-9f8235e57d84",
        })

        response_1 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload_1)
        response_2 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload_2)

        statuscode_1 = response_1.status_code
        statuscode_2 = response_2.status_code

        self.assertEqual(statuscode_1, 200)
        self.assertEqual(statuscode_2, 200)

        a_1 = json.loads(response_1.data)
        a_2 = json.loads(response_2.data)

        self.assertEqual(a_1["login"], True)
        self.assertEqual(a_2["login"], True)

    def test_login_for_valid_consumer(self):
        """Test login for valid producer"""
        url = "http://127.0.0.1:5000/login/auth"

        payload_1 = json.dumps({
            "user_id": "e3717879-1aa8-42ff-83ae-6c6058f70exx",
        })
        payload_2 = json.dumps({
            "user_id": "36efadc1",
        })
        payload_3 = json.dumps({
            "user_id": "",
        })

        response_1 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload_1)
        response_2 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload_2)
        response_3 = self.app.post(
            url, headers={"Content-Type": "application/json"}, data=payload_3)

        statuscode_1 = response_1.status_code
        statuscode_2 = response_2.status_code
        statuscode_3 = response_3.status_code

        self.assertEqual(statuscode_1, 401)
        self.assertEqual(statuscode_2, 401)
        self.assertEqual(statuscode_3, 401)

        a_1 = json.loads(response_1.data)
        a_2 = json.loads(response_2.data)
        a_3 = json.loads(response_3.data)

        self.assertEqual(a_1["msg"], "user not registered")
        self.assertEqual(a_2["msg"], "user not registered")
        self.assertEqual(a_3["msg"], "user not registered")


if __name__ == '__main__':
    unittest.main()
