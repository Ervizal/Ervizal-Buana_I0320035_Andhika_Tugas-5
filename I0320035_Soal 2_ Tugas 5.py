# mambuat judul program
print("==========================================")
print("====== Program Konversi Grade Nilai ======")
print("==========================================")

#membuat input nama dan nilai
nama = str(input("Masukkan nama anda : "))
nilai = float(input("Masukkan nilai anda : "))

#IF-ELSE STATEMENT
if(nilai < 60 and nilai >= 0):
	print("Halo, %s! Nilai anda setelah dikonversi adalah E" % nama)
elif(nilai < 65 and nilai >= 60):
	print("Halo, %s! Nilai anda setelah dikonversi adalah C" % nama)
elif(nilai < 70 and nilai >= 65):
	print("Halo, %s! Nilai anda setelah dikonversi adalah C+" % nama)
elif(nilai < 75 and nilai >= 70):
	print("Halo, %s! Nilai anda setelah dikonversi adalah B" % nama)
elif(nilai < 80 and nilai >= 75):
	print("Halo, %s! Nilai anda setelah dikonversi adalah B+" % nama)
elif(nilai < 85 and nilai >= 80):
	print("Halo, %s! Nilai anda setelah dikonversi adalah A-" % nama)
elif(nilai <= 100 and nilai >= 85):
	print("Halo, %s! Nilai anda setelah dikonversi adalah A" % nama)
else:
	print("Nilai yang anda masukkan tidak valid")