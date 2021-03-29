# Membuat judul program
print("==========================================")
print("==== Program Menyapa Pengunjung Hotel ====")
print("==========================================")

#membuat input nama dan jenis kelamin
nama = str(input("Silakan masukkan nama anda: "))
jenis_kelamin = str(input("Silakan masukkan jenis kelamin anda (Perempuan atau Laki-laki): "))

#membuat percabangan
if(jenis_kelamin.upper() == "LAKI-LAKI"):
	print("Selamat datang, Tuan %s" % nama) 
elif(jenis_kelamin.upper() == "PEREMPUAN"):
	print("Selamat datang, Nyonya %s" % nama)
else:
	print("Input salah")
	