# ------------------------------------------------
# BaseCase containing the setUp and tearDown for the test files
#
# (C) 2021 Emmanuel Oyedeji, Lagos, Nigeria
# email emmanueloyedeji2086@gmail.com
# ------------------------------------------------

import unittest
import os
import sys

# adding grandparent directory to path so I can make imports from there.
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
grandparentdir = os.path.dirname(parentdir)
sys.path.append(grandparentdir)

from kafkaserver import app


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        

    def tearDown(self):
        pass
    
