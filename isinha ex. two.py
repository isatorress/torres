
with open ('series.csv','r') as file:
    for line in file:
        lista = line.split(',')
        if lista[5] == '10' and lista[6] == '10\n':
            print(line)

        
    

