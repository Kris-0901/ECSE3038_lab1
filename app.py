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

