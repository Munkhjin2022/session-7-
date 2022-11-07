def compavg(hit,batts):
  avg=float(hit)/float(batts)

  return avg

name=input("Enter the last name")
hit=input("Enter the number of hit")
batts=input("Enter the number of at batts")

avg=compavg(hit,batts)

print("The last name: ", name)
print("Batting average: ", avg)