annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost = float(input('Enter the cost of your dream home: '))

current_savings = 0
annal_return_rate = 0.04
portion_down_payment = 0.25
number_of_months = 0

monthly_salary = annual_salary / 12
down_payment = portion_down_payment * total_cost

while current_savings < down_payment:
    current_savings += monthly_salary * portion_saved + ((current_savings * annal_return_rate) / 12)
    print(current_savings)
    number_of_months += 1

print('Number of months: ', number_of_months)



