print("")
print("Max and Min Value Calculator")
print("______________________________________________")
inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
data = []
for bilangan in inputan.split(','):
    data.append(int(bilangan))
print("")
print("***************")
print("Pilih Operasi:")
print("1. Min")
print("2. Max")
print("***************")
choice = input("Pilih operasi: ")
print("Data yang dimasukan:", data)
if choice == "1":
    print('Nilai minimalnya adalah', min(data))
elif choice == "2":
    print('Nilai maksimalnya adalah', max(data))