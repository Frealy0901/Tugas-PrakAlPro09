handle = open("file_dunia.txt", 'r') # pada variabel ini berisi pembukaan file dan juga membacanya
kata = []  # membuat variabel kosong untuk dimasukan
for line in handle: 
    kata1 = line.strip().split()
    for kalmt in kata1:
        kata.append(kalmt) # akan memasukan hasil perulangan dan strip dan split ke dalam variabel kata
print(kata) # memuculkan
            



