# ECSE3038_lab1 

 ## Summary

### Function 1: 

This functions accepts a variable of type 'list' with resistance values and returns a variable of type 'float' with the total resistance in a parallel. It also will print the result to the terminal. 

   *parallel(parallel_resistors_in_circuit:list) -> float*

**Eg.**  

    parallel([100,200])  

#### Expected output: 
```
Parallel resistors in circuit: [330, 1000, 2200] ohms

The total parallel resistance is: 222.973 ohms

```      
**OR** 

    circuit_resistance = parallel([100,200])

### Function 2: 

This function accepts a variable of type 'float' with the voltage supply value and a variable of 
type 'list' with the seires resistor values in a voltage divider circuit. 

The function then calculates the overall current using I=V/R. 
Where R is the total series resistance. The total current is then used to determine 
the voltage drop accross each resistor using V=IR. 

The fucntion will output a summary of voltage divider circuit  along with a list of dictionaries with 
the resistor/resistance values and their corresponding voltage drops. 

   *potential_divider(voltage_supply_value: float,series_resistor_values: list) -> list*

**Eg.**  

    potential_divider(9, [3000, 1000])  
         
**OR** 

    resistors_and_voltage_drops = potential_divider(9, [3000, 1000])

### Function 3: 


## Purpose 

This code was written to fulfill the course requirements of **'ECSE3038 Engineering Internet of Things Systems'** and to learn the Python programming language.  

## A Short Joke 

*Jason Todd walks into a bar, where the Joker is behind the counter. 
He says "Jason, you know I can't serve Robins here"
Jason asks "Why?" 
and Joker replies "this is a CROW bar!"*





