
# The in-memory variable carrying the list of producers added to the kafka server.
producers = []

consumers = {
    "topic1": [],
    "topic2": [],
    "topic3": [],
}

assigner = {
    "topic1": [{"p1": [1223, 444]}],
    "topic2": [{"p1": []}, {"p2": []}],
    "topic3": [{"p1": []}, {"p2": []}, {"p3": []}]
}
