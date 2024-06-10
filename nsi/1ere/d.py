a=0
capture=True
while capture:
    pkmn=randint(1,4096)
    if pkmn!=4096:
        print("il n'est pas shiny")
        a=a+1
    else:
        print('il est shiny')
        capture=False