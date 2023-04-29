from tkinter import *
from algoritmoKruskal import inicio

arregloDeArista=[]
arregloDeVetices=[]
soloVetices=[]

def miFuncion():
    n1 = box.get()
    n2 = box1.get()
    n3 = box2.get()
    v=""+str(n1)+" ---> "+str(n2)+" peso arista "+str(n3)
    print("Esto es vertice 1 "+n1+" vertice 2 "+n2+" peso arista "+n3+"\n")
    #box4.insert(0,v)
    #texto = StringVar()
    #texto.set(v)
    #lbl3.config(textvariable=texto)
    #lbl3.set()
    #texto1.insert(0,v)
    miVariable.set(v)
    
    x=(int(n3),n1,n2)
    arregloDeArista.append(x)
    soloVetices.append(n1)
    soloVetices.append(n2)
    #x = {'A':i[0],'B':i[1]}


def verArreglo():
    unique = []
    for s in soloVetices:
        if s not in unique:
            unique.append(s)

    print(unique)



    for i in arregloDeArista:
        print(arregloDeArista)

    x = {'A':unique,'B':arregloDeArista}
    arregloDeVetices.append(x)
    print(arregloDeVetices)
    #for i in arregloDeVetices:
    #    print(i)

    inicio(arregloDeVetices)






ventana= Tk()
ventana.title("Grafos de Kruskal")    
ventana.geometry("600x400")

lbl=Label(ventana,text="Ingrese el primer vertice")
lbl.place(x=10,y=10,width=150,height=20)
#lbl.pack()

box= Entry(ventana)
box.place(x=20,y=40,width=180,height=20)

lbl=Label(ventana,text="Ingrese el segundo vertice")
lbl.place(x=10,y=70,width=150,height=20)
#lbl.pack()

box1= Entry(ventana)
box1.place(x=20,y=100,width=180,height=20)

lbl=Label(ventana,text="Ingrese el peso de la arista")
lbl.place(x=10,y=130,width=150,height=20)
#lbl.pack()

box2= Entry(ventana)
box2.place(x=20,y=160,width=180,height=20)


boton=Button(ventana, text="Agregar",command=miFuncion)
boton.place(x=350,y=40,width=100,height=30)


boton2=Button(ventana, text="Crear",command=verArreglo)
boton2.place(x=350,y=160,width=100,height=30)

lbl2=Label(ventana,text="Vetices Ingresados")
lbl2.place(x=10,y=190,width=150,height=20)
#boton.pack()

#box4= Entry(ventana)
#box4.place(x=20,y=220,width=150,height=100)


miVariable = StringVar()
miLabel = Label(ventana, textvariable = miVariable)
miLabel.place(x=10,y=220,width=700,height=180)


#texto1 = Text(ventana)
#texto1.place(x=20,y=220,width=180,height=120)

#lbl3=Label(ventana,text="")
#lbl3.place(x=10,y=220,width=150,height=20)

ventana.mainloop()
