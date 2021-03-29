# mambuat judul program
print("==========================================")
print("====== Program Konversi Grade Nilai ======")
print("==========================================")

#membuat input nama dan nilai
nama = str(input("Masukkan nama anda : "))
nilai = float(input("Masukkan nilai anda : "))

#IF-ELSE STATEMENT
if(nilai < 60):
	print("Halo, "+ nama +"! Nilai anda setelah dikonversi adalah E")
elif(nilai <= 64 and nilai >= 60):
	print("Halo, "+ nama +"! Nilai anda setelah dikonversi adalah C")
elif(nilai <= 69 and nilai >= 65):
	print("Halo, "+ nama +"! Nilai anda setelah dikonversi adalah C+")
elif(nilai <= 74 and nilai >= 70):
	print("Halo, "+ nama +"! Nilai anda setelah dikonversi adalah B")
elif(nilai <= 79 and nilai >= 75):
	print("Halo, "+ nama +"! Nilai anda setelah dikonversi adalah B+")
elif(nilai <= 84 and nilai >= 80):
	print("Halo, "+ nama +"! Nilai anda setelah dikonversi adalah A-")
elif(nilai <= 100 and nilai >= 85):
	print("Halo, "+ nama +"! Nilai anda setelah dikonversi adalah A")
else:
	print("Nilai yang anda masukkan tidak valid")