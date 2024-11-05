"""In this code I created a code which can be used to
add or remove energy from sources such as solar, hydro and wind.
I also created a button to view statistics and messageboxes
for users to view how much energy they have added or removed.
As well as creating error messageboxes for error handling."""


import random #Imported random values for city demand
import tkinter as tk #For GUI
from tkinter import messagebox #For users to view notifications


city_demand = random.uniform(77, 1000)
#Random values for city demand between these numbers

"""Created a class and variables within"""
class EnergySources():
    """To manage the sources and energy production total"""
    def __init__(self, name):
        self.name = name
        #Dictinary to manage energy levels
        self.energy_sources = {
            "hydro": 0.0, 
            "solar": 0.0,
            "wind": 0.0
        }
        self.total_energy = 0.0 #Total energy produced


    def calculate_total_energy(self):
        """Calculates total energy input across all sources"""
        self.total_energy = sum(self.energy_sources.values())


    def add_energy(self, source, amount):
        """Adds energy to sources"""
        if source in self.energy_sources:
            self.energy_sources[source] += amount
            self.calculate_total_energy()


    def remove_energy(self, source):
        """removes energy from sources"""
        if source in self.energy_sources:
            self.energy_sources[source] = 0.0 #Resets to 0 energy
            self.calculate_total_energy() #updates total energy

#Instance for EnergySources class
energy_sources = EnergySources("City Power Plant")


def add_energy():
    """MAnages the addition of enrgy to sources"""
    source = source_var.get() #Gets the selected source
    try:
        amount = float(energy_entry.get())
        if amount < 0:
            messagebox.showerror\
            ("Error found", "Please enter a positive number.")
            #Error if the number input is below 0
            return
        energy_sources.add_energy(source, amount)
        update_total_energy()
        #Adds energy and updates the total
        if energy_sources.total_energy > city_demand:
            #checks if energy is higher than demans
            excess_energy = energy_sources.total_energy - city_demand
            #calcuates the excess energy
            messagebox.showinfo("Excess energy", f"Energy exceeds \
                                demand by: {excess_energy:.2f} MW.")
            #Error message if exceeds demand
        messagebox.showinfo\
            ("Success", f"Added {amount} MW to {source}.")
        #Displays info box of amount added to chosen source
    except ValueError:
        messagebox.showerror\
            ("Error found", "Please enter a valid number")
        #Makes sure the input is a number


def remove_energy():
    """Manages the removal of energy"""
    source = source_var.get() #Gets the source
    try:
        amount = float(energy_entry.get()) #Converts to float
        if amount <0:
            messagebox.showerror\
                ("Error found", "Please enter a positive number")
            #Error message if amount is below 0
            return
        if energy_sources.energy_sources[source] < amount:
            messagebox.showerror\
                ("Error found", "Not enough energy to remove")
            #Not enough energy to be removed will show an error
            return
        energy_sources.energy_sources[source] -= amount #Removes energy
        energy_sources.calculate_total_energy()
        update_total_energy() #Updates the total
        messagebox.showinfo\
            ("Success", f"Removed {amount} MW from {source}.")
        #User gets info about amount added to source
    except ValueError:
        messagebox.showerror\
            ("Error found", "Please enter valid number")
        #Error box to prompt user to enter valid number


def update_total_energy():
    """Updates the displayed energy from each source"""
    global total_energy
    total_energy = energy_sources.total_energy #Update global energy
    check_energy_vs_demand() #Checks for city demand
    total_label.config\
        (text= f"Total energy produced is:\
         {energy_sources.total_energy:.2f} MW.")
    #displays total energy produced
    hydro_label.config (text= f"Hydro:\
                        {energy_sources.energy_sources['hydro']:.2f} MW.")
    #Displays energy produced from hydroelectric power
    solar_label.config (text= f"Solar:\
                        {energy_sources.energy_sources['solar']:.2f} MW.")
    #Displays energy from solar pannels
    wind_label.config (text = f"Wind:\
                       {energy_sources. energy_sources['wind']:.2f} MW.")
    #Displays energy made from wind turbines


def check_energy_vs_demand():
    """Checks the total energy and the city energy demand"""
    if total_energy >= city_demand:
        #checks if total energy is higher than demand
        messagebox.showerror= f"Energy meets city demand. Excess\
            energy is above by:{total_energy - city_demand: .2f} MW."
        #Error box for excess energy whilst calculating the excess
    else:
        messagebox.showerror= f"Energy doesn't meet demand. Short by\
            {city_demand - total_energy:.2f} Mw."
        #error box for shortfall of energy and calculates it
    demand_label.config(text = f"City demand: {city_demand:.2f} MW.")
    #Users to view the city demand


def view_energy_statistics():
    """Allows users to view each sources' energy produced"""
    stats = (
        f"Hydro: {energy_sources.energy_sources['hydro']} MW\n"
        f"Solar: {energy_sources.energy_sources['solar']} MW\n"
        f"wind: {energy_sources.energy_sources['wind']} MW\n"
        f"Total energy produced: {energy_sources.total_energy:.2f} MW\n"
        f"City demand:{city_demand:.2f} MW"
    )
    messagebox.showinfo("Energy Statistics", stats)
    #Shows the user the statistics

#Creates the main window for program
root = tk.Tk()
root.title("Energy Distribution System!")
root.geometry("450x400")

#Menu for users to select their choice
source_var = tk.StringVar(value="hydro")
source_menu = tk.OptionMenu(root, source_var, "hydro", "solar", "wind")
source_menu.pack(pady=7)

#Field for users to add or remove amount of energy from sources
energy_entry = tk.Entry(root)
energy_entry.pack(pady=7)

#Buttons for user to interact if they want to add energy
add_button= tk.Button(root, text="Add Energy", command=add_energy)
add_button.pack(pady=7)

#Button to allow user to remove energy
remove_button = tk.Button(root, text= "Remove Energy",\
                           command=remove_energy)
remove_button.pack(pady=7)

#Alloes users to view statistics
view_button = tk.Button(root, text="View energy statistics",\
                         command= view_energy_statistics)
view_button.pack(pady=7)

#Displays the energy for solar pannels
solar_label = tk.Label(root, text = "Solar: 0.0 MW")
solar_label.pack()

#Displays the energy for hydroelectric power
hydro_label = tk.Label(root, text="Hydro: 0.0 MW")
hydro_label.pack()

#Displays the energy for wind turbines
wind_label = tk.Label(root, text= "Wind: 0.0 MW")
wind_label.pack()

#Shows the user the city energy demand
demand_label= tk.Label(root, text=f"The city demand is:\
 {city_demand:.2f} MW.")
demand_label.pack()

#Displays total energy produced
total_label = tk.Label(root, text="Total energy produced is 0.00 MW")
total_label.pack()

#Event loop to run Tkinter
if __name__ == "__main__":
    root.mainloop()
