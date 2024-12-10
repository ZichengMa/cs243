string = """
sys[7] finished, 9569116 cycles
sys[3] finished, 12289056 cycles
sys[1] finished, 15713618 cycles
sys[5] finished, 15713630 cycles
sys[0] finished, 17124916 cycles
sys[4] finished, 17124928 cycles
sys[2] finished, 17124928 cycles
sys[6] finished, 17124940 cycles
"""

import re

cycles = re.findall(r'(\d+) cycles', string)
cycles = list(map(int, cycles))

print(len(cycles))
avg = sum(cycles) / len(cycles)

print(avg)
