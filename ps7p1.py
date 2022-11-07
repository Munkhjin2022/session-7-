def compt(q,p):
  t=float(q)* float(p)

  if t>10000.00:
    t= t-(t*0.10)
  else:
    t=t

  return t

q=float(input("Enter quantity "))
p=float(input("Enter price"))

t=compt(q,p)

print("Quantity: ", q)
print("Price: ", p)
print("Total: ",t)