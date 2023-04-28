capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}

print("Italy" in capital_city.keys())   .................to check if a key is available in the dictionary
print("Rome" in capital_city.values())  ..................to check if a vale is available in the dictionary
del capital_city["Nepal"] .................................to remove an element from the dictionary
print(capital_city)
print(capital_city["Italy"]) ...............................to access a value in the dictionary
capital_city["Italy"] = "Vatican"  ......................  to change a value in the dictionary
print(capital_city)
capital_city["Germany"] = "Munich" ..........................to add an element in a dictionary
print(capital_city)