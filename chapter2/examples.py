'''
 range() produces values from 0 to minus one of the value
'''

for i in range(5):
    print(i)

# Print a rectangle of stars
for i in range(6):
    print('*'*15)

# Print triangle of stars
for i in range(10):
    times = i+1
    print('*'*times)

# Print inverted triangle stars
for i in range(10, 0, -1):
    times = i+1
    print('*'*times)