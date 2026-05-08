alien_0 = {'color': 'green', 'point': '5'}

print(alien_0['color'])
print(alien_0['point'])

print("List dictinary")
print(alien_0)
# Add new object
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print("List dictinary after add 2 key")
print(alien_0)

print('Add speed alien')
alien_0['speed']= 'medium'
print(alien_0)

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #So fast
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New Position: {alien_0['x_position']}")

