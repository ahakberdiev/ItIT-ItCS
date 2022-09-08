from array import array
from time import sleep


mainInfotext = """\nThis program will calculate standard error of your experiment
based on given datasets (experiment results)\n\n"""

print(mainInfotext)

datasets = array("d")

input("Press enter to continue . . .\n\n")
sleep(1)
inputInstructions = """Enter only numbers here and press enter
If you have entered all datasets print nothing and press enter\n"""

print(inputInstructions)

sleep(3)

datasetNumber = 1
leastPrecision = 0
while True:
    inp = input("Enter dataset " + str(datasetNumber) + ": ")
    
    if inp == "":
        break

    datasets.append(float(inp))
    
    datasetNumber += 1

if len(datasets) == 0:
    exit(0)

xsum = 0
for i in datasets:
    xsum += i

avg = xsum/len(datasets)

sigma = 0
alpha = 0

for x in datasets:
    sigma += x**2

sigma = (sigma/len(datasets))**0.5
alpha = sigma/len(datasets)**0.5

print("Standard error is", alpha)
