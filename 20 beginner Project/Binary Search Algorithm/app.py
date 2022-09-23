# function that takes a list and target parameter
# Multiple variable: middle, start, end, steps
# #recursion or while loop
# increase the steps each time a plit is done 
# conditions to track target position  

def SearchAlg(list, target):
    start = 0
    middle = 0
    end = len(list)
    count = 0

    while(start <=end):
        print(f"Counts {count} : {list[start:end+1]}")
        
        count = count + 1
        middle = (middle + end) // 2

        if(target == list[middle]):
            return middle
        if(target < list[middle]):
            end = middle - 1
        else:
            start = middle + 1
    
    return -1

mylist = [*range(10)]
Element = 9

SearchAlg(mylist, Element)