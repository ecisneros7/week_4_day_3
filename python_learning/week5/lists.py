cars = ["ford", "volvo", "bmw"]
cars.append("Honda")
print(f"The cars in the list are: {cars}")
cars[-1]= "austin martin"
cars[2]= "lambo"
print(f"The cars in the list are: {cars}")
cars.insert(2, "chevy")
print(f"The cars in the list are: {cars}")
cars.remove("chevy")
print(f"The cars in the list are: {cars}")
check=("ford" in cars)
print(f"The statement that ford is in the list is {check}")