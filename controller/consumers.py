
from model.consumer_abstract import ConsumerAbstract


class Consumers(ConsumerAbstract):

    def __init__(self, consumers, assigner):
        self.consumers = consumers
        self.assigner = assigner

    def add(self, consumer_id, topic):
        """ function to add new consumer to a specified topic"""
        if topic == "topic1":

            if consumer_id in self.consumers['topic1']:
                return("consumer already added")
                
            # check to see if there's space for any consumer.
            # max_consumer = 1
            if len(self.consumers["topic1"]) == 0:
                self.consumers["topic1"].append(consumer_id)
                self.assigner["topic1"][0]["p1"].append(consumer_id)
                return(f"{consumer_id} added suucessfully to {topic}")

            elif len(self.consumers["topic1"]) == 1:
                return("Topic 1 space for consumers already filled")

            else:
                return("Topic 1 space for consumers already filled")

        if topic == "topic2":
            if consumer_id in self.consumers['topic2']:
                return("consumer already added")

            # check to see if there's space for a new consumer.
            # max_consumer = 2
            if len(self.consumers["topic2"]) == 0:
                self.consumers["topic2"].append(consumer_id)
                self.assigner["topic2"][0]["p1"].append(consumer_id)
                self.assigner["topic2"][1]["p2"].append(consumer_id)
                return(f"{consumer_id} added suucessfully to {topic}")

            elif len(self.consumers["topic2"]) == 1:
                self.consumers["topic2"].append(consumer_id)
                self.assigner["topic2"][1]["p2"].pop()
                self.assigner["topic2"][1]["p2"].append(consumer_id)
                return(f"{consumer_id} added suucessfully to {topic}")

            elif len(self.consumers["topic2"]) == 2:
                return("Topic 2 space for consumers already filled")

            else:
                return("Topic 2 space for consumers already filled")

        if topic == "topic3":
            if consumer_id in self.consumers['topic3']:
                return("consumer already added")

            # check to see if there's space for a new consumer.
            # max_consumer = 3
            if len(self.consumers["topic3"]) == 0:
                self.consumers["topic3"].append(consumer_id)
                self.assigner["topic3"][0]["p1"].append(consumer_id)
                self.assigner["topic3"][1]["p2"].append(consumer_id)
                self.assigner["topic3"][2]["p3"].append(consumer_id)
                return(f"{consumer_id} added suucessfully to {topic}")

            elif len(self.consumers["topic3"]) == 1:
                self.consumers["topic3"].append(consumer_id)
                self.assigner["topic3"][1]["p2"].pop()
                self.assigner["topic3"][1]["p2"].append(consumer_id)
                return(f"{consumer_id} added suucessfully to {topic}")

            elif len(self.consumers["topic3"]) == 2:
                self.consumers["topic3"].append(consumer_id)
                self.assigner["topic3"][2]["p3"].pop()
                self.assigner["topic3"][2]["p3"].append(consumer_id)
                return(f"{consumer_id} added suucessfully to {topic}")

            elif len(self.consumers["topic3"]) == 3:
                return("Topic 3 space for consumers already filled")

            else:
                return("Topic 2 space for consumers already filled")
