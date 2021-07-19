print("\n\nBuffer Size Example")
print("---------------------")

inputFile = open ('myfile.txt', 'r')
outputFile = open ('myoutputfile.txt', 'w')

msg = inputFile.read(10)

while len(msg):
    #outputFile.write(msg + '\n')
    outputFile.write(msg)
    msg = inputFile.read(10)    
    
inputFile.close()
outputFile.close()
