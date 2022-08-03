# Leitura da vida de Jinx e Ekko
pi_jinx = int(input())
pi_ekko = int(input())
jinx = []
ekko = []
ataques_j = int(input())
for i in range(ataques_j):
    jinx.append(int(input()))
ataques_e = int(input())
for i in range(ataques_e):
    ekko.append(int(input()))

for i in jinx:
    if pi_ekko > 0:
        if pi_jinx >= pi_ekko:
            pi_ekko = pi_ekko - i
        elif pi_jinx < pi_ekko:
            pi_ekko = pi_ekko - (i // 2)
        if pi_ekko <= 0:
            pi_ekko = 0

if pi_ekko != 0:
    for j in ekko:
        if pi_jinx > 0:
            if pi_ekko >= pi_jinx:
                pi_jinx = pi_jinx - j
            elif pi_ekko < pi_jinx:
                pi_jinx = pi_jinx - (j // 2)
            if pi_jinx <= 0:
                pi_jinx = 0

print("Vida da Jinx:", pi_jinx)
print("Vida do Ekko:", pi_ekko)
if pi_jinx == pi_ekko:
    print("A batalha terminou empatada")
elif pi_jinx > pi_ekko:
    print("Jinx foi a vencedora da batalha")
else:
    print("Ekko foi o vencedor da batalha")
