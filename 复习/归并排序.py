# 归并排序
def mergeSort(left: int, right: int, data: list):
    if left < right:
        mid = (left+right)//2
        ldata = mergeSort(left, mid, data)
        rdata = mergeSort(mid+1, right, data)
        merge(ldata, rdata, data, left)
    return [data[i] for i in range(left, right+1)]



def merge(ldata, rdata, data: int, k: int):
    i, j = 0, 0
    lsz, rsz = len(ldata), len(rdata)
    while i < lsz and j < rsz:
        if ldata[i]<=rdata[j]:
            data[k]=ldata[i]
            i+=1
        else:
            data[k] = rdata[j]
            j+=1
        k+=1
    while i < lsz:
        data[k]=ldata[i]
        i+=1
        k+=1
    while j < rsz:
        data[k]=rdata[j]
        j+=1
        k+=1
    


lis = [2, 1, 3, 4, 5, 64, 34, 777, 55]
mergeSort(0, len(lis)-1, lis)
for i in lis:
    print(i, end=' ')
