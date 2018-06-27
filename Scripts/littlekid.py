print ('What is your name?')
name = input()
#print ('You entered ' + name)

if name == 'Alice':
    print ('Hi, Alice.')
else:
    print ('What is you age?')
    age = int(input())
    if age < 12:
        print('You are not Alice, kiddo.')
    else:
        print ('You are neither Alice nor a little kid.')
