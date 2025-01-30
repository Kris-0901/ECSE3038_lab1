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

# This functions accepts a list of resistance values and returns a float with total resistance in a parallel  

def parallel(parallel_resistors_in_circuit:list) -> float:
    total_resistance=0
    for value in parallel_resistors_in_circuit:
        total_resistance+=(1/value)
    total_resistance=1/total_resistance
    print("Parallel resistors in circuit: " + str(parallel_resistors_in_circuit))
    print("")
    print("The total parallel resistance is: "+ str(f"{total_resistance:.3f}") +" ohms")
    return total_resistance


parallel([330, 1000, 2200])

## circuit_resistance = parallel([330, 1000, 2200])