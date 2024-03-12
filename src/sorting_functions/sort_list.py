def list_sort(Input):
    for i in range(len(Input)):
        for j in range(i+1,len(Input)):
            if Input[i]>Input[j]:
                Input[i],Input[j]= Input[j],Input[i]
    return Input


mylist=[5,2,6,3,1]
print(list_sort(mylist))