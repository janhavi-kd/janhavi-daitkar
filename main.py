import TEMPERATURE 
from TEMPERATURE import celsius_to_fahrenhit
from TEMPERATURE import celsius_to_kelvin
from TEMPERATURE import fahrenhit_to_celsius

print("Temperature Conversion Program") 
print("1. Celsius to Fahrenhit") 
print("2. Fahrenhit to Celsius") 
print("3. Celsius to Kelvin") 

choice = int(input("Enter your choice (1-3): ")) 

if choice == 1: 
 c = float(input("Enter temperature in Celsius: ")) 
 result = TEMPERATURE.celsius_to_fahrenhit.convert(c) 
 print("Temperature in Fahrenhit:", result) 

elif choice == 2: 
 f = float(input("Enter temperature in celcius: ")) 
 result = TEMPERATURE.celsius_to_kelvin.convert(f) 
 print("Temperature in kelvin:", result) 
  
elif choice == 3: 
 c = float(input("Enter temperature in fahrenhit: ")) 
 result = TEMPERATURE.fahrenhit_to_celcius.convert(c) 
 print("Temperature in celsius:", result) 

else: 
 print("Invalid choice!") 