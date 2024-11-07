07/11/2024
StudentID - 24002821
Version 1

In this file I will be going through the process taken to create the program and explain the steps I decided to take and why.
My program is a simple to navigate and use program, it contains buttons, a menu consisting of hydro, solar and wind that users can choose from, 
a field for users to enter their values, 3 buttons, to add, remove and view statistics as well as displaying it. It contains object oriented programming, 
event driven programming and procedural programming.

I used Visual Studio Code to implement my code and used python language, the version 2024.18.0 and interpreter 3.12.64-bit to write the code. 
I had also used the python debugging tool version 2024.12.0.

I started by importing random values in numbers to implement the city demand later on. 
I have also imported Tkinter as tk for the GUi and from Tkinter I have also imported messagebox which will allow error
or information boxes to appear to the user.

The next step I took was creating the city demand by calling random.uniform to help me get a random value between my chosen number 77 and 1000. 
Which will give me a float number between the chosen values. I chose random.uniform as I thought it worked best with the vision I had in mind; 
as it will provide a value between my chosen values as a float.

I then created the class EnergySources to manage the sources and energy production and also created a dictionary 
for the energy sources hydro (hydroelectric power), solar (solar panells) and wind (wind turbines) which are all set to 0.0 MW 
in the beginning allowing them to be recalculated and modified later on. I have done this to ensure easier modification of the values and updates. 
The total energy is also set to 0.0MW to allow the value to be updated and changed. 

I defined the calculation of total energy to make sure energy from all energy sources is summed from all energy sources values input. 

I also defined the addition of energy which allows users to add energy to the chosen source, 
it  gets the source and adds the amount then, calculating the total energy.

I also defined the removal of energy which allows users to remove energy from the chosen source. 
This resets the to 0 energy and updates the total energy.

I then created an instance called energy_sources for the class EnergySources to allow it to be used within my code and call the variables needed.

I defined the addition of energy which will manage the addition of energy across all the sources. 
Firstly, this will get the selected source from the user and will try to get the amount from the user. 
I used try as an error handling measure to ensure the amount is correct and valid, allowing it to be tried for an error and ensuring it works.
If the amount input by the user is below 0, then the program will show an error message and inform the user there has been an error found, 
and tell them to enter a positive number and return the value. Then, it gets the source and adds the amount and updates the total energy. 
If the energy is higher than demand then there will be excess energy calculated by getting the energy sources and total energy - city demand 
then the user will get an info box telling them how much excess energy there is. Otherwise, there will be an info box, 
telling the user how much energy has been added to their chosen source. Except for a value error to ensure valid input from the user, 
the user will be shown an error box informing them to enter a valid number. This makes sure that the user enters a valid input.

I then implemented the removal of energy which manages how energy is removed from the sources. This is similar to addition,
but applies to the removal of energy. It gets the source chosen, it then tries to get the amount from the user, if the user enters a value below 0,
then the program will show an error and tell the user to input a positive value and returns back to trying to get the amount.
If the amount in the energy source selected is smaller than the amount the user wants to remove then the program will show an error message 
telling the user that there is not enough energy available to be removed. Otherwise, if energy in energy sources in the chosen source 
is equal or smaller then energy will be removed from the chosen source which will then calculate the total energy and update it; 
showing the user an info box telling them how much energy has been removed from the selected source. Except, a value error to make sure the user 
enters a valid input, showing an error box with a message to enter a valid number. 

I then implemented the updating of total energy, this updates the total energy from each source which is then able to be displayed. 
I called global total energy as it allowed me to use it outside of the class created which allowed me to change the value outside of the scope. 
I then took the total energy and updated it by taking the energy sources and their energy which updates the total. 
I also checked for the city demand by implementing check energy vs demand, and then created the total label configuration by getting the 
energy sources and total energy as a float to 2 decimal places. 
I also did this for all energy sources, hydro, solar and wind. This helped me update and display the total energy produced as well as each sources’ energy.

I then defined the check energy vs demand to help me determine if energy meets demand or if there is a shortfall. 
I did this by checking if the total energy is greater than or equal to the city demand which will show the user a box telling them that 
the energy does meet the city demand and the excess energy is above by calculating the total energy - city demand as a float to 2 decimal places. 
This is an error handling to ensure that the user is notified if the energy surpassed the demand or not. The excess can be 0.0 or other value. 
If the energy does not meet the demand, an error box will pop up, informing the user that the energy does not meet demand 
and it is short of calculating the city demand - total energy as a float to 2 decimal places. 
This ensures the user is aware of the energy and handles the city demand and the total energy. 
Then I implemented the demand label configuration for the users to be able to view the city demand of energy. 

