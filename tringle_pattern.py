
# class pattern:
length=int(input('Enter the base of tringle:'))
def func():
    for i in range(1,length+1):
        print("* "*i)
    print()

# def func1():
    for i in range(1,length+1):
        for j in range(1,length+1):
            number = length +1-i
            if j<=number:
                print('* ',end='')
            else:
                print(' ',end='')

        print()
    print()
# length=int(input('Enter the base of tringle:'))
# p=pattern(length)
# print(p.func1)

    # for i 

    for i in range(1,length+1):
        for j in range(1,length+1):
            if j>=i:
                print('* ',end='')
            else:
                print(' ',end=' ')

        print()
    print()

    '''<----------------x-------------------------x------------------------------x------------------->'''

    for i in range(1,length+1):
        for j in range(1,length+1):
            number=length+1-i
            if j<number:
                print(' ',end=' ')
            else:
                print('* ',end='')
        print()
    print()

    '''<----------------x-------------------------x------------------------------x------------------->'''

    for i in range(1,length+1):
        for j in range(1,length+1):
            number=length+1-i
            if j<number:
                print(' ',end='')
            else:
                print('*',end=' ')
        print()
    print()


    '''<----------------x-------------------------x------------------------------x------------------->'''

    for i in range(1,length+1):
        for j in range(1,length+1):
            if j>=i:
                print('*',end=' ')
            else:
                print(' ',end='')
        print()
    print()

    '''<----------------x-------------------------x------------------------------x------------------->'''
    for i in range(1,length+1):
        for j in range(1,length+1):
            number=length+1-i
            if j<number:
                print(' ',end='')
            else:
                print('*',end=' ')
        print()
    for i in range(1,length+1):
        for j in range(1,length+1):
            if j>=i:
                print('*',end=' ')
            else:
                print(' ',end='')
        print()
func()


