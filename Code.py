import matplotlib.pyplot as plt

cancion = """
When you get older, plainer, saner
When you remember all the danger we came from
Burning like embers, falling, tender
Long before the days of no surrender
Years ago, and well you know

Smoke them if you got them
Because it's going down
All I ever wanted was you
I'll never get to heaven
Because I don't know how

Let's raise a glass or two
To all the things I lost on you
Tell me, are they lost on you?
Just that you could cut me loose
After everything I've lost on you
Is that lost on you?
Is that lost on you?
Baby, is that lost on you?
Is that lost on you?

Wishing I could see the machinations
Understand the toil of expectations in your mind
Hold me like you never lost your patience
Tell me that you love me more than hate me all the time
And you're still mine

So smoke them if you've got them
Because it's going down
All I ever wanted was you
Let's take a drink of ever
This can turn around

Let's raise a glass or two
To all the things I lost on you
Tell me, are they lost on you?
Just that you could cut me loose
After everything I've lost on you
Is that lost on you?
Is that lost on you?
Baby, is that lost on you?
Is that lost on you?

Let's raise a glass or two
To all the things I've lost on you
Tell me, are they lost on you?
Just that you cold cut me loose
After everything I've lost on you
Is that lost on you?
Is that lost on you?
"""

cancion = cancion.split()

def analizar_cancion(letra:str)->dict:

    datos = {}
    palabras = len(cancion)
    contador = 0
    frecuencia = 0

    for i in cancion:

        if i not in datos:
            datos[i] = 1
        
        else:
            datos[i] += 1

    plt.figure(figsize=(10,20))
    plt.barh(range(len(datos)), datos.values(), tick_label=list(datos.keys()))
    plt.ylabel ('Palabra')
    plt.xlabel ('Frecuencia')
    plt.show()

    return datos

print(analizar_cancion(cancion))