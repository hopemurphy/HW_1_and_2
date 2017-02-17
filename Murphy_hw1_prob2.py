#Hope Murphy created 2/6/17

from math import pi

G=6.67*10**(-11)  #in m^3/kgs^2
M=5.97*10**24     #in kg
R=6371            #in km  (need to convert to m)

T= int(input("Enter the desired value for T (in s):"))	

h=(G*M*(T**2)/(4*((pi)**2)))**(1/3) - R*10**3

print("The altitude in meters is:",h)