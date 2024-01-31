def Det_2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def Det(m):
    if len(m) == 2:
        return Det_2(m)
    det = 0
    for k in range(len(m)):  # indice de l'élément de repère
        s_m = []
        for i in range(1, len(m)):  # on prend pas la première ligne
            l = [m[i][j] for j in range(len(m)) if j != k]
            s_m.append(l)
        det += (-1)**k * m[0][k] * Det(s_m)
    return det
