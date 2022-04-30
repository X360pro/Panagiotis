import fileinput

for line in fileinput.input("sample.py", inplace=True):
    if(line[0]=='#'):
        print('{}'.format(line[1:]), end='')
    else:
        print('{}'.format(line), end='')


print('{}'.format("hello"))