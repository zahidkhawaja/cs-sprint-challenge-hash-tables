# One way flight with layovers - tickets scrambled
#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    route = []

    # Hash tickets
    hash = {}

    for ticket in tickets:
        # Starting location is the key and the destination is the value
        hash[ticket.source] = ticket.destination
    
    # 'Source' ticket
    # First flight ticket has a source of 'NONE'
    route.append(hash["NONE"])

    # Add ticket based on value of last ticket
    for ticket in hash:
        if ticket == "NONE":
            continue
        route.append(hash[route[-1]])
    return route
