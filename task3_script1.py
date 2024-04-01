import random
def calculate_magic_numbers(start,end):
    magic_number = []
    for i in range(20):
        rand = random.randint(start,end)
        magic_number.append(rand)
    return magic_number
magic_number = calculate_magic_numbers(1,40)
out_Task3_S1 = magic_number[0]
print(magic_number)
        
    