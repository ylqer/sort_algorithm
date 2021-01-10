import time

start_time = time.time()

for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print("a: %d,\t b: %d,\t c: %d,\t" % (a, b, c))

end_time = time.time()

print("total time is: %d" % (end_time - start_time))
print("finished")
