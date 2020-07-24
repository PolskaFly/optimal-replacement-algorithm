class OptimalPageReplacement:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = []

    def opt_algorithm(self, distance, trace, pos) -> None:
        for x in range(len(self.cache)):
            # if statement to check if x is referenced ever again.
            if self.cache[x] not in trace[slice(pos + 1, None)]:
                self.cache[x] = trace[pos]
                break
            else:
                distance[x] = trace[slice(pos + 1, None)].index(self.cache[x])
        else:
            cache[distance.index(max(distance))] = trace[pos]


capacity = input("Capacity: ")
capacity = int(capacity)

cache = OptimalPageReplacement(capacity)

hits = 0
faults = 0

traceString = input("Trace (Example: 1 2 3): ")
trace = list([int(s) for s in traceString.split(' ')])

distance = [None] * capacity

for i in range(len(trace)):
    if trace[i] not in cache.cache:
        if len(cache.cache) < capacity:
            cache.cache.append(trace[i])
        else:
            cache.opt_algorithm(distance, trace, i)
        faults += 1
        print(cache.cache)
    else:
        hits += 1

print("Hits: ", hits)
print("Faults: ", faults)