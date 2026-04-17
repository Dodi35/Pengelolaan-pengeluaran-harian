data = []

def a():
    while True:
        print("1.tambah 2.lihat 3.total 4.keluar")
        x = input("pilih:")
        
        if x == "1":
            n = input("nama:")
            j = int(input("jumlah:"))
            data.append([n,j])
        
        elif x == "2":
            for i in data:
                print(i)
        
        elif x == "3":
            t = 0
            for i in data:
                t = t + i[1]
            print("total:", t)
        
        elif x == "4":
            break
        
        else:
            print("salah")

a()