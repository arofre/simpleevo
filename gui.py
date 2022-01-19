from tkinter import *

msg = ("This is Evolution simulator 0.1. Start the simulation by using the sliders to set the values. Population size is the initial amount of agents. Standard attractiveness is the average chance for male agents to make a female agent reproduce. Standard fertility is the chance the a females offspring is born successfully. Food gathering efficiency is the chance that an agent is able to find food for the round. During one round every agent has to find food or they will die. After that the male agents will try to find a female willing to reproduce. If the agent is successful and the offpsring survives, a new agent is born with stats based on its parents. After all the rounds are done graphs will show relevant stats for the simulation. After closing the graph windows you will be asked in the console to continue the simulation if you so wish. Be careful with the amount of rounds you choose as the exponential growth of the population will make it take longer. If the simulation won't start this could be the problem. Simply restart the program and choose less years.")

def popupmsg():
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=msg, wraplength=400, justify=LEFT)
    label.grid(padx=100, pady=10)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()

def start_gui():
    window = Tk()
    window.title("Evolution Simulation")

    window.geometry('400x300')



    lbl = Label(window, text="EvoSim 0.1", font=("Arial Bold", 20))
    lbl.grid(column=0, row=0)

    pop = Scale(window, from_=0, to=100, orient=HORIZONTAL)
    pop.grid(column=1, row=2)
    poplbl = Label(window, text="Population size:")
    poplbl.grid(column=0, row=2)

    staatr = Scale(window, from_=0, to=100, orient=HORIZONTAL)
    staatr.grid(column=1, row=4)
    staatrbl = Label(window, text="Standard attractiveness(%):")
    staatrbl.grid(column=0, row=4)

    stafert = Scale(window, from_=0, to=100, orient=HORIZONTAL)
    stafert.grid(column=1, row=6)
    stafertbl = Label(window, text="Standard fertility(%):")
    stafertbl.grid(column=0, row=6)

    foodgat = Scale(window, from_=0, to=100, orient=HORIZONTAL)
    foodgat.grid(column=1, row=8)
    foodgatbl = Label(window, text="Food gathering efficiency(%):")
    foodgatbl.grid(column=0, row=8)

    simu = Entry(window,width=10)
    simu.grid(column=1, row=10)
    simubl = Label(window, text="How many simulations:")
    simubl.grid(column=0, row=10)

    btn = Button(window, text="Run", command=lambda: window.quit())
    btn.grid(column=2, row=12)

    btn = Button(window, text="Help", command= lambda: popupmsg())
    btn.grid(column=1, row=12)

    window.mainloop()

    return pop.get(), staatr.get(), stafert.get() ,foodgat.get(), simu.get()