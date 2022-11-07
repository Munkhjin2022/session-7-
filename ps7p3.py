def compmpg(mile,gallon):
  mpg= float(mile)/float(gallon)

  return mpg

def compcost(gallon):
  cost=gallon*2.50

  return cost 

city=input("Enter the destination city")
mile=float(input("Enter miles travelled"))
gallon=float(input("Enter gallons used "))

mpg=compmpg(mile,gallon)

cost=compcost(gallon)

print("Destination city: ", city)
print("Miles travelled: ",mile)
print("Miles per gallons: ", mpg)
print("Total cost of gas: ", cost)

