salary = float(input("Enter salary: "))
benefits = float(input("Enter benefits: "))
grosss_salary = salary + benefits
print('Gross salary =', grosss_salary)


nssf_rate = 0.06
max_deductible_nssf = 18000
nssf = min(grosss_salary * nssf_rate, max_deductible_nssf)

taxable_income = grosss_salary - nssf

        paye = 2400 + 0.25 * (taxable_income - 24000)
    else:if taxable_income <= 24000:
    paye = 0.1 * taxable_income
if taxable_income > 32333:
    paye = 0.3 *(taxable_income - 32333)
else:
    if taxable_income <= 32333:
        paye = 0.3 * (taxable_income - 32333) +2400

if grosss_salary < 5999:
    print('NHIF=',150)
    print('NSSF =', nssf)
    print('PAYE =', paye)
else:
    if grosss_salary <= 7999:
        print('NHIF=',300)
        print('NSSF =', nssf)
        print('PAYE =', paye)
    else:
        if grosss_salary <= 11999:
            print('NHIF=',400)
            print('NSSF =', nssf)
            print('PAYE =', paye)
        else:
            if grosss_salary >= 12000 and grosss_salary <= 14999:
                print('NHIF=',500)
                print('NSSF =', nssf)
                print('PAYE =', paye)
            else:
                if grosss_salary >= 15000 and grosss_salary <= 19999:
                    print('NHIF=',600)
                    print('NSSF =', nssf)
                    print('PAYE =', paye)
                else:
                    if grosss_salary >= 20000 and grosss_salary <= 29999:
                        print('NHIF=',750)
                        print('NSSF =', nssf)
                        print('PAYE =', paye)
                    else:
                        if grosss_salary >= 30000 and grosss_salary <= 34999:
                            print('NHIF=',900)
                            print('NSSF =', nssf)
                            print('PAYE =', paye)
                        else:
                            if grosss_salary >= 35000 and grosss_salary <= 39999:
                                print('NHIF=',950)
                                print('NSSF =', nssf)
                                print('PAYE =', paye)
                            else:
                                if grosss_salary >= 40000 and grosss_salary <= 44999:
                                    print('NHIF=',1000)
                                    print('NSSF =', nssf)
                                    print('PAYE =', paye)
                                else:
                                    if grosss_salary >= 45000 and grosss_salary <= 49999:
                                        print('NHIF=',1100)
                                        print('NSSF =', nssf)
                                        print('PAYE =', paye)
                                    else:
                                        if grosss_salary >= 50000 and grosss_salary <= 59999:
                                            print('NHIF=',1200)
                                            print('NSSF =', nssf)
                                            print('PAYE =', paye)
                                        else:
                                            if grosss_salary >= 60000 and grosss_salary <= 69999:
                                                print('NHIF=',1300)
                                                print('NSSF =', nssf)
                                                print('PAYE =', paye)
                                            else:
                                                if grosss_salary >= 70000 and grosss_salary <= 79999:
                                                    print('NHIF=',1400)
                                                    print('NSSF =', nssf)
                                                    print('PAYE =', paye)
                                                else:
                                                    if grosss_salary >= 80000 and grosss_salary <= 89999:
                                                        print('NHIF=', 1500)
                                                        print('NSSF =', nssf)
                                                        print('PAYE =', paye)
                                                    else:
                                                        if grosss_salary >= 90000 and grosss_salary <= 99999:
                                                            print('NHIF=', 1600)
                                                            print('NSSF =', nssf)
                                                            print('PAYE =', paye)
                                                        else:
                                                            if grosss_salary >= 100000:
                                                                print('NHIF=', 1700)
                                                                print('NSSF =', nssf)
                                                                print('PAYE =', paye)
                                                            
                                        # ans:
                                        #     Enter salary: 75000
                                        #     Enter benefits: 5600
                                        #     Gross salary = 80600.0
                                        #     NHIF= 1500
                                        #     NSSF = 4836.

                                        #     Enter salary: 500000
                                        #     Enter benefits: 4562
                                        #     Gross salary = 504562.0
                                        #     NHIF= 1700
                                        #     NSSF = 18000
                                            



