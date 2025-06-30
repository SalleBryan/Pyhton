# Ask the user for the advertised unit
print('Enter TB or GB for the advertised unit:')
# Get the advertised unit
unit = input('>')
# Calculate the amount that the advertised capacity lies:
if unit == 'TB' or unit == 'tb'or unit == 'Tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb' or unit == 'Gb':
    discrepancy = 1000000000 / 1073741824
# Ask the user for the advertised capacity
print('Enter the advertised capacity:')
# Get the advertised capacity
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)
 # Calculate the real capacity, round it to the nearest hundredths,
 # and convert it to a string so it can be concatenated:
real_capacity = str(round(advertised_capacity * discrepancy, 2))
print('The actual capacity is ' + real_capacity + ' ' + unit)