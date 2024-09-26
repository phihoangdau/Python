#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the score of the runner-up.
if __name__ == '__main__':
    n = int(input("Enter number here:"))
    arr = list(map(int, input("Enter array here:").split()))
    print(max([i for i in arr if i != max(arr)]))
    print(arr)