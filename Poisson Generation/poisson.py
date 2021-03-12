import numpy as np

lam = 5
size = 113

failure = 0
tests = 10000
test_count = 0
while test_count < tests:
    count_0 = 0
    rand_data = np.random.poisson(lam, size)
    for i in range(0,112):
        if rand_data[i] == 0:
            count_0 += count_0 + 1
    if count_0 > 0:
        failure = failure+1
    test_count = test_count+1

print((tests - failure)/tests)
