# You are allowed to use this code but do not remove the following
# recognition: "This code has been developed by Mohammad Nasucha, Ph.D."
# Create a Synthetic Linear Dataset (x, y)
import numpy as np
import random

#USER ENTRIES
nama_file = "dataset_linier.npy" #nama file yg dihasilkan program ini
data_x_min, data_x_max = 0, 100            #range of independent data
data_y_min, data_y_max = 0, 20               #range of dependent data
m, b = 0.08, 8  #Control m and b so that y data is within the y range.
N = 1             #N controls how many samples you will have in total.

#MAIN PROGRAM
#Create dummy dataset using a mathematical linear function and borrow 
#the computer's function for generating random numbers. 
data = []                                     #Buat satu list kosong.
for n in range(0, N):
    for x in range(data_x_min, data_x_max+1):
        y = m*x + b + random.uniform(-3, 3)  
        data.append((y,x))#Masukkan setiap nilai y dan x ke dlm list.

np.save(nama_file, data)          #Save the dummy dataset to storage.
data_read = np.load(nama_file)        #Check if the dataset is there.
print(data_read)
print(len(data))
print("A linear dataset has been generated and saved in the storage.")
print("The file name is", '"', nama_file, '"')