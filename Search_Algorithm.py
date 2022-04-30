arr = [1,2,3,4,5,6,7,70985,70689695,87,6,4,5,6,35,67,45,67,6,67,4,6,6,54,67,""]
y = int(input("Enter Element to be found: "))
if y in arr:
    print("Element Found")
    print("Index of Element:" , arr.index(y))
else:
    print("Element not present in array")

