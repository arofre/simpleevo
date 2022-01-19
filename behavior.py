import random
from names import *

def mating(p,female_population,male_population):
    q = random.choice(female_population)
    b = p[1] * 100
    c = q[1] * 100
    if random.randint(0, 100) < b:
        if random.randint(0, 100) < c:
            cgender = random.choice(["Male","Female"])
            if cgender == "Male":
                attr, foodg = 10, 10
                name = random.choice(male_name)

                attr = random.gauss(p[1], 0.1)
                if attr > 1:
                    attr = 1
                if attr < 0:
                    attr = 0
                x = (q[2]+p[2])/2
                foodg = random.gauss(x, 0.1)
                if foodg > 1:
                    foodg = 1
                if foodg < 0:
                    foodg = 0

                male_population.append([name, attr, foodg, "Male"])

            elif cgender == "Female":
                fert, foodg = 10, 10
                name = random.choice(female_name)

                fert = random.gauss(q[1], 0.1)
                if fert > 1:
                    fert = 1
                if fert < 0:
                    fert = 0

                x = (q[2] + p[2]) / 2
                foodg = random.gauss(x, 0.1)
                if foodg > 1:
                    foodg = 1
                if foodg < 0:
                    foodg = 0
                female_population.append([name, fert, foodg, "Female"])


def male_behavior(male_population,female_population):
    for p in male_population:
        a = p[2]*100

        if random.randint(0,100) > a:
            male_population.remove(p)
        else:
            mating(p,female_population,male_population)
    return male_population, female_population

def female_behavior(male_population,female_population):
    for p in female_population:
        a = p[2]*100
        if random.randint(0,100) > a:
            female_population.remove(p)
        else:
            continue
    return male_population, female_population
