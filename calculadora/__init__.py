def crear(names,goal,goals_avoid,assits):
    x={}
    for i in range(20):
        x.update({names[i]: (lambda: (goal[i],goals_avoid[i],assits[i]))()})
    return x
def mas_influ(diccionario):
    puntajes={}
    for jugador, valores in diccionario.items():
        puntaje = valores[0] * 1.5 + valores[1] * 1.25 + valores[2] * 1
        puntajes[jugador] = puntaje
        x=max(puntajes, key=puntajes.get)
    return x
def promedio(diccionario):
    x= sum([jugador[0] for jugador in diccionario.values()])
    x = x / 25
    return x
def promedio_goleador(diccionario, nombre):
    x=diccionario[nombre][0]
    x=x/25
    return x