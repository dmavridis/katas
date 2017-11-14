mass = 15
LMST = [7, 3.4, 1.1, 0.77]

it = [int(mass / ii) for ii in LMST]


for l in range(it[0]):
    for m in range(it[1]):
        for s in range(it[2]):
            for t in range(it[3]):
                w = l*LMST[0] + m*LMST[0] + s*LMST[0] + t*LMST[0]
                