from matplotlib import pyplot as plt
import sys
# Define constants
TIME_INCREMENT = 10  # nanoseconds
FILENAME = 'astra-sim/extern/network_backend/ns-3/scratch/output/fct.txt'

# parse 1st argument as the figure's label name
figure_name = sys.argv[1]


# Initialize queue and variables
queue = []
current_time = 0
queue_length_over_time = []

# Function to parse a line from the file
def parse_line(line):
    parts = line.strip().split()
    sip = int(parts[0], 16)
    dip = int(parts[1], 16)
    sport = int(parts[2])
    dport = int(parts[3])
    size = int(parts[4])
    start_time = int(parts[5])
    fct = int(parts[6])  # Flow completion time in ns
    end_time = start_time + fct
    return size, start_time, end_time, fct

# Read and parse file data
with open(FILENAME, 'r') as file:
    data = [parse_line(line) for line in file if line.strip()]

index_dict = {"size": 0, "start_time": 1, "end_time": 2, "fct": 3}
time_series = []
# Simulation loop
while data or queue:
    # Add messages that start at the current time to the queue
    while data and data[0][index_dict["start_time"]] <= current_time: # 1 is the start time
        size, start_time, end_time, fct = data.pop(0)
        queue.append((size, end_time))

    # Remove messages that have completed by the current time
    # 1 is the end time
    queue = [item for item in queue if item[1] > current_time]

    # Calculate the total queue length
    total_queue_length = sum(size for size, _ in queue)
    queue_length_over_time.append(total_queue_length)
    time_series.append(current_time)


    # Print queue length every 10 nanoseconds
    # if current_time % TIME_INCREMENT == 0:
    #     print(f"Time: {current_time} ns, Queue Length: {total_queue_length} bytes")

    # Increment the time
    current_time += TIME_INCREMENT


# Plotting the results
plt.figure(figsize=(8, 6))
plt.plot(time_series, queue_length_over_time, label='Queue Length')
plt.xlabel("Time (ns)")
plt.ylabel("Queue length in bytes")

# Set the title of the plot
plt.title(f"Queue Length Over Time for {figure_name}")

plt.legend()

# Save the plot
plt.savefig("queue_length_over_time.png", transparent=True)
