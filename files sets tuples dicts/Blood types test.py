father = 'A+'
mother = 'B-'

ABO_dict = {"A" : [("A", "A"), ("A", "O")],
           "B" : [("B", "B"), ("B", "O")],
           "AB" : [("A", "B")],
           "O" : [("O", "O")]}
Rhesus_dict = {"+": [("+", "+"), ("+", "-")],
                   "-": [("-", "-")]}

blood_father = father[:-1]
blood_mother = mother[:-1]
Rhes_father = father[-1]
Rhes_mother = mother[-1]

allele_father = ABO_dict[blood_father]
allele_mother = ABO_dict[blood_mother]
combis = []
for i in allele_father:
    for j in allele_mother:
        combi1 = str(i[0]) + str(j[0])
        combi2 = str(i[1]) + str(j[1])
        combi3 = str(i[0]) + str(j[1])
        combi4 = str(i[1]) + str(j[0])
        combis.append(combi1)
        combis.append(combi2)
        combis.append(combi3)
        combis.append(combi4)

combis = list(set(combis))
newcombis = []
for i in combis:
    if i == 'AO' or i == 'OA':
        newcombis.append('A')
    elif i == 'OB' or i == 'BO':
        newcombis.append('B')
    elif i == 'BA':
        newcombis.append('AB')
    elif i == 'OO':
        newcombis.append('O')
    else:
        newcombis.append(i)

print(newcombis)