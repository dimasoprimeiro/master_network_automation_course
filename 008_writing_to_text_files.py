#writing to text files

with open('myfile.txt', 'w') as f: #create the file if it not exists
    f.write('Just a line.\nJust a second line.')
    # f.write()

with open('myfile.txt', 'a') as f: #create the file if it not exists
    f.write('\nOUTRA PORRA DE ESCRITA CARALHO BUSSETA\n')
    f.write('OUTRA LINHA NAMORAL DESSA VEZ\n')

with open('myfile.txt', 'r+') as f: #the file must exist for this r+ method, can read and write
    f.seek(5)
    f.write('100')
    f.write('Line addicionada com r+\n') # add at the beging of the file as default
    f.seek(10)
    print(f.read())


