jina = "python expt"

for j in jina:
    if j != 1:
        print(j)
x = ["Python", "exceptions", "try and except"]

try:
    for i in range(5):
        print(f"The index and element from the list is {i, x[i]}")
except:
    print("index out of range")
