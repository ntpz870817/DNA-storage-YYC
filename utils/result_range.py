import matplotlib.pyplot as plt
import numpy

rule_0 = [
    [
        8279.45,
        8235.10,
        8324.76,
        8414.07,
        8378.32
    ], [
        275261/((275261+53203)/2),
        275261/((275261+53103)/2),
        275261/((275261+53285)/2),
        275261/((275261+53249)/2),
        275261/((275261+53193)/2)
    ]
]

rule_495 = [
    [
        8125.13,
        8215.66,
        8050.90,
        8073.92,
        7986.02
    ], [
        275261/((275261+51721)/2),
        275261/((275261+51869)/2),
        275261/((275261+51819)/2),
        275261/((275261+51731)/2),
        275261/((275261+51883)/2)
    ]
]

rule_888 = [
    [
        2158.34,
        2143.81,
        2137.57,
        2163.88,
        2143.66
    ],[
        275261 / ((275261 + 1277) / 2),
        275261 / ((275261 + 1163) / 2),
        275261 / ((275261 + 1153) / 2),
        275261 / ((275261 + 1357) / 2),
        275261 / ((275261 + 1187) / 2)
    ]
]

rule_1535 = [
    [
        8462.81, 8485.49, 8552.28, 8676.76, 8511.67
    ], [
        275261 / ((275261 + 53047) / 2),
        275261 / ((275261 + 53161) / 2),
        275261 / ((275261 + 53159) / 2),
        275261 / ((275261 + 53181) / 2),
        275261 / ((275261 + 53065) / 2)
    ]
]

def mean(data):
    average = 0
    for value in data:
        average += value

    return average / len(data)


plt.figure()

value_0 = numpy.std(numpy.array(rule_0[0]))
plt.plot([mean(rule_0[0]) - value_0, mean(rule_0[0]) + value_0], [mean(rule_0[1]), mean(rule_0[1])], c="green")
value_1 = numpy.std(numpy.array(rule_0[1]))
plt.plot([mean(rule_0[0]), mean(rule_0[0])], [mean(rule_0[1]) - value_1, mean(rule_0[1]) + value_1], c="green")

value_0 = numpy.std(numpy.array(rule_495[0]))
plt.plot([mean(rule_495[0]) - value_0, mean(rule_495[0]) + value_0], [mean(rule_495[1]), mean(rule_495[1])], c="red")
value_1 = numpy.std(numpy.array(rule_495[1]))
plt.plot([mean(rule_495[0]), mean(rule_495[0])], [mean(rule_495[1]) - value_1, mean(rule_495[1]) + value_1], c="red")

value_0 = numpy.std(numpy.array(rule_888[0]))
plt.plot([mean(rule_888[0]) - value_0, mean(rule_888[0]) + value_0], [mean(rule_888[1]), mean(rule_888[1])], c="orange")
value_1 = numpy.std(numpy.array(rule_888[1]))
plt.plot([mean(rule_888[0]), mean(rule_888[0])], [mean(rule_888[1]) - value_1, mean(rule_888[1]) + value_1], c="orange")

value_0 = numpy.std(numpy.array(rule_1535[0]))
plt.plot([mean(rule_1535[0]) - value_0, mean(rule_1535[0]) + value_0], [mean(rule_1535[1]), mean(rule_1535[1])], c="blue")
value_1 = numpy.std(numpy.array(rule_1535[1]))
plt.plot([mean(rule_1535[0]), mean(rule_1535[0])], [mean(rule_1535[1]) - value_1, mean(rule_1535[1]) + value_1], c="blue")

# plt.scatter([mean(rule_0[0])], [mean(rule_0[1])], c="green", edgecolors="black", linewidths=1)
# plt.scatter([mean(rule_495[0])], [mean(rule_495[1])], c="red", edgecolors="black", linewidths=1)
# plt.scatter([mean(rule_888[0])], [mean(rule_888[1])], c="orange", edgecolors="black", linewidths=1)
# plt.scatter([mean(rule_1535[0])], [mean(rule_1535[1])], c="blue", edgecolors="black", linewidths=1)

plt.xlabel("Encoding runtime (seconds)")
plt.ylabel("Actual information density (bits/nt)")
# plt.axis([7000, 10000, 1.675, 1.685])
# plt.axis([2000, 2300, 1.985, 1.995])
plt.axis([0, 10000, 0.95, 2.05])
plt.autoscale(enable=True, axis='both', tight=True)


plt.show()
