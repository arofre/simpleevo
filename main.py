import sys
from gui import *
from create_population import *
from behavior import *
from plot import *

foodlist = []
fertlist = []
attrlist = []
poplist = []


def run(sim):

    for i in range(sim):
        totfood, totattr, totfert = 0, 0, 0
        male_behavior(male_population,female_population)
        female_behavior(male_population,female_population)


        for i in male_population:
            totfood+=i[2]
            totattr+=i[1]

        for y in female_population:
            totfood+=y[2]
            totfert+=y[1]


        total_people = len(male_population)+len(female_population)
        total_females = len(female_population)
        total_males = len(male_population)

        try:
            foodlist.append(totfood/ total_people)
            fertlist.append(totfert / total_females)
            attrlist.append(totattr / total_males)
            poplist.append(total_males+total_females)

        except:
            print("Population died")
            plot(foodlist, fertlist, attrlist, poplist)
            sys.exit()

    print(male_population)
    print(female_population)
    plot(foodlist, fertlist, attrlist, poplist)


    ask = input("Simulate more years, y/n")

    if ask == "y":
        sim = int(input("How many turns"))
        run(sim)
    else:
        print()

if __name__ == '__main__':
    pop, staatr,stafert, foodgat, simu = start_gui()
    simu=int(simu)
    staatr, foodgat, stafert = staatr / 100, foodgat / 100, stafert / 100
    female_population, male_population = crepop(pop, staatr, stafert, foodgat)
    run(simu)

