dna_sec = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

def nucleotide_sec_counts(sec):
    temp_sec = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for n in sec:
        temp_sec[n] += 1
    return temp_sec

    # Enother solution
    # a, t, g, c = 0, 0, 0, 0
    # for n in sec:
    #     if n == 'A':
    #         a += 1
    #     elif n == 'T':
    #         t += 1
    #     elif n == 'G':
    #         g += 1
    #     else:
    #         c += 1
    # print(a, t, g, c)

# print(nucleotide_sec_counts(dna_sec))
res = nucleotide_sec_counts(dna_sec)
print(' '.join([str(val) for key, val in res.items()]))