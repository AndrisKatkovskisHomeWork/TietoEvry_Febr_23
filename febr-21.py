my_name = "Andris"
print(f"{my_name} " * 5)

first_string_part = "Ba"
second_string_part = "na" * 5
print(first_string_part + second_string_part)

days = 365
hours_in_year = 24 * days
minutes_in_year = hours_in_year * 60
seconds_in_year = minutes_in_year * 60
print("In 2022 year is", seconds_in_year, "seconds")

print("10**100 is", 10 ** 100)
print()

increase = 6
deposited_amount = 1000
total_deposit_term = 12

print("if you invest ", deposited_amount, "Eur",
      "for", total_deposit_term, "years",
      " with yearly interest ", increase, "%",
      ", then you will earn: ")

deposited_amount = (deposited_amount * (increase / 100) + deposited_amount)
print("after 1 year deposited_amount", '{0:.2f}'.format(deposited_amount))
deposited_amount = (deposited_amount * (increase / 100) + deposited_amount)
print("after 2 years deposited_amount", '{0:.2f}'.format(deposited_amount))
deposited_amount = (deposited_amount * (increase / 100) + deposited_amount)
print("after 3 years deposited_amount", '{0:.2f}'.format(deposited_amount))
deposited_amount = (deposited_amount * (increase / 100) + deposited_amount)
print("after 4 years deposited_amount", '{0:.2f}'.format(deposited_amount))
deposited_amount = (deposited_amount * (increase / 100) + deposited_amount)
print("after 5 years deposited_amount", '{0:.2f}'.format(deposited_amount))
deposited_amount = (deposited_amount * (increase / 100) + deposited_amount)
print("after 6 years deposited_amount", '{0:.2f}'.format(deposited_amount))
deposited_amount = (deposited_amount * (increase / 100) + deposited_amount)
print("after 7 years deposited_amount", '{0:.2f}'.format(deposited_amount))
deposited_amount = (deposited_amount * (increase / 100) + deposited_amount)
print("after 8 years deposited_amount", '{0:.2f}'.format(deposited_amount))
deposited_amount = (deposited_amount * (increase / 100) + deposited_amount)
print("after 9 years deposited_amount", '{0:.2f}'.format(deposited_amount))
deposited_amount = (deposited_amount * (increase / 100) + deposited_amount)
print("after 10 years deposited_amount", '{0:.2f}'.format(deposited_amount))
deposited_amount = (deposited_amount * (increase / 100) + deposited_amount)
print("after 11 years deposited_amount", '{0:.2f}'.format(deposited_amount))
deposited_amount = (deposited_amount * (increase / 100) + deposited_amount)
print("after 12 years deposited_amount", '{0:.2f}'.format(deposited_amount))
