import string
lists = []
def check_pass():
    save = []
    count = 0
    while(True):
        username = input("user:")
        password = input("password:")
        tup = (username, password)
        lists.append(tup)
        count += 1
        if(input("for exit  type e:") == 'e'):
            break
    for x in lists:
        c = 0
        p = 0
        l = 0
        u = 0
        for i in x[1]:
            if(i in string.punctuation):
                p += 1
            elif(i.isupper()):
                u += 1
            elif(i.islower()):
                l += 1
            c+=1
        if(c >= 8 and l > 0 and p > 0 and u > 0):
            save.append(1)
        else:
            save.append(0)
    for l in range(count):
        if(save[l] == 1):
            print(lists[l][0])
check_pass()
out_Task3_S3 = lists[0][0] 