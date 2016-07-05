# Spent too much time on trying to use replace, and looking for a different function

def to_rna(dna):
    """Swap DNA to RNA. G to C, C to G, T to A, A to U"""
    rna = []
    for letter in dna:
        if letter == 'G':
            rna.append('C')
        elif letter == 'C':
            rna.append('G')
        elif letter == 'T':
            rna.append('A')
        elif letter == 'A':
            rna.append('U')
        else:
            rna.append(str(letter))
    return ''.join(rna)
