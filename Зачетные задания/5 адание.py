def DNA(dna_rid):
    consensus = str()
    n = 0

    while n < 4:
        letter_counter = str()
        for i in dna_rid:
            letter_counter = letter_counter + i[n]

        letter_sum = {}

        for i in letter_counter:
            if i not in letter_sum:
                letter_sum[i] = letter_counter.count(i)

        letter_max = max(letter_sum.values())

        for i in letter_sum:
            if letter_sum[i] == letter_max:
                consensus = consensus + i
        n += 1

    print(consensus)

if __name__ == '__main__':
    dna_rid = ["ATTA", 'ACTA', 'AGCA', 'ACAA']
    DNA(dna_rid)
