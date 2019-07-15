#variables
priority = input("Did you observe priority violations? (Y or N) ")
cert = input("Is the PIC certified? (Y or N) ")
no_vio = "No violation"
vio = "Violation"

#defined functions
def quiz():
  quest = input("Did the PIC correctly answer your questions? (Y or N) ")
  if quest == "y":
      return "No violation"
  else: print(vio)

#program determines if person-in-charge demonstrates knowledge based upon presence of priority 
#violations, as well as if the PIC is either certified or correctly answers the sanitarian's
#food safety questions
while priority.lower() == "n":
  if priority.lower() == "n" and cert.lower() == "y":
    print(no_vio)
    break 
  elif priority.lower() == "n" and cert.lower() == "n":
    quiz()
    break

while priority.lower() == "y": 
  if priority.lower() == "y" and cert.lower() == "y":
    quiz()
    break
  elif priority.lower() == "y" and cert.lower() == "n":
    print(vio)
    break