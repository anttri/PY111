def rhyme(n, k):

    beaten_person = 0
    new_list = []
    for i in range(0, n):
        i += 1
        new_list.append(i)
    print(new_list)

    while True:
        if len(new_list) == 1:
            print(f'Победил: {new_list[0]}')
            break
        else:
            if k > n:
                del_person = k - n - 1 + beaten_person
                if del_person >= len(new_list):
                    del_person = del_person - len(new_list)
            else:
                del_person = k - 1 + beaten_person
                while len(new_list) <= del_person:
                    del_person = del_person - len(new_list)

            del new_list[del_person]

            beaten_person = del_person

            if beaten_person > len(new_list):
                beaten_person = beaten_person - len(new_list) - 1
            print(new_list)

    return None


if __name__ == '__main__':
    n = 10
    k = 5
    rhyme(n, k)
