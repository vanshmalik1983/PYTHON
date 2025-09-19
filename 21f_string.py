letter= "Hey my name is {1} and I am from {0}"
country= "India" 
name = "Vansh" 

print(letter.format(country , name ))
print(f" Hey my name is {name} and I am from {country}")
#if {} use then use as a string and if not then replace value
print(f"W use F-string like this : hey my name is {{name}} I am from {{country}}") 

price = 64.8548
txt = f"for only {price:.2f} dollars!"
print(txt)

