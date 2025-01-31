 # Summary




### Function 1: 

This functions accepts a variable of type 'list' with resistance values and returns a variable of type 'float' with the total resistance in a parallel. It also will print the result to the terminal. 

   *parallel(parallel_resistors_in_circuit:list) -> float*

**Eg.**  

    parallel([100,200])  

**Expected output:** 
```
Parallel resistors in circuit: [330, 1000, 2200] ohms

The total parallel resistance is: 222.973 ohms

```      
**OR** store in new variable

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

**Expected output:**
```
SUMMARY:

A voltage divider circuit has a power supply of 9v
The resistors in series are as follows: [3000, 1000]ohms
The total current in the circuit is 0.00225A

The voltage drops across each resistor are as follows:

{'resistance': '3000 ohms', 'voltage_drop': '6.75v'}
{'resistance': '1000 ohms', 'voltage_drop': '2.25v'}

```   

         
**OR** store in new variable

    resistors_and_voltage_drops = potential_divider(9, [3000, 1000])


    

### Function 3: 

This function accepts a variable of type 'flaot' as the patient's temperature and a variable of type 'str' 
('C' or 'F') as the temperature unit. It then uses predefined upper and lower threshholds in both farenheit and 
celcius to determine if the patient is hypothermic, hyperthermic or has normal body temperature. 
The result is then output. The function also employs error checking for incorrect temperature unit and 
returns an error statement.  

   *temperature_check(patient_temperature: float,temperature_unit: str) -> None*

**Eg.**  
```
    temperature_check(99.7,"C")
    temperature_check(99.7,"F")

    temperature_check(37.6,"C")
    temperature_check(37.6,"F")

    print("")
    print("Error Return Statement:")

    temperature_check(37.6,"A") # example of invalid return statement
```
**Expected output:** 
```
The patient's temperature, '99.7' C is hyperthermic
the patient's temperature, '99.7' F is normal
the patient's temperature, '37.6' C is normal
The patient's temperature, '37.6' F is hypothermic

Error Return Statement:
Invalid unit. Please enter 'C' or 'F' as temperature unit

```      

# Purpose 

This code was written to fulfill the course requirements of **'ECSE3038 Engineering Internet of Things Systems'** and to learn the Python programming language.  

# A Short Joke 

*Jason Todd walks into a bar, where the Joker is behind the counter. 
He says "Jason, you know I can't serve Robins here"
Jason asks "Why?" 
and Joker replies "this is a CROW bar!"*





