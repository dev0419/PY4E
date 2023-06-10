'''x = 5 
if x < 10:
    print('smaller')
if x > 20:
    print('bigger')

print('Finish')'''

'''x = 5
if x == 5:
    print('Equals 5')

if x  > 4:
    print('Greater than 4')

if x >= 5:
    print('Greater than or equals 5')

if x < 6:
    print('Less than 6')

if x <= 5:
    print('Less than or equals 5')

if x !=  6:
    print('not equal to 6')'''

'''x = 5 
print('Before 5')
if x == 5:
    print('Is 5')
    print('Is stil 5')
    print('Third 5')

print('Afterwards 5')
print('Before 6')
if x == 6:
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print('Afterwards 5')'''

'''
x = 5 
if x > 2:
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i',i)
print('All done')'''
'''
x = 42 
if x > 1:
    print('More than one')
    if x  < 100:
        print('Less than 100')
print('All done')

x  = 5
if x > 2:
    print('Bigger')
else:
    print('Smaller')

x = 0
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('All done')'''

#try,except 
'''
astr = 'Hello Bob'

try:
    istr = int(astr)
except:
    istr = -1

print('First ', istr)

astr = '123'

try:
    istr = int(astr)
except:
    istr = -1

print('Second',istr)
'''
'''
astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1

print('Done ', istr)
'''

rawstr = input('Enter a number:\n')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')