def list_sum(list1, list2):
    leng = len(list1)
    for i in range(0, leng):
        list1[i] += list2[i]
    return list1
if __name__ == "__main__":
    print(list_sum([2,4,1,3], [4,1,1,2]))