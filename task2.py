def solve_puzzles(puzzles):
    puzzles_new = puzzles.readlines()
    bool_list = []
    for i in puzzles_new:
        i = i.replace("\n","")
        try:
            bool_list.append(bool(eval(i)))
        except:
            bool_list.append(bool(i))
    return bool_list
puzzles = open("E:\project_python_uni\p2\puzzles.txt", "r")
bool_list = solve_puzzles(puzzles)
out_Task2 = bool_list[0]
print(bool_list)