# Decalare variable like 'name', 'age', 'job' and companay with values respectively

name = 'Sabir Ansari'
age = 25
job = 'Service Engineer'
company = 'One Click Service'

# Use format() with print() function to access the variable

print('{0} is {1} years old'.format(name, age))
print('{0} works at {1} as a {2}'.format(name, company, job))

# Numbers are optional
print('{} is {} years old'.format(name, age))
print('{} works at {} as a {}'.format(name, company, job))

# We can also name the parameters
print('{name} is {age} years old'.format(name=name, age=age))
print('{name} works at {company} as a {job}'.format(name=name, company=company, job=job))

# We can also use the f strings like belos
print(f'{name} is {age} years old')
print(f'{name} works at {company} as a {job}')
