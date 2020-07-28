import codecs
import matplotlib.pyplot as plt
import numpy as np

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
            self.cache[distance.index(max(distance))] = trace[pos]


trials = input("Trials: ")
trials = int(trials)

trace = []

with codecs.open("multi2.trc", "r", "UTF8") as inputFile:
    inputFile = inputFile.readlines()
for line in inputFile:
    trace.append(int(line))

# traceString = input("Trace (Example: 1 2 3): ")
# trace = list([int(s) for s in traceString.split(' ')])

xAxis = []
yAxis = []

for i in range(trials):
    capacity = input("Capacity: ")
    capacity = int(capacity)
    cache = OptimalPageReplacement(capacity)
    hits = 0
    faults = 0
    distance = [None] * capacity

    for j in range(len(trace)):
        if trace[j] not in cache.cache:
            if len(cache.cache) < capacity:
                cache.cache.append(trace[j])
            else:
                cache.opt_algorithm(distance, trace, j)
            faults += 1
        else:
            hits += 1

    print("Hits: ", hits)
    print("Faults: ", faults)
    xAxis.append(capacity)
    yAxis.append((((hits)/(hits+faults))*100))

plt.plot(xAxis, yAxis, linestyle='--', marker='s', color='k')
plt.xticks(np.arange(200, 3200, step=200))
plt.title('Multi2')
plt.ylabel('Hit Ratio (%)')
plt.xlabel('Cache Size (# of blocks)')
plt.grid()
plt.show()

