contry_to_capital = { 'UK': 'London', 'Malaysia': 'KL', 'Morocco': 'Rabat'}

capital_to_county = { capital: country for country, capital in contry_to_capital.items()}

from pprint import pprint as pp
pp(capital_to_county)

# dict.items() to get keys and values from dict 

words = ['hi', "bye", "chao"]
print({x[0]: x for x in words})