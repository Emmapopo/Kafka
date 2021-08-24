
from model.producer_abstract import ProducerAbstract


class Producers(ProducerAbstract):

    def __init__(self, producers):
        self.producers = producers

    def add(self, user_id):
        """ function to add new producer"""
        if user_id in self.producers:
            return("user already added")
        else:
            self.user_id = user_id
            self.producers.append(self.user_id)
            return(f"{self.user_id} added")
