import task1
import task2
import task3_script1
import task3_script2
import task3_script3
print("outputFrom task1:",task1.out_Task1)
print("outputFrom task2:",task2.out_Task2)
print("outputFrom task3_s1:",task3_script1.out_Task3_S1)
print("outputFrom task3_s2:",task3_script2.out_Task3_S2)
"""
for compelete exiting in (task3_script2) write number after 20 second beacuse the 
input function still running!!!!
"""
print("outputFrom task3_s3:",task3_script3.out_Task3_S3)
def unlock_vault(clues):
    passw = ""
    for i in clues:
        i = str(i)
        passw += i[0]
    return passw
clues = [task1.out_Task1,task2.out_Task2,task3_script1.out_Task3_S1,task3_script2.out_Task3_S2,task3_script3.out_Task3_S3]
password = unlock_vault(clues)
print(password)