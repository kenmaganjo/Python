def calculate_grosss_salary(s, b):
    grosss_salary = s + b
    grosss_salary = round(grosss_salary,2)
    
    return grosss_salary

def calculate_nssf(grosss_salary):
    nssf = 0 
    nssf_rate = 0.06 
    max_deductible_nssf = 18000
    nssf = min((grosss_salary * nssf_rate), max_deductible_nssf)
    nssf = round(nssf,2)

    return nssf

def calculate_nhif(grosss_salary):
    nhif = 0
    nhif = round(nhif,2)
    if grosss_salary < 5999:
        nhif = 150
    else:
        if grosss_salary <= 7999:
            nhif = 300
        else:
            if grosss_salary <= 11999:
                nhif = 400
            else:
                if grosss_salary <= 14999:
                    nhif = 500
                else:
                    if grosss_salary <= 19999:
                        nhif = 600
                    else:
                        if grosss_salary <= 29999:
                            nhif = 750
                        else:
                            if grosss_salary <= 34999:
                                nhif = 900
                            else:
                                if grosss_salary <= 39999:
                                    nhif = 950
                                else:
                                    if grosss_salary <= 44999:
                                        nhif = 1000
                                    else:
                                        if grosss_salary <= 49999:
                                            nhif = 1100
                                        else:
                                            if grosss_salary <= 59999:
                                                nhif = 1200
                                            else:
                                                if grosss_salary <= 69999:
                                                    nhif = 1300
                                                else:
                                                    if grosss_salary <= 79999:
                                                        nhif = 1400
                                                    else:
                                                        if grosss_salary <= 89999:
                                                            nhif = 1500
                                                        else:
                                                            if grosss_salary <= 99999:
                                                                nhif = 1600
                                                            else:
                                                                nhif = 1700
                                                                  
    return nhif

def calculate_taxable_income(grosss_salary):
    taxable_income = 0
    taxable_income = grosss_salary - nssf
    taxable_income = round(taxable_income, 2)

    return taxable_income

def calculate_paye(grosss_salary):
    paye = 0
    
    if taxable_income <= 24000:
        paye = 0.1 * taxable_income
    else:
        if taxable_income <= 32333:
            paye = (0.25 * (taxable_income - 24000)) + 2400
        else:
            paye = (0.3 * (taxable_income - 32333)) + 4483.25

    paye = round(paye, 2)
    
    return paye

def calculate_net_salary(grosss_salary):
    net_salary = grosss_salary - (nhif + nssf + paye)
    net_salary = round(net_salary, 2)

    return net_salary

            

salary = float(input("Enter salary: "))
benefits = float(input("Enter benefits: "))

gs = calculate_grosss_salary(salary, benefits)
nssf = calculate_nssf(gs)
nhif = calculate_nhif(gs)
taxable_income = calculate_taxable_income(gs)
paye = calculate_paye(gs)
net_salary = calculate_net_salary(gs)


print("NHIF =", nhif)
print("NSSF =", nssf)
print("Taxable Income =", taxable_income)
print("PAYE =", paye)
print("Net Salary =", net_salary)






