import heapq
class PriorityQueue:
    def __init__(self):
        self.content = []

    def add(self, item): # add via priority, arrival time will be the consideration, queue will order in such a way that will be sorted via arrival time
        heapq.heappush(self.content, item)

    def peek(self): # returns top element
        return self.content[0]

    def poll(self): # returns top element and removes from list
        return heapq.heappop(self.content) if len(self.content) > 0 else None

    def is_empty(self): #
        return len(self.content) == 0

    def __str__(self):
        return str(heapq.nsmallest(len(self.content), self.content))

# customer = (arrival time, duration) tuple
# shorter duration = higher priority
# parking_spaces = # of parking spaces
# blocktime = time required to drive around the block

def simuleer_parking(parking_spaces, blocktime, customers):
    customer_queue = PriorityQueue() # create empty priority queue
    for arrival, duration in customers: # adding via given priorityqueue method, customers one by one
        customer_queue.add((arrival, duration))

    t = blocktime # the amount of time at which each customer drives around the block when the parking lot is full
    parked = [] # parking lot
    while not customer_queue.is_empty(): # introducing a loop at which we poll (extract and remove) customers from queue, top one being the one with shortest arrival time
        arrival, duration = customer_queue.poll()
        current_time = arrival
        if len(parked) < parking_spaces: # parking lot is not full.
            parked = [i for i in parked if i[0] > current_time] # we update the parking lot if there are still cars that have stayed as long as their leaving time
            new_current = (arrival + duration, duration)
            parked.append(new_current)
            print(parked, customer_queue)
        else: # parking lot is full.
            leave_time = min(parked)[0] # the earliest time at which a car leaves.
            if current_time < leave_time: # not enough parking spaces and duration has not passed yet
                arrival += t  # goes around block
                customer_queue.add((arrival, duration))  # readded to priority queue
                print(parked, customer_queue)
            elif current_time >= leave_time: # when the car arrives, one of the cars in parking lot are ready to leave
                parked = [i for i in parked if i[0] > current_time] # car is at or exceeds leave time, previous car leaves (any car that has exceeded their leaving time)
                new_current = (arrival + duration, duration)
                parked.append(new_current) # new arriving car gets added to parking space
                print(parked, customer_queue)
    lastcar = max(parked) # we get the max value from the list of tuples to extract the car that has the biggest leaving time, which is ultimately the time at which the last customer leaves
    return lastcar[0]



def main():
    space = 10
    t = 4
    cust = [(12, 6), (11, 10), (6, 3), (10, 3), (36, 8), (63, 7), (57, 5), (50, 9), (32, 4), (44, 3), (68, 10), (29, 5), (10, 10), (68, 10), (56, 2), (35, 8), (25, 2), (58, 9), (17, 8), (51, 3), (36, 9), (69, 3), (21, 4), (34, 10), (63, 4), (41, 6), (27, 3), (67, 3), (44, 7), (48, 1)]
    simuleer_parking(space, t , cust)

main()