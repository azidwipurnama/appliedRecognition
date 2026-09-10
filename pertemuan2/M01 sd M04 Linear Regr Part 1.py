# You are allowed to use this code but do not remove the following
# recognition: "This code has been developed by Mohammad Nasucha, Ph.D."
# PART 1
# Visualize the dataset on the screen as is, without spatial mapping.
import matplotlib.pyplot as plt
import numpy as np

#USER ENTRIES
nama_file = "pertemuan2/dataset_linier.npy"    #nama file dataset yg akan dibaca
data_x_min, data_x_max = 0, 100            #range of independent data
data_y_min, data_y_max = 0, 20               #range of dependent data
kanvas_row_min, kanvas_row_max = 0, 899                #ukuran kanvas
kanvas_col_min, kanvas_col_max = 0, 1199                #ukuran kanvas
warna_axis  = (255, 255, 255)
warna_garis = (0, 0, 255)
warna_data  = (255, 190, 30)
warna_data2  = (255, 30, 30)
nd = 1                                    #diameter of the data nodes
nr = round(nd/2)                             #radii of the data nodes
I = 1000  #banyaknya data yang ingin didemokan: pilih antara 0 dan N.

#PREPARING FUNCTION(S)
def buat_lingkaran(gambar, py, px, r, warna): #sebagai unsur dasar garis, kurva, dan nodes (data)
    py = round(py); px = round(px)
    for y in range(py-r, py+r+1):
        for x in range (px-r, px+r+1):
            if (y-py)**2 + (x-px)**2 <= r**2:
                gambar[y,x] = warna

#MAIN PROGRAM
dataset = np.load(nama_file)     #Read the dataset in the storage.            
print(dataset)
print(len(dataset))

#Create the canvas
gambar = np.zeros(shape=(kanvas_row_max+1, kanvas_col_max+1, 3), dtype=np.uint8) #Create the canvas.

#Draw each sample of the dataset onto the canvas as a node.
for i in range(0, len(dataset)):
    y_data, x_data = dataset[i][0], dataset[i][1]
    print(i, y_data, x_data)
    buat_lingkaran(gambar, y_data, x_data, nr, warna_data)

#Show the result - tanpa label apapun.
plt.figure(facecolor='black')
plt.axis('off')                                  #Matikan garis kartesius bawaan.
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  #Hilangkan padding/margin.
plt.imshow(gambar, origin='lower')
plt.show()