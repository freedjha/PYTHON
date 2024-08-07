# 2. Write a python program using function to convert Celsius to Fahrenheit.

#°C × (9/5) + 32 = °F

def temp():
    Celsius = float(input("Enter temp in celcius"))
    Fahrenheit =  (Celsius * (9/5) + 32)
    print(f"Temprature in Farenheit: {Fahrenheit}",  end="")

    
    

temp()