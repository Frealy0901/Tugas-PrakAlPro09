list = [] # membuat list kosong untuk nanti dimasukan nilai
while True:             # mengulangi 
    print("---------------Nilai Maximum dan Minimum--------------")
    print("MASUKAN (done) UNTUK SELESAI")
    user = input("masukan angka: ")         # meminta masukan user dalam bentuk angka
    if user == "done":
        break       #jika user memasukan kata done akan menyelesaikan program
    try:
        list1 = float(user) 
        list.append(list1) # memasukan list1 yang sudah dirubah float dan memasukannya kedalam list
    except ValueError:
        print("Masukan tidak valid. Masukkan angka atau ketik 'done' untuk selesai.") #jika salah masukan inputan user maka akan muncul tulisan berikut
if list is not None: # jika list ada isi maka akan memunculkan max dan minimumnya
    print("angka maximum : ", max(list))
    print("angka minimum : ", min(list))
else : # jika tidak ada isi maka akan muncul pesan sebagai berikut
    print("tidak ada angka yang dimasukan")
   