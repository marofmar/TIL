"""
suggest the cheapest delivery method out of ground, premium ground, and drone
"""

premium_flat = 125.0 
def ground(weight, premium=False):

  flat = 20.0 
  
  if weight <= 2:
    pp = 1.50
  elif 2< weight <= 6:
    pp = 3.0
  elif 6< weight <= 10:
    pp = 4.0 
  else:
    pp = 4.75

  if premium:
    flat = premium_flat
  cost = flat + pp*weight
  return cost
  
def drone(weight):
  if weight <= 2:
    pp = 4.50
  elif 2< weight <= 6:
    pp = 9.0
  elif 6< weight <= 10:
    pp = 12.0 
  else:
    pp = 14.25
  cost = weight*pp
  return cost

# print(ground(8.4))
# print(drone(1.5))

def suggest(weight):
  gr = ground(weight), "Ground"
  pr = ground(weight, True), "Premium Ground"
  dr = drone(weight), "Drone"

  sug = min([gr[0], pr[0], dr[0]])
  print(sug)
  if sug in gr:
    print("Ground")
  elif sug in pr:
    print("Premiun Ground")
  else:
    print("Drone")

suggest(1.5)
    

  
  
