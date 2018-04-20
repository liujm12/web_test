
import re

code = 'fefageafxxIxxgeeregefeljixxlovexxjijlhyhn3456xxyouxxfeiijogei'

a = 'ytest2345'
b = re.findall('y..',a)
print(b)


c = 'abbbgfegi2345'
d = re.findall('b*', c)
print(d)

e = 'abbbgfegi2345'
f = re.findall('b?', e)
print(f)

getcode = re.findall('xx.*?xx', code)
print(getcode)

getcode_needed = re.findall('xx(.*?)xx', code)
print(getcode_needed)

for i in getcode_needed:
    print(i)