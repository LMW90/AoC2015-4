import hashlib
import re
import time
# for timing runtime
startTime = time.time()
# regex for finding hash we are interested in
regex = re.compile(r'^000000.*')
# variable to increment
sufix = 0
result = ''
# lopp untill regex matched by hash converted into a string
while not regex.match(result):
    inputData = 'ckczppom'
    # combine input with sufix
    inputData += str(sufix)
    # hash it
    result = hashlib.md5(inputData.encode())
    # convert into a string
    result = result.hexdigest()
    sufix += 1
# display result and sufix that genereted it
print(result)
print(sufix - 1)
# callculate and display runtime
execTime = (time.time() - startTime)
print(execTime)