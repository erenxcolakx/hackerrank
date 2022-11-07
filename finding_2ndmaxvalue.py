if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sett= set(arr)
    liste = list(sett)
    liste.remove(max(liste))
    print(max(liste))
    # input 5
    # 2 3 6 6 5