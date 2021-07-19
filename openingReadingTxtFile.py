inputFile = open ('Desktop/files/myfile.txt', 'r')
outputFile = open ('Desktop/files/myoutputfile.txt', 'w')

msg = inputfile.read(10)

while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)

inputFile.close()
outputFile.close()
