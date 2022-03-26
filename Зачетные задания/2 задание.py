def rhyme(n, k):
    new_list = []
    for i in range(0, n):
        i += 1
        new_list.append(i)
    print(new_list)

    while n > 1:

        del_person = k % n
        del new_list[del_person - 1]
        n -= 1


    print(f'Победил: {new_list[0]}')


if __name__ == '__main__':
    n = 10
    k = 5
    rhyme(n, k)
