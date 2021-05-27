import random
import math
temp = 100

def calc_easom(x1,x2):
    easom = -math.cos(x1)*math.cos(x2)*math.pow(math.e, -math.pow(x1-math.pi,2) - math.pow(x2-math.pi,2))
    return easom

def get_random():
    x1 = random.randint(-100,100)
    x2 = random.randint(-100,100)
    val = calc_easom(x1,x2)
    return [val,x1,x2]

def get_probability(point1, point2):
    prob = random.uniform(0,1)
    if prob < math.pow(math.e,(point1[0]-point2[0])/temp):
        return point1
    else:
        return point2


def shift(x1,x2):
    delta1 = temp * random.uniform(-1, 1)
    delta2 = temp * random.uniform(-1, 1)
    xnew =  x1 + delta1
    xprev = x2 + delta2
    val = calc_easom(xnew,xprev)
    return [val,xnew,xprev]



randomPoint = get_random() #x0

for i in range(0,100000):
    randomNew = shift(randomPoint[1],randomPoint[2]) #x1
    if randomPoint[0] > randomNew[0]:
        randomPoint = randomNew

    if randomPoint[0] < randomNew[0]:
        randomPoint = get_probability(randomPoint,randomNew)

    temp = temp*0.995
print(randomPoint)
print(temp)




