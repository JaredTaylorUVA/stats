import math
import matplotlib.pyplot as plt

x = 1000
a = 24693
c = 3967
K = 2**15
x_list = []
u_list = []
time_list = []
x_list.append(x)
for i in range(0, 4000):
    x = (a*x_list[i] + c) % K
    x_list.append(x)
    u = x_list[i+1]/K
    u_list.append(u)
for n in range(0, 1000):
    time = 0
    counter = 4
    while counter > 0:
        if u_list[0] < .2:
            time += 10
            counter -= 1
        elif .2 <= u_list[0] < .5:
            time += 32
            counter -= 1
        else:
            var = (u_list[0] - 0.5)/0.5
            y = -12*math.log(1 - var)
            if y <= 25:
                time += 7 + y
                counter = 0
            else:
                time += 32
                counter -= 1
        u_list.pop(0)
    time_list.append(time)

print(time_list)
print(len(time_list))
print("Mean: ", sum(time_list)/1000)

fifteen = 0
for val in time_list:
    if val <= 15:
        fifteen += 1

print("W <= 15: ", fifteen/1000)

twenty = 0
for val in time_list:
    if val <= 20:
        twenty += 1

print("W <= 20: ", twenty/1000)

thirty = 0
for val in time_list:
    if val <= 30:
       thirty += 1

print("W <= 30: ", thirty/1000)

forty = 0
for val in time_list:
    if val > 40:
        forty += 1

print("W > 40: ", forty/1000)

w5 = 0
for val in time_list:
    if val > time_list[5]:
        w5 += 1

print("W > ", time_list[5], " (W5): ", w5/1000)

w6 = 0
for val in time_list:
    if val > time_list[6]:
        w6 += 1

print("W > ", time_list[6], " (W6): ", w6/1000)

w7 = 0
for val in time_list:
    if val > time_list[7]:
        w7 += 1

print("W > ", time_list[7], " (W7): ", w7/1000)

time_list.sort()
p_list = []
for o in range(0, 1000):
    p_list.append(o/1000)
print("First quartile: ", time_list[249])
print("Median: ", time_list[499])
print("Third quartile: ", time_list[749])
plt.plot(time_list, p_list)
print(time_list)
print(max(time_list))
plt.show()
