def calculate_nhif(salary, benefits):
    salary = float(input("Enter salary: "))
    benefits = float(input("Enter benefits: "))
    grosss_salary = salary + benefits
    # nhif = calculate_nhif("salary", "benefits")
    # return (nhif)

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
                                                                
                                                                

    return (nhif)
nhif = calculate_nhif("salary", "benefits")
print("NHIF =", nhif)

    # ans:
    #     Enter salary: 5000.50
    #     Enter benefits: 450.20
    #     NHIF = 150

    #     Enter salary: 86450
    #     Enter benefits: 2150.65
    #     NHIF = 1500

    #     Enter salary: 115000
    #     Enter benefits: 9565.33
    #     NHIF = 1700




