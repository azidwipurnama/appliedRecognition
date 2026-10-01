import numpy as np
file_input = "02a_inputs_200_401.npy"
file_label = "02b_labels_200_11.npy"

inputs = np.load(file_input)   #Please type the file name accordingly.
labels = np.load(file_label)       #Please type the file name accordingly.
m, n = np.shape(inputs)
r, s = np.shape(labels)
print(np.shape(inputs))
print(np.shape(labels))

#Creating seeds for randomization.
a = []
for i in range(0, m):
    a.append(i)
print(np.shape(a))
print(a[0])
print(a[m-1])
np.random.shuffle(a)
print(np.shape(a))
print(a[0])
print(a[m-1])

#Now randomize inputs and labels using the seeds.
inputs_random = np.zeros(shape = (m, n), dtype = float)   #Template for the randomizes dataset (inputs).
labels_random = np.zeros(shape = (r, s), dtype = float)   #Template for the randomizes dataset (labels).

for i in range(0,m):
    inputs_random[i,:] = inputs[a[i],:]            #Realizing the randomization (inputs).
    labels_random[i,:] = labels[a[i],:]            #Realizing the randomization (labels).

np.save("03a_random_" + file_input, inputs_random)
np.save("03b_random_" + file_label, labels_random)
