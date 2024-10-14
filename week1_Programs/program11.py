try:
    with open("input1.txt",'r') as file:
        input_list=file.read().split()
        sum=0;
        print(input_list)
        for i in input_list:
            j=int(i)
            sum+=j
        print(sum)
except:
    print("error")