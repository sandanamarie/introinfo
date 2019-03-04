def mon_jeu(repr3):
    
    
    
    for jeux in repr3:
        if jeux == 1:
            place_detail = place_detail + 'True'
        else:
            place_detail = place_detail + 'False'
            
    print(place_detail)
    return

state = ['-','-','-','-','-','1','-','-','-',]
mon_jeux (repr3=state)


def ma_fonction(param):
    variable=param[2]
    return variable
result=ma_fonction(param=["z","b","c","d","e","f","g"])
print(result*3)