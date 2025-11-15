def bloodgroup_child(father, mother):

    ABO_dict = {"A" : [("A", "A"), ("A", "O")],
           "B" : [("B", "B"), ("B", "O")],
           "AB" : ["A", "B"],
           "O" : [("O", "O")]}
    Rhesus_dict = {"+": [("+", "+"), ("+", "-")],
                   "-": [("-", "-")]}

    blood_father = father[:-1]
    blood_mother = mother[:-1]
    Rhes_father = father[-1]
    Rhes_mother = mother[-1]

    allele_father = ABO_dict[blood_father]
    allele_mother = ABO_dict[blood_mother]

