import math
import matplotlib.pyplot as plt
import numpy

del_poss_range = numpy.linspace(0, 1, 101)

repetition_numbers = [1, 2, 5, 10, 20, 50, 100, 200, 1000, 10000]

number = math.pow(10, 6)
yin_yang_group = []

for repetition_number in repetition_numbers:
    coding_potentials = []
    for poss in del_poss_range:
        repetition_rate = math.pow(poss, repetition_number)
        actual_number = number * (1 - repetition_rate) / 2 + number * repetition_rate

        coding_potentials.append(number / actual_number)

    yin_yang_group.append(coding_potentials)

plt.figure()

for index in range(len(repetition_numbers)):
    plt.plot([int(_ * 100) for _ in del_poss_range], yin_yang_group[index],
             label=str(repetition_numbers[index]) + " iterations")

plt.xlabel("Average rejected rate in screening operation (%)")
plt.ylabel("Theoretical information density (bits/nt)")
plt.axis([-5, 105, 0.92, 2.08])
plt.legend(loc="lower left")

plt.show()
