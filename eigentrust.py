import numpy as np

Dimension = 50

#random matrix with local trust values
B =np.random.randint(5, size=(Dimension, Dimension))
print(B) 

normalised_matrix = np.identity(Dimension)
print(normalised_matrix)

#normalising trust values

#getting rid of negatives
for i in range(len(B)):
    for j in range(len(B)):
        value = max( B[i,j], 0)
        B[i,j] = value

#sum over j of S_ij
sum = B.sum(axis=1)

for i in range(len(B)):
    for j in range(len(B)):
        Sij = B[i,j]
        sum_Sij = sum[i]
        if (sum_Sij == 0):
            normalised_matrix[i,j] = 0 #could replace this value with pre-trusted value
        else:
            normalised_matrix[i,j]= Sij/sum_Sij

#print(normalised_matrix)

#aggregating local trust values
#simple non-distributed eigentrust algorithm
        
#create e vector        
e = np.empty(Dimension)
e.fill(1/Dimension)
e = np.matrix(e)
print(e)

#begin iterations
delta = 1
t = e.T 
Ct = normalised_matrix.T

while (delta > 0.001):
    t_2 = np.dot(Ct,t)
    delta = np.linalg.norm(t_2-t)
    t = t_2

#final global trust values https://dl.acm.org/doi/pdf/10.1145/775152.775242
    
print(t)
print(delta)
print(t.sum(axis=0))







        