
from model.producer_abstract import ProducerAbstract


class Producers(ProducerAbstract):

    def __init__(self, producers):
        self.producers = producers

    def add(self, producer_id):
        """ function to add new producer"""
        if producer_id in self.producers:
            return("producer already added")
        else:
            self.producers.append(producer_id)
            return(f"{producer_id} added")
