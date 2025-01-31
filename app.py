"ID# 620138053"



"""
1. Write a function, `parallel()`, that, when called, prints the effective resistance of a network of resistors 
connected in parallel. The function should be able to accept a single **list** as argument.
    
    Use the example provided below to test the functionality of your function. ie, 
    copy the line below into your python script to call the function you wrote. 
    
    ```python
    parallel([330, 1000, 2200])
    ```
    
    Your script should print the following:
    
    ```python
    "222.973 ohms"
    ```
    

(5 marks)
"""
print("")
print("")
print("1.")
print("")
# This functions accepts a list of resistance values and returns a float with total resistance in a parallel  

def parallel(parallel_resistors_in_circuit:list) -> float:
    total_resistance=0
    for value in parallel_resistors_in_circuit:
        total_resistance+=(1/value)
    total_resistance=1/total_resistance
    print("Parallel resistors in circuit: " + str(parallel_resistors_in_circuit)+" ohms")
    print("")
    print("The total parallel resistance is: "+ str(f"{total_resistance:.3f}") +" ohms")
    return total_resistance


parallel([330, 1000, 2200])

## circuit_resistance = parallel([330, 1000, 2200])

print("")
print("")
print("2.")
print("")
"""
2. Write a function, potential_divider(), that takes two values as argument: a number 
that represents a voltage supply value, and a list of numbers that represent 
resistance values of resistors connected in series. The function should output the voltage drop across 
each resistor in your resistor list. The function should be able to accept a list of any length.
eg. 
> potential_divider(9, [3000, 1000])
> "6.75v"
> "2.25v" 
"""

# This function accepts a variable of type float with the voltage supply value and a variable of 
# type list with the seires resistor values in a voltage divider circuit. 
# 
# The function then calculates the overall current using I=V/R. 
# Where R is the total series resistance. The total current is then used to determine 
# the voltage drop accross each resistor using V=IR. The fucntion will output a summary of 
# voltage divider circuit  along with a list of dictionaries with 
# the resistor/resistance values and their corresponding voltage drops 

def potential_divider(voltage_supply_value:float,series_resistor_values:list) -> list:
    total_resistance=0
    current=0.00
    voltage_drops=[]
   

    for resistance_value in series_resistor_values:
        total_resistance+=resistance_value

    current=voltage_supply_value/total_resistance


    for resistance_value in series_resistor_values:
        voltage_drops.append({"resistance":str(resistance_value) +
                              " ohms","voltage_drop":str(round(current*resistance_value,2))+ "v"})


    print ("SUMMARY:")
    print("")
    print("A voltage divider circuit has a power supply of "+str(voltage_supply_value)+"v")
    print ("The resistors in series are as follows: "+str(series_resistor_values)+"ohms")
    print("The total current in the circuit is "+str(current)+"A")
    print("")
    print("The voltage drops across each resistor are as follows: ")
    print("")    
    i=0
    for dictionaries in voltage_drops:
        print(voltage_drops[i])
        i+=1
    
    return voltage_drops

potential_divider(9, [3000, 1000])

#resistors_and_voltage_drops=potential_divider(9, [3000, 1000])

print("")
print("")
print("3.")
print("")

"""
3. Write a function, temperature_check(), that accepts a single number, a patient's body 
temperature, and a single character, the unit of temperature. The function should output whether 
the patient is hypothermic, hyperthermic or has normal body temperature based on the number passed to the function. 
The second value passed as argument should tell the function whether the 
condition should calculated in degrees celcius or degrees fahrenheit.
An appropriate message should be written to the screen with the result. 
You’re free to use what ever reasonable temperature limits you feel will adequately act as boundaries for these conditions.
eg. 
> temperature_check(14, "C")
> "the patient is hypothermic"

> temperature_check(37, "C")
> "the patient's temperature is normal"

> temperature_check(37, "F")
> "the patient is hypothermic"
"""
#This function accepts a variable of type 'flaot' as the patient's temperature and a variable of type 'chr' 
# ('C' or 'F') as the temperature unit. It then uses predefined upper and lower threshhold in both fareheit and 
# celcius to determine if the patient is hypothermic, hyperthermic or has normal body temperature. 
# The result is then output. The function also employs error checking for incorrect temperature unit and 
# returns an error statement.   

def temperature_check(patient_temperature:float,temperature_unit:str):
    
    if (temperature_unit.upper() =="C"):
        lower_threshold= 34.4
        upper_threshold=37.6
        if (patient_temperature<lower_threshold):
           print("The patient's temperature, '" +str(patient_temperature)+ "' C is hypothermic")
        elif(patient_temperature>upper_threshold):
            print("The patient's temperature, '" +str(patient_temperature)+ "' C is hyperthermic")
        else:
            print("the patient's temperature, '" +str(patient_temperature)+ "' C is normal")
    elif(temperature_unit.upper() =="F"):
        lower_threshold= 94.0
        upper_threshold=99.7
        if (patient_temperature<lower_threshold):
            print("The patient's temperature, '" +str(patient_temperature)+ "' F is hypothermic")
        elif(patient_temperature>upper_threshold):
            print("The patient's temperature, '" +str(patient_temperature)+ "' F is hyperthermic")
        else:
            print("the patient's temperature, '" +str(patient_temperature)+ "' F is normal")
    else:
     print("Invalid unit. Please enter 'C' or 'F' as temperature unit")
     return 



temperature_check(99.7,"C")
temperature_check(99.7,"F")

temperature_check(37.6,"C")
temperature_check(37.6,"F")

print("")
print("Error Return Statement:")

temperature_check(37.6,"A") # example of invalid return statement

print("")



