def binom (n, k):
  b = 1
  for i in range (k):
    b = b * (n-i)//(i+1)
  return b

def matrice_binom (n):
  M = []
  for i in range (n):
    l = []
    for i in range (n):
      l.append (binom (j+i, i))
    M.append(l)
  return M