I lastly defined the viewing of energy statistics by creating the stats of each energy source as well as the 
total energy produced and the city’s demand of energy. This has been implemented by getting the energy sources variables 
from EnergySources and the energy sources variables from the dictionary as strings and floats. For the total energy produced 
I called on the variables energy sources and the total energy as a float to 2 decimal places and demand by calling on the 
city demand as a float to 2 decimal places. 

I then created the event driven part of the programming which is the GUI implementing Tkinter and created the title of the main
window program and the size of it. I created a menu of 3 drop down selections which users can choose from which contain hydro, solar and wind.
I then made the field of entry which users can use to enter values from. Followed by an addition button that users can click after they input a 
value in the field entry and click the button to add; I also made a remove button which allows the user to remove energy through the same process as addition. 
Entering a value in the entry field can be either added or removed depending on the user’s choice. A view energy statistics button is also 
available to the user to allow them to view the statistics of energy. I also added the stats below the buttons which displays the energy for solar,
hydro and wind, as well as the city demand and the total energy produced. I then looped the whole program and ensured it ran smoothly by conducting a 
debugging process through python debugger to ensure the program works well. 


![EcoSmartCity (IDE debugging) (1)](https://github.com/user-attachments/assets/345e3e94-6fbd-46d3-85da-0da6e7b86282)
![EcoSmartCity (IDE debugging) (2)](https://github.com/user-attachments/assets/8194d2fa-ebaf-4d23-90c0-28ff503291c6)
![EcoSmartCity (IDE debugging) (3)](https://github.com/user-attachments/assets/2d7db2ce-ce3e-4634-9ed5-cecf0a006c39)
![EcoSmartCity (IDE debugging) (4)](https://github.com/user-attachments/assets/52b28442-d9c5-4cb5-b17b-80c1b67f4374)
![EcoSmartCity (IDE debugging) (5)](https://github.com/user-attachments/assets/bca43715-7054-4065-97b6-27243b345a3e)


In these images you can see my debugging process and the usage of IDE. 
I used python debugger to debug my code ensuring it runs smoothly and visual studio code to implement my code. 

Throughout my code I used Object Oriented programming though encapsulation which is proved from the class keeping the 
energy sources and total energy as attributes but they can be interacted with and abstraction being used through the addition of 
energy and calculating total energy which hide unnecessary information from the user whilst being able to offer a clean easy to use interface.

I have also used procedural programming in my code, for example the add_energy, remove_energy, update_total_energy and check_energy_vs_demand 
all perform specific tasks in a procedural way through a step by step process whilst operating on shared data (energy sources, energy) 
which are outside of the class providing an organised way to handle the tasks specified within the program. 

Event driven programming is shown through the use of Tkinter GUI library. 
When a button is pressed an action happens for example viewing stats, adding or removing information or choosing 
the source which proves usage as the user is able to control the way they use the program and how they wish to use it.

In my code I have stuck to PEP 8 python standards to ensure that it is easy to read 
and understand as I also added comments through my code to ensure anyone can understand the program. 
The indentations make it easier to understand the lines of code, where they start and where they end. 
It also just improves the code visually, pleasant to look at and easier to follow making it quickly readable. 
People sticking to PEP 8 standards can also easily read and collaborate on this code which makes collaboration easier and simpler. 

In my repository, I have a main folder called 24002821_EcoSmartCity with a file called preface which welcomes into the folde; 
a subfolder called source code with my code which is called energy_distribution.py; a subfolder with documentation which contains Eco Smart City Algorithm.pdf 
and flowchart_EcoSmartCity.png and a subfolder called screenshots which includes EcoSmartCity (IDE&debugging) (1).png, 
EcoSmartCity (IDE&debugging) (2).png, EcoSmartCity (IDE&debugging) (3).png, EcoSmartCity (IDE&debugging) (3).png, EcoSmartCity (IDE&debugging) (4).png 
and EcoSmartCity (IDE&debugging) (5).png


StudentID 24002821
