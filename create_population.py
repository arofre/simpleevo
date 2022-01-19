from names import *
import random

def crepop(pop,staatr,stafert,foodgat):
    male_population = []
    female_population = []
    hpop=int(pop/2)
    for i in range(hpop):
        attr, foodg = 10, 10
        name = random.choice(male_name)
    #    male_name.remove(name)
        attr = random.gauss(staatr, 0.1)
        if attr > 1:
            attr = 1
        if attr < 0:
            attr = 0

        foodg = random.gauss(foodgat, 0.1)
        if foodg > 1:
            foodg = 1
        if foodg < 0:
            foodg = 0

        male_population.append([name, attr, foodg, "Male"])


    for i in range(hpop):
        fert, foodg = 10, 10
        name = random.choice(female_name)
    #    female_name.remove(name)

        fert = random.gauss(stafert, 0.1)
        if fert > 1:
            fert = 1
        if fert < 0:
            fert = 0

        foodg = random.gauss(foodgat, 0.1)
        if foodg > 1:
            foodg = 1
        if foodg < 0:
            foodg = 0

        female_population.append([name, fert, foodg, "Female"])
    return female_population, male_population