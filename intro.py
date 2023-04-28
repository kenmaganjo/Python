# my_name = "Ken Maganjo"
# print(my_name.upper())
# print(my_name.lower())
    
  # take input of basic salary
basic_salary = float(input("Enter your basic salary: "))

# calculate gross salary
gross_salary = basic_salary + (0.1 * basic_salary) + 13500

# calculate NSSF contribution
nssf_rate = 0.06
max_nssfable_salary = 18000
nssf_contribution = min(gross_salary * nssf_rate, max_nssfable_salary)

# print out the results
print("Your gross salary is:", gross_salary)
print("Your NSSF contribution is:", nssf_contribution)

    


