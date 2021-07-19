print("\n\nWriting to a Text File Example")
print("---------------------")


f = open ('myfile.txt', 'a')

f.write('\nThis sentence will be appended.')
f.write('\nPython is Fun!')

f.close()
