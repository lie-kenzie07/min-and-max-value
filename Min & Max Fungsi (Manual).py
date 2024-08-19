print("")
print("Max and Min Value Calculator")
print("______________________________________________")
inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
data = []
for bilangan in inputan.split(','):
    data.append(int(bilangan))
def nilai_maksimal(deret_bilangan):
  nilai_terbesar = deret_bilangan[0]

  for nilai in deret_bilangan:
    if nilai > nilai_terbesar:
      nilai_terbesar = nilai

  return nilai_terbesar

def nilai_minimal(deret_bilangan):
  nilai_terkecil = deret_bilangan[0]

  for nilai in deret_bilangan:
    if nilai < nilai_terkecil:
      nilai_terkecil = nilai

  return nilai_terkecil
print("")
print("***************")
print("Pilih Operasi:")
print("1. Min")
print("2. Max")
print("***************")
choice = input("Pilih operasi: ")
print("Data yang dimasukan:", data)
if choice == "1":
    print('Nilai minimalnya adalah', nilai_minimal(data))
elif choice == "2":
    print('Nilai maksimalnya adalah', nilai_maksimal(data))