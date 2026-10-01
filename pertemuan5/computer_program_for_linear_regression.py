# You are allowed to use this code but do not remove the following
# recognition: "This code has been developed by Mohammad Nasucha, Ph.D."
# This is to demonstrate a linear regression where y = mx + b
# The generation of dataset is done randomly where the x and y values are
# auto-adjusted with respect to the x data range, y data range, and the size of the canvas.
# Data variables are x and y. Screen coordinates are x_kanvas and y_kanvas.
# This program provides conversion of x to x_kanvas and y to y_kanvas.
import matplotlib.pyplot as plt
import numpy as np
import random

#USER ENTRIES
data_x_min, data_x_max = 0, 100          #range of independent data
data_y_min, data_y_max = 0, 20           #range of dependent data
m, b = 0.08, 8                     #garis regresi linier u/ simulasi data: y = mx + b
N = 1   
kanvas_row_min, kanvas_row_max = 0, 899  #ukuran kanvas
kanvas_col_min, kanvas_col_max = 0, 1199  #ukuran kanvas
margin_row = round(0.05 * kanvas_row_max)
margin_col = round(0.05 * kanvas_col_max)                           #Ini artinya jumlah dataset = N * rentang data
warna_axis  = (255, 255, 255)
warna_garis = (0, 0, 255)
warna_data  = (255, 190, 30)
warna_data2  = (255, 30, 30)
nd = 10                         #data node diameter
lw = 4                          #line width
rn = round(nd/2)                #radii of the data nodes
rl = round(lw/2)                #radii of the circles that make up the line
I = 1000                        #banyaknya data (nodes) yang ingin didemokan: 0 - N

def buat_lingkaran(gambar, py, px, r, warna): #sebagai unsur dasar garis, kurva, dan nodes (data)
    for y in range(py-r, py+r+1):
        for x in range (px-r, px+r+1):
            if (y-py)**2 + (x-px)**2 <= r**2:
                gambar[y,x] = warna

def buat_kurva(gambar, m, n, o, warna, lw):
    hw = int(lw/2)
    for x in range(0+hw, kanvas_col_max-hw):          #ensuring no node crashes the canvas' margins
        y = round(m*x**2 + n*x + o)
        if y > 0+hw and y < kanvas_row_max-hw and x > 0+hw and x < kanvas_col_max-hw:
            py = y; px = x; r = hw
            buat_lingkaran(gambar, py, px, r, warna)

def konversi_koord_data_ke_koord_kanvas(y_data, x_data, data_y_min, data_y_max, data_x_min, data_x_max, \
                                        kanvas_row_min, kanvas_row_max, kanvas_col_min, kanvas_col_max, \
                                        margin_row, margin_col):
    ver_ratio = (kanvas_row_max-kanvas_row_min-2*margin_row)/(data_y_max-data_y_min)
    hor_ratio = (kanvas_col_max-kanvas_col_min-2*margin_col)/(data_x_max-data_x_min)
    y_kanvas = round(y_data * ver_ratio + margin_row)
    x_kanvas = round(x_data * hor_ratio + margin_col)
    return (y_kanvas, x_kanvas)

#MAIN PROGRAM
gambar = np.zeros(shape=(kanvas_row_max, kanvas_col_max, 3), dtype=np.uint8) #Create the canvas.

#Create dummy dataset x dan y and save them to a list and save it to storage.
data = []                               #Buat satu list kosong.
for n in range(0, N):
    for x in range(data_x_min, data_x_max+1):
        y = m*x + b + random.uniform(-3, 3)
        data.append((y,x))    #Simpan setiap nilai data (y dan x) ke dalam list.
print(data)
print(len(data))
# save the dummy dataset
np.save("dummy_dataset.npy", data)
baca_data = np.load("dummy_dataset.npy")

#Classifying data to class1 and class2
class1 = []
class2 = []
for i in range(0, len(data)):
    y = data[i][0]
    x = data[i][1]
    if y >= m*x + b:
        class1.append((y,x))
    if y < m*x + b:
        class2.append((y,x))

print(class1)
print(len(class1))
print(class2)
print(len(class2))

#Show the data onto the kanvas
for i in range(0, len(class1)):
    y_data, x_data = class1[i][0], class1[i][1]
    koordinat_kanvas = konversi_koord_data_ke_koord_kanvas(y_data, x_data, data_y_min, data_y_max, data_x_min, data_x_max, \
                                        kanvas_row_min, kanvas_row_max, kanvas_col_min, kanvas_col_max, \
                                        margin_row, margin_col)
    y_kanvas, x_kanvas = koordinat_kanvas[0], koordinat_kanvas[1]
    #print(i,y_data, x_data, y,x)
    buat_lingkaran(gambar, y_kanvas, x_kanvas, rn, warna_data)

#Show the data onto the kanvas
for i in range(0, len(class2)):
    y_data, x_data = class2[i][0], class2[i][1]
    koordinat_kanvas = konversi_koord_data_ke_koord_kanvas(y_data, x_data, data_y_min, data_y_max, data_x_min, data_x_max, \
                                        kanvas_row_min, kanvas_row_max, kanvas_col_min, kanvas_col_max, \
                                        margin_row, margin_col)
    y_kanvas, x_kanvas = koordinat_kanvas[0], koordinat_kanvas[1]
    #print(i,y_data, x_data, y,x)
    buat_lingkaran(gambar, y_kanvas, x_kanvas, rn, warna_data2)

#Show the regression line; for now using the sama equation as the dummy data generator.
line_coordinate = []
Iy = kanvas_row_max-kanvas_row_min - 2 * margin_row
Ix = kanvas_col_max-kanvas_col_min - 2 * margin_col
dy = (data_y_max - data_y_min) / Iy                               #Ini float.
dx = (data_x_max - data_x_min) / Ix                               #Ini float.
x = data_x_min - dx
for i in range(0, Ix):
    x = x + dx            #Ini float.
    y = m*x + b           #Ini float.
    line_coordinate.append((y,x))              #Simpan koordinat titik-titik pada garis.
    koordinat_kanvas = konversi_koord_data_ke_koord_kanvas(y, x, data_y_min, data_y_max, data_x_min, data_x_max, \
                                        kanvas_row_min, kanvas_row_max, kanvas_col_min, kanvas_col_max, \
                                        margin_row, margin_col)
    y_kanvas, x_kanvas = round(koordinat_kanvas[0]), round(koordinat_kanvas[1])
    buat_lingkaran(gambar, y_kanvas, x_kanvas, rl, warna_garis)

#Show the y axis.
for y in range(kanvas_row_min+margin_row, kanvas_row_max-margin_row):
    x = kanvas_col_min+margin_col
    buat_lingkaran(gambar, y, x, rl, warna_axis)
#Show the x axis.
for x in range(kanvas_col_min+margin_col, kanvas_col_max-margin_col):
    y = kanvas_row_min + margin_row
    buat_lingkaran(gambar, y, x, rl, warna_axis)

# Tampilkan hasil di windownya Plt tanpa label apapun.
plt.figure(facecolor='black')
plt.axis('off')  # Matikan garis kartesius bawaan
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Hilangkan padding/margin
plt.imshow(gambar, origin='lower')
x = 11.7
y = m * x + b
print(x, y)
plt.show()