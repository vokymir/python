import copy
import helping

def bubbleSort(data:list[int]):
    for i in range(len(data)-1):
        doesItAnything:bool = False
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                swap:int = data[j]
                data[j] = data[j+1]
                data[j+1] = swap
                doesItAnything = True
                print(f"[",end="")
                for k in range(len(data)):
                    if k == j:
                        print(f"\033[93m{data[k]}",end="")
                    elif k == j+1:
                        print(f"\033[94m{data[k]}",end="")
                    else:
                        print(f"\x1b[0m{data[i]}",end="")
                    if k != len(data) -1:
                        print("\x1b[0m, ",end="")
                print("]")
        if not doesItAnything:
            break

if __name__ == "__main__":
    print("Startuji program pro testov8n9 5ayen9:")
    data = helping.generate_random_array(10,0,10,1)
    dataUnsorted = copy.deepcopy(data)

    print("\x1b[0m", end="")
    print(data)

    bubbleSort(data)

    helping.testIsSorted(data)
    helping.testContainsSame(dataUnsorted, data)

    print(data)

    print("konec")