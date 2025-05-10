# Error Case
try:
    result = 12/0              #if there is an error in this section interpreter start execution from except  
    print(result)
except:
    print('Error is coming..')
print('Kamran')
print('Kamran')
print('Kamran')




# Normal Case
try:
    result = 12/2         #if there is no error in this section interpreter run try section and ignore except  
    print(result)
except:
    print('Error is coming..')
print('Kamran')
print('Kamran')
print('Kamran')