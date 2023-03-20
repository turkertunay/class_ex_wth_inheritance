from class_example import Footballer

Footballer1 = Footballer("Altay Bayındır", "Türkiye", 24, "Fenerbahçe", "Goalkeeper", True)
Footballer2 = Footballer("Emre Demir", "Türkiye", 19, "Samsunspor", "Midfielder", True)
Footballer3 = Footballer("Ronaldo", "Brasil", 47, "None", "Number 9", False)

print(Footballer2.position)
if Footballer2.young() == True:
    print("The footballer is young")
else:
    print("The footballer is not young")
