def comprate(code):
  if code=="L":
    rate=25
  elif code=="A":
    rate=30
  else:
    rate=50
  return rate

def compg(h,rate):
  if h>40:
    gpay=(h-40)*rate*1.5+40*rate
  else:
    gpay=h*rate
  return gpay

name=input("Enter the last name")
code=input("Enter job code (L, A or J)")
h=float(input("Enter number of hours"))

rate=comprate(code)
gpay=compg(h,rate)

print("The last name: ", name)
print("The gross pay: ", gpay)

