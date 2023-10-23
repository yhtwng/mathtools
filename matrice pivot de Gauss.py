'''Indiquer la matrice A carré
A=[[2,3],[1,5]]'''
Id=[[1,0],[0,1]]

'''chaque fonction sont utiles pour effectuer la manipulation du pivot de Gauss. Pour inverser la matrice, il faudra
effectuer ces mêmes opérations en "miroir" sur la matrice identité'''

'''indiquer le numéro de deux lignes i et j à inverser'''
def echange_ligne(A,i,j):
    i=i-1
    j=j-1
    A[i],A[j]=A[j],A[i]
    return(A)
    
'''indiquer le numéro de la ligne i à multiplier et le réel non nul t'''
def multiplication_reel(A,i,t):
    i=i-1
    for j in range(len(A)):
        A[i][j]=A[i][j]*t
    return(A)

'''indiquer les numéros des lignes i et k et les réels p et t (respectivement coefficients de i et k) >>> i=p*i+t*k'''
def combinaison_lineaire(A,i,k,p,t):
    i=i-1
    k=k-1
    for j in range(len(A)):
        A[i][j]=p*A[i][j]+t*A[k][j]
    return(A)
'''    
print(multiplication_reel(A, 1, 1/2))
print(combinaison_lineaire(A, 2, 1, 1, -1))
print(multiplication_reel(A, 2, 2/7))
print(combinaison_lineaire(A, 1, 2, 1, -3/2))

print("Inverse de la matrice")

print(multiplication_reel(Id, 1, 1/2))
print(combinaison_lineaire(Id, 2, 1, 1, -1))
print(multiplication_reel(Id, 2, 2/7))
print(combinaison_lineaire(Id, 1, 2, 1, -3/2))'''
