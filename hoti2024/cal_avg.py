string = """
sys[7] finished, 836660553 cycles
sys[3] finished, 1168665077 cycles
sys[5] finished, 1508770923 cycles
sys[1] finished, 1508854380 cycles
sys[6] finished, 1848625261 cycles
sys[4] finished, 1848708718 cycles
sys[2] finished, 1848708718 cycles
sys[0] finished, 1848792175 cycles
"""

import re
# parse the string, extract all the numbers before the word 'cycles'

cycles = re.findall(r'(\d+) cycles', string)
cycles = list(map(int, cycles))

# calculate the average
print(len(cycles))
avg = sum(cycles) / len(cycles)

print(avg)
