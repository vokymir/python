def chart_line(array:list[int]):
    for i in range(len(array)):
        for j in range(array[i]):
            print("█", end="")
        print("")




pole:list[int] = [0,1,2,3,4,5]
chart_line(pole)