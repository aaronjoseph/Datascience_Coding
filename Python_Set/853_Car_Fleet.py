class Solution(object):
    # def carFleet(self, target, position, speed):
    #     cars = sorted(zip(position, speed))
    #     times = [float(target - p) / s for p, s in cars]
    #     ans = 0
    #     while len(times) > 1:
    #         lead = times.pop()
    #         if lead < times[-1]: ans += 1  # if lead arrives sooner, it can't be caught
    #         else: times[-1] = lead # else, fleet arrives at later time 'lead'
    #
    #     return ans + bool(times) # remaining car is fleet (if it exists)


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

x = Solution()
x.carFleet(target, position, speed)


time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
res = cur = 0
for t in time[::-1]:
    if t > cur:
        res += 1
        cur = t

car = sorted(zip(position, speed), key=lambda x:x[0],reverse=True)
time = [(target - p)/float(s) for p, s in car]

fleet = 0
while time:
    lead_time = time.pop(0)
    fleet += 1
    while time and time[0] <= lead_time:
        time.pop(0)
print(fleet)