fruit = {"appel": "rood", "sinaasappel": "oranje ", "kiwi": "groen"}
matrialen = {"hout":"vlambaar", "metaal": "roest", "papier": "scheuren" }



key = input("type een fruit")
fruit["druif"] = "paars"
del fruit["kiwi"]
if key == "appel":
    if "appel" in fruit:
       print(fruit["appel"])
for key in fruit:
    print(key)

print("lol")



    
   
