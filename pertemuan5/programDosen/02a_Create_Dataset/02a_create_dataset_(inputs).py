"""
CATATAN TENTANG DATASET INPUT YANG DIBANGUN INI
Terdapat 10 kelas, masing-masing diwakili dengan 20 gambar. Total 200 gambar.
Kolom ke-0 berisi nomor sampel (0 s.d. 199)
Kolom ke-1 berisi piksel nomor 0 dari gambar
Kolom ke-2 berisi piksel nomor 1 dari gambar
dst sampai kolom ke 399.
File "hor (0)_ready" masuk ke dataset baris ke-0.
File "e (19)_ready" masuk ke dataset baris ke-199.
"""
import numpy as np
import matplotlib.pyplot as plt

#USER ENTRIES
file0 = "hor ("
file1 = "ver ("
file2 = "diag ("
file3 = "circle ("
file4 = "square ("
file5 = "a ("
file6 = "b ("
file7 = "c ("
file8 = "d ("
file9 = "e ("
ext = ")_ready.jpg"

#jumlah huruf = 10
juml_sampel_per_huruf = 20
juml_sampel = 200               #10*20 = 200

#MENCARI UKURAN ROW DAN COL DARI TIAP GAMBAR
i = 0                                                                     #file pertama
pic = plt.imread(file0 + str(i) + ext)                                    #Baca file pertama.
row, col = pic.shape[0], pic.shape[1]
print("row, col =", row, ",", col, ".")
juml_kolom = row * col + 1

#MENENTUKAN NAMA FILE OUTPUT
nama_file_dataset = "02a_inputs_" + str(juml_sampel) + "_" + str(juml_kolom) + ".npy"

#BUAT TEMPLATE UNTUK DATASET (.npy)
dataset = np.zeros(shape = (juml_sampel, juml_kolom), dtype=np.uint16)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#ISI KOLOM PERTAMA DATASET DENGAN NOMOR URUT SAMPEL
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
for k in range(0, juml_sampel):
    dataset[k, 0] = k

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#MEMASUKKAN NILAI PIKSEL TIAP GAMBAR KE TEMPLATE DATASET KOLOM KE-1 s.d. KOLOM TERAKHIR
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
temp = np.zeros(shape = (row, col), dtype = np.uint16) #penampung untuk tiap gambar, satu channel.
k = 0
for i in range (0, 10):                                    #file0 s.d. file9 (untuk 10 huruf).
    for n in range(0, juml_sampel_per_huruf):
        nama_file = globals()["file" + str(i)]                      #Panggil file0 s.d. file9.
        pic = plt.imread(nama_file + str(n) + ext) #Panggil file0 sampel nomor 1 s.d. 19, dst.
        temp = pic[:, :, 0]        #Tampung nilai satu channel saja. Nilai semua channel sama.
        data = temp.reshape(row*col)   #Reshape data (row, col) menjadi (row*col) agar dapat dimasukkan ke dataset.
        dataset[k, 1:juml_kolom] = data
        k += 1

print(dataset)
print(dataset[0, :])
print(dataset[199, :])

np.save(nama_file_dataset, dataset)
print(""); print("Dataset telah di-create dan disimpan pada folder yang sama dengan program ini.")

#Cek Isi Dataset dan Tampilkan Gambarnya
plt.figure()
i = 0
while i < juml_sampel:
    isi = np.load(nama_file_dataset)
    isi_baris = isi[i, 1:]                                                    #Kolom ke-0 tidak dibaca.
    isi_baris = isi_baris.reshape(row,col)
    gambar = np.zeros(shape = (row, col, 3), dtype = np.uint16)
    gambar[:, :, 0] = isi_baris
    gambar[:, :, 1] = isi_baris
    gambar[:, :, 2] = isi_baris
    plt.title (str(i))
    plt.imshow(gambar)
    plt.ion()
    plt.show()
    plt.pause(1)
    i += juml_sampel_per_huruf
