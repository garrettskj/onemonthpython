states = {'NY' : 'New York', 'PA' : 'Pennsylvania', 'CA' : 'California'}

print (states['NY'])

people = ['Mattan', 'Chris']

print (type(states))
print (type(people))

print (states.get('FL', 'Not Found'))
print (states.get('NY', 'Not Found'))

print (states.keys())
print (states.values())

states['FL'] = 'Florida'

print (states)
