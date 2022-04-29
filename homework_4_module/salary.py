from sys import argv

script_name, production_in_hours, rate_per_hour, premium = argv

print("Заработная плата = " + str(int(production_in_hours) * int(rate_per_hour) + int(premium)))
