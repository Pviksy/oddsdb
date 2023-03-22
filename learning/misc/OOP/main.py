import team

ineos = team.Team(1, "Ineos Grenadiers", "UWT", "Great Britain")

ineos.__setattr__("name", "Ineos") #ineos.__getattribute__("id")
print(ineos.name)




uae = team.Team(2, "UAE", "UWT", None)

uae.toString()


