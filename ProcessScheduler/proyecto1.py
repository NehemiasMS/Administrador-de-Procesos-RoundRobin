import tkinter
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import PIL
from PIL import Image, ImageTk

import sys
import os
import math

import time
from random import randint

rbool = False
fbool = True
piwifinish = False

def mover_pinguino ():
    global piwi
    global runningx, runningy, pinguinox, pinguinoy
    global rbool
    global fbool
    global piwifinish
    global pauseTimer

    global cFinished
    global finished
    global finished_tabla
    global running
    global running_tabla
    global ventana

    pauseTimer = False

    if((runningx + 50) != pinguinox and not rbool):
        pinguinox -= 1
    
    if((runningy) != pinguinoy and not rbool):
        pinguinoy -= 1

    if(runningy == pinguinoy and runningx+50 == pinguinox):
        rbool = True
        running_tabla.destroy()
        running_tabla = ttk.Frame(ventana)
        running_tabla.place(x = 860, y = 130)
        running_tabla_titulo = ttk.Label(running_tabla, text = "Running").grid()
        printnumerorunning = ttk.Label(running_tabla, text = "SO").grid(row = 1, column = 0)

    if(rbool and fbool):
        if(pinguinox != 1250):
            pinguinox += 1

        if(pinguinoy != 30):
            pinguinoy -= 1
        
        if(pinguinox == 1250 and pinguinoy == 30):
            fbool = False
            cFinished += 1
            printFinished = ttk.Label(finished_tabla, text = running[0].numero).grid(row = cFinished, column = 0)
            finished.append(running[0])
            running.clear()

            fish = tkinter.Canvas(finished_tabla, width = 31, height = 18, highlightthickness = 0)
            imagen = tkinter.PhotoImage(file = "C:/projects/python/os/Proyecto1/fish1.png")
            fish.config(background = "#464646")
            fish.create_image(13,8, image = imagen)
            fish.image = imagen
            fish.grid(row = cFinished, column = 1)
            
            

    if(rbool and not fbool):
        if(pinguinoy != 420):
            pinguinoy += 1
        else:
            piwifinish = True
            rbool = False
            fbool = True


    if(not piwifinish):
        piwi.place(x = pinguinox, y = pinguinoy)
        ventana.after(6, mover_pinguino)
    else:
        piwifinish = False
        pauseTimer = True


def mover_pinguinoSolo():
    global piwi
    global runningx, runningy, pinguinox, pinguinoy
    global rbool
    global fbool
    global piwifinish
    global pauseTimer
    global ventana

    pauseTimer = False
    if((runningx + 50) != pinguinox and not rbool):
        pinguinox -= 1
    
    if((runningy) != pinguinoy and not rbool):
        pinguinoy -= 1

    if(runningy == pinguinoy and runningx+50 == pinguinox):
        rbool = True
    if(rbool and fbool):
        if(pinguinox != 1250):
            pinguinox += 1

        if(pinguinoy != 30):
            pinguinoy -= 1
        
        if(pinguinox == 1250 and pinguinoy == 30):
            fbool = False

    
    if(rbool and not fbool):
        if(pinguinoy != 420):
            pinguinoy += 1
        else:
            piwifinish = True
            print("De regreso")
            rbool = False
            fbool = True


    if(not piwifinish):
        piwi.place(x = pinguinox, y = pinguinoy)
        ventana.after(6, mover_pinguinoSolo)
    else:
        piwifinish = False
        pauseTimer = True

# Crear ventana principal
ventana = tk.ThemedTk(theme = "equilux", background = True)
ventana.geometry("1500x600")

ventana.overrideredirect(True)
ventana.geometry("{0}x{1}+0+0".format(ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
ventana.focus_set()
ventana.bind("<Escape>", lambda e: e.widget.quit())

# Titulo

letras = ["A", "B", "C", "D", "E", "F"]
# Objeto Proceso
class Proceso:
    global pquantum, ppromedioProceso, pprobProceso, ppromedioImpresora, pprobImpresora, frame_Size
    def __init__(self, numero, llegada):
        self.numero = numero
        self.llegada = llegada
        self.duracion = randint(2, 48)
        self.acumulado = 0
        self.impresora = "False"
        self.tiempoimpresora = 0
        self.horaimpresora = 0
        self.duracionimpresora = 0
        self.flag = -1

        if(self.duracion > 2):
            if(generarAleatorio(0, 100) < pprobImpresora):
                self.impresora = "True"
                self.horaimpresora = generarAleatorio(2, self.duracion-1)
                self.duracionimpresora = generarAleatorio(1, (ppromedioImpresora+10))

        # Crear Tap para cada proceso
            # Crear páginas
        paginas = math.ceil(self.duracion / frame_Size.get())
        i = 0
        self.pages = []
        self.page_Labels = []
        while i < paginas:
            self.pages.append(str(self.numero)+"D")
            print(self.pages[i])
            self.page_Labels.append(ttk.Label(tap_tabla, text = "D"))
            i += 1
        

# Numero aleatorio
def generarAleatorio (min, max):
    value = randint(min, max)
    return value

def stopTime():
    global stopTimer
    global contStop
    stopTimer = not stopTimer
    python = sys.executable
    os.execl(python, python, * sys.argv)

def pauseTime():
    global pauseTimer
    pauseTimer = not pauseTimer
    print(pauseTimer)
  
def easy_bro():
    global easyBro
    global wait
    global delay
    if(delay):
        wait = 150
        delay = not delay
        easyBro.configure(text = "Mas lento bro")
    else:
        wait = 1000
        delay = not delay
        easyBro.configure(text = "Ya dale otra vez")

def tick():
    
    global stopTimer
    global cont
    global tim
    global lista
    global contquantum
    global pprobProceso
    global pquantum

    # Listas de impresión
    global new_tabla
    global ready_tabla
    global running_tabla
    global waiting_tabla
    global printing_tabla
    global tap_tabla
    global waitingDisk_tabla
    global UsingDisk_tabla
    global usableram
    global usableram_pointer

    global numeroproceso
    global procesosmaximos
    global cFinished

    global tabla
    global printnumero
    global printllegada
    global printduracion
    global printacumulado
    global printimpresora
    global printimpresorah
    global printimpresorad

    global quantum
    global waiting
    global printing
    global cPrinting
    global running_tabla
    global diskCounter

    if(stopTimer and cFinished < procesosmaximos):
        if(pauseTimer):
            cont += 1
            tim.configure(text = cont)

            # Generar nuevos procesos
            if(generarAleatorio(0, 100) < pprobProceso and numeroproceso < procesosmaximos):
                numeroproceso += 1
                proceso = Proceso(numeroproceso, cont)
                new.append(proceso)      # Añadir elemento a la lista
                listaprocesos.append(proceso)

            if(running):
                # La página A está visitada?
                # Primera posición del proceso - running[0].pages[0] -
                if(running[0].flag == -1):
                    # Pagina A utilizandose
                    running[0].flag = 0
                    # Mandar a waiting disk
                    waitingDisk.append(running[0])
                    running.clear()
                
                else:
                    # Hay cambio de página?
                    if(generarAleatorio(1, 100) > 110):
                        # A que página debo cambiar?
                        tempList = []
                        tempList.extend(running[0].pages)
                        del tempList[running[0].flag]
                        
                        new_flag = generarAleatorio(0, len(tempList))
                        running[0].flag = new_flag
                        
                    if(running[0].impresora and running[0].horaimpresora == running[0].acumulado):
                        waiting.append(running[0])
                        running.clear()
                        contquantum = 0
            
            # Hay algo en Using Disk?
            if(usingDisk):
                diskCounter += 1
                if(diskCounter > 3):
                    # Añadir página a usable ram
                    if(usableram[usableram_pointer] == "x"):
                        usableram[usableram_pointer] = usingDisk[0].pages[usingDisk[0].flag]
                    elif(usableram[usableram_pointer] != "x"):
                        splitted = usableram[usableram_pointer].split('D')
                        listaprocesos[int(splitted[0])].flag = -1
                        
                    usableram_pointer += 1
                    if(usableram_pointer == len(usableram)):
                        usableram_pointer = 0
                    usingDisk[0].page_Labels[usingDisk[0].flag].config(text = "M")
                    new.append(usingDisk[0])
                    usingDisk.clear()
                    diskCounter = 0    

            # Hay algo en waiting Disk?
            if(waitingDisk):
                if(not usingDisk):
                    usingDisk.append(waitingDisk[0])

                    del waitingDisk[0]
            
            if(printing):
                cPrinting += 1
                if(cPrinting >= printing[0].duracionimpresora):
                    ready.append(printing[0])
                    printing.clear()
                    cPrinting = 0

            # Hay proceso en waiting?
            if(waiting):
                # Hay algo en printing?
                if(not printing):
                    printing.append(waiting[0])
                    waiting.remove(printing[0])
                    # Se añade a printing

            if(ready and not running):
                running.append(ready[0])
                del ready[0]

            # Hay proceso en running?
            if(running):
                if(running[0].flag != -1):
                    contquantum += 1
                    running[0].acumulado += 1

                if(running[0].acumulado == running[0].duracion):   # Hay proceso en running y ya cumplió su duración
                    contquantum = 0
                    mover_pinguino()

                elif(contquantum == pquantum):
                    new.append(running[0])
                    running.clear()
                    contquantum = 0

            if(not running):
                # New a Ready
                ready.extend(new)
                new.clear()

            
            # ------------------------------------------------------ IMPRESIONES ---------------------------------------------------------------- #
            # Imprimir todos los procesos
            s = 4
            contlistaprocesos = 0
            tabla.destroy()
            tabla = ttk.Frame(ventana, width = 150, height = 150)
            tabla.place(x = 30, y = 30)
            tabla_numero = ttk.Label(tabla, text = "numero").grid(row = 0, column = 0, padx = s)
            tabla_llegada = ttk.Label(tabla, text = "llegada").grid(row = 0, column = 1, padx = s)
            tabla_duracion = ttk.Label(tabla, text = "duracion").grid(row = 0, column = 2, padx = s)
            tabla_acumulado =  ttk.Label(tabla, text = "acumulado").grid(row = 0, column = 3, padx = s)
            tabla_impresora = ttk.Label(tabla, text = "impresora").grid(row = 0, column = 4, padx = s)
            tabla_tiempoimpresora = ttk.Label(tabla, text = "Hora impresión").grid(row = 0, column = 5, padx = s)
            tabla_horaimpresora = ttk.Label(tabla, text = "Duración impresión").grid(row = 0, column = 6, padx = s)
                
            for x in listaprocesos:
                contlistaprocesos += 1
                
                printnumero = ttk.Label(tabla, text = x.numero).grid(row = contlistaprocesos, column = 0, padx = s)
                printllegada = ttk.Label(tabla, text = x.llegada).grid(row = contlistaprocesos, column = 1, padx = s)
                printduracion = ttk.Label(tabla, text = x.duracion).grid(row = contlistaprocesos, column = 2, padx = s)
                printacumulado = ttk.Label(tabla, text = x.acumulado).grid(row = contlistaprocesos, column = 3, padx = s)
                printimpresora = ttk.Label(tabla, text = x.impresora).grid(row = contlistaprocesos, column = 4, padx = s)
                printimpresorah = ttk.Label(tabla, text = x.horaimpresora).grid(row = contlistaprocesos, column = 5, padx = s)
                printimpresorad = ttk.Label(tabla, text = x.duracionimpresora).grid(row = contlistaprocesos, column = 6, padx = s)

            # Impresión de running
            running_tabla.destroy()
            running_tabla = ttk.Frame(ventana)
            running_tabla.place(x = 860, y = 130)
            running_tabla_titulo = ttk.Label(running_tabla, text = "Running").grid()
            if(running):
                printnumerorunning = ttk.Label(running_tabla, text = running[0].numero).grid(row = 1, column = 0)
            else:
                printnumerorunning = ttk.Label(running_tabla, text = "SO").grid(row = 1, column = 0)
            
            # Impresión de printing
            if(printing):
                printnumeroprinting = ttk.Label(printing_tabla, text = printing[0].numero).grid(row = 1, column = 0)
            else:
                printnumeroprinting = ttk.Label(printing_tabla, text = "  ").grid(row = 1, column = 0)

            # Impresión de new
            contlistaprocesos = 0
            new_tabla.destroy()
            new_tabla = ttk.Frame(newframe)
            new_tabla.pack()
            new_tabla_titulo = ttk.Label(new_tabla, text = "New").grid(row = 0, column = 0)

            if(new):
                for x in new:
                    contlistaprocesos += 1
                    printnumero = ttk.Label(new_tabla, text = x.numero).grid(row = contlistaprocesos, column = 0)

            # Impresión de Ready
            contlistaprocesos = 0
            ready_tabla.destroy()
            ready_tabla = ttk.Frame(readyframe)
            ready_tabla.pack()
            ready_tabla_titulo = ttk.Label(ready_tabla, text = "Ready").grid(row = 0, column = 0)
            if(ready):
                for x in ready:
                    contlistaprocesos += 1
                    printnumero = ttk.Label(ready_tabla, text = x.numero).grid(row = contlistaprocesos, column = 0)
            
            # Impresión de Waiting
            contlistaprocesos = 0
            waiting_tabla.destroy()
            waiting_tabla = ttk.Frame(waitingframe)
            waiting_tabla.pack()
            waiting_tabla_titulo = ttk.Label(waiting_tabla, text = "Waiting").grid()
            if(waiting):
                for x in waiting:
                    contlistaprocesos += 1
                    printnumero = ttk.Label(waiting_tabla, text = x.numero).grid(row = contlistaprocesos, column = 0)

            # -------------------------------- PROYECTO III ------------------------------

            # Impresión de Tap
            i = 0
            for x in listaprocesos:
                tamano = len(x.page_Labels)
                while(i < tamano):
                    x.page_Labels[i].grid(row = x.numero, column = i+1)
                    i += 1
                i = 0
            
            # Impresión de UsingDisk
            if(usingDisk):
                UsingDisk_numero.config(text = usingDisk[0].numero)
            else:
                UsingDisk_numero.config(text = "  ")

            # Impresión de WaitingDisk
            contlistaprocesos = 0
            waitingDisk_tabla.destroy()
            waitingDisk_tabla = ttk.Frame(waitingDiskframe)
            waitingDisk_tabla.pack()
            waitingDisk_tabla_titulo = ttk.Label(waitingDisk_tabla, text = "Waiting Disk").grid()
            if(waitingDisk):
                for x in waitingDisk:
                    contlistaprocesos += 1
                    printnumero = ttk.Label(waitingDisk_tabla, text = x.numero).grid(row = contlistaprocesos, column = 0)

        ventana.after(wait, tick)
'''            
----------------------------------------------------------------------------------------------------------------------------------------------------
'''

            
# ------------------------ LECTURA DE PARAMETROS ------------------------
quantum = IntVar()
promedioProceso = IntVar()
probProceso = IntVar()
promedioImpresora = IntVar()
probImpresora = IntVar()
ramlectura = IntVar()
frame_Size = IntVar()

lecturas = Frame(ventana, bg = '#464646', bd = '0', highlightthickness = '0')
lecturas.place(x = 1000, y = 620)
tiempoquantum = tkinter.Scale(lecturas, from_ = 1, to = 20, resolution = 1, length = 170, variable = quantum, label = 'Quantum', orient = tkinter.HORIZONTAL, bg = '#464646', bd = '2', highlightthickness = 0).grid(row = 0, column = 2)
pproceso = tkinter.Scale(lecturas, from_ = 1, to = 100, resolution = 1, length = 170, variable = promedioProceso, label = 'Duración media de proceso', orient = tkinter.HORIZONTAL, bg = '#464646', bd = '2', highlightthickness = 0).grid(row = 1, column = 0)
prob = tkinter.Scale(lecturas, from_ = 0, to = 100, resolution = 1, length = 170, variable = probProceso, label = 'Probabilidad de proceso', orient = tkinter.HORIZONTAL, bg = '#464646', bd = '2', highlightthickness = 0).grid(row = 2, column = 0)
impr = tkinter.Scale(lecturas, from_ = 1, to = 80, resolution = 1, length = 170, variable = promedioImpresora, label = 'Duración media de impresora', orient = tkinter.HORIZONTAL, bg = '#464646', bd = '2', highlightthickness = 0).grid(row = 1, column = 1)
probI = tkinter.Scale(lecturas, from_ = 0, to = 100, resolution = 1, length = 170, variable = probImpresora, label = 'Probabilidad de impresora', orient = tkinter.HORIZONTAL, bg = '#464646', bd = '2', highlightthickness = 0).grid(row = 2, column = 1)
RAMLabel = tkinter.Scale(lecturas, from_ = 32, to = 256, resolution = 4, length = 170, variable = ramlectura, label = 'ram', orient = tkinter.HORIZONTAL, bg = '#464646', bd = '2', highlightthickness = 0).grid(row = 1, column = 2)
Frame_Size = tkinter.Scale(lecturas, from_ = 4, to = 32, resolution = 8, length = 170, variable = frame_Size, label = 'Tamaño de Frame', orient = tkinter.HORIZONTAL, bg = '#464646', bd = '2', highlightthickness = 0).grid(row = 2, column = 2)

quantum.set(5)
promedioProceso.set(20)
probProceso.set(50)
promedioImpresora.set(15)
probImpresora.set(40)
ramlectura.set(128)
frame_Size.set(16)

pquantum = 0
ppromedioProceso = 0
pprobProceso = 0
ppromedioImpresora = 0
pprobImpresora = 0
pram = 0
pframe_Size = 0
frames = 0

def start():
    global pquantum, ppromedioProceso, pprobProceso, ppromedioImpresora, pprobImpresora
    global quantum, promedioProceso, probProceso, promedioImpresora, probImpresora
    global ram, usableram

    pquantum = quantum.get()
    ppromedioProceso = promedioProceso.get()
    pprobProceso = probProceso.get()
    ppromedioImpresora = promedioImpresora.get()
    pprobImpresora = probImpresora.get()
    pram = ramlectura.get()
    pframe_Size = frame_Size.get()
    frames = math.ceil(pram/pframe_Size)
    espacioOs = math.ceil(frames/4)

    # Crear Memoria
    pos = 0
    while(pos < frames):
        if(pos < espacioOs):
            ram.append("SO")
        else:
            usableram.append("x")
        pos += 1

    for x in ram:
        print(x)
    for x in usableram:
        print(x)

    tick()


wait = 125
numeroproceso = 0
cont = 0
contquantum = 0
lista = []
cquantum = 0

procesosmaximos = 10

listaprocesos = []
new = []
ready = []
running = []
waiting = []
printing = []
finished = []

tim = ttk.Label(ventana, text = cont)
tim.pack()


# ------------------ BOTONES ------------------ 
stopTimer = True

play = False
playButton = ttk.Button(ventana, text = "Start", command = start, width = 5)
playButton.place(x = 600, y = 50)

contStop = False
stop = ttk.Button(ventana, text = "Stop", command = stopTime, width = 5)
stop.place(x = 660, y = 50)

pauseTimer = True
pause = ttk.Button(ventana, text = "Pause", command = pauseTime, width = 6)
pause.place(x = 720, y = 50)

delay = False
easyBro = ttk.Button(ventana, text = "Mas lento bro", command = easy_bro)
easyBro.place(x = 780, y = 50)

pbutton = ttk.Button(ventana, text = "Mover pinguinito", command = mover_pinguinoSolo, width = 20)
pbutton.place(x = 1300, y = 550)

# ---------------------------- TABLAS ----------------------------

# Tabla de procesos
separacion = 4
tabla = ttk.Frame(ventana, width = 150, height = 150)
tabla.place(x = 30, y = 30)
tabla_numero = ttk.Label(tabla, text = "numero").grid(row = 0, column = 0, padx = separacion)
tabla_llegada = ttk.Label(tabla, text = "llegada").grid(row = 0, column = 1, padx = separacion)
tabla_duracion = ttk.Label(tabla, text = "duracion").grid(row = 0, column = 2, padx = separacion)
tabla_acumulado =  ttk.Label(tabla, text = "acumulado").grid(row = 0, column = 3, padx = separacion)
tabla_impresora = ttk.Label(tabla, text = "impresora").grid(row = 0, column = 4, padx = separacion)
tabla_tiempoimpresora = ttk.Label(tabla, text = "Hora impresión").grid(row = 0, column = 5, padx = separacion)
tabla_horaimpresora = ttk.Label(tabla, text = "Duración impresión").grid(row = 0, column = 6, padx = separacion)

printnumero = ttk.Label(tabla)
printllegada = ttk.Label(tabla)
printduracion = ttk.Label(tabla)
printacumulado = ttk.Label(tabla)
printimpresora = ttk.Label(tabla)
printimpresorah = ttk.Label(tabla)
printimpresorad = ttk.Label(tabla)

# Lista de New
newframe = ttk.Frame(ventana)
newframe.place(x = 700, y = 130)
new_tabla = ttk.Frame(newframe)
new_tabla.pack()
new_tabla_titulo = ttk.Label(new_tabla, text = "New").grid()

# Lista de ready
readyframe = ttk.Frame(ventana)
readyframe.place(x = 780, y = 130)
ready_tabla = ttk.Frame(readyframe)
ready_tabla.pack()
ready_tabla_titulo = ttk.Label(ready_tabla, text = "Ready").grid()

# Linea de running
runningx = 900
runningy = 130
running_tabla = ttk.Frame(ventana)
running_tabla.place(x = runningx, y = runningy)
running_tabla_titulo = ttk.Label(running_tabla, text = "Running").grid()

# Lista de waiting
waitingframe = ttk.Frame(ventana)
waitingframe.place(x = 920, y = 200)
waiting_tabla = ttk.Frame(waitingframe)
waiting_tabla.pack()
waiting_tabla_titulo = ttk.Label(waiting_tabla, text = "Waiting").grid()

# Linea de printing
cPrinting = 0
printing_tabla = ttk.Frame(ventana)
printing_tabla.place(x = 850, y = 200)
printing_tabla_titulo = ttk.Label(printing_tabla, text = "Printing").grid(row = 0, column = 0)

# Tabla de finished
finishFrame = ttk.Frame(ventana)
finishFrame.place(x = 1350, y = 30)
finished_tabla = ttk.Frame(finishFrame)
finished_tabla.grid(row = 0, column = 0)
finished_tabla_numero = ttk.Label(finished_tabla, text = "Finished Bucket").grid(row = 0, column = 0, columnspan = 2)
cFinished = 0



# -------------------------------------------------------- PROYECTO III --------------------------------------------------------
ram = []
usableram = []
usableram_pointer = 0
diskCounter = 0

# Tabla de Tap
tapFrame = ttk.Frame(ventana)
tapFrame.place(x = 30, y = 340)
tap_tabla = ttk.Frame(tapFrame)
tap_tabla.grid(row = 0, column = 0)
tap_tabla_numero = ttk.Label(tap_tabla, text = "Proceso").grid(row = 0, column = 0)
i = 0
tap_A = ttk.Label(tap_tabla, text = "A").grid(row = 0, column = 1, padx = 10)
tap_B = ttk.Label(tap_tabla, text = "B").grid(row = 0, column = 2, padx = 10)
tap_C = ttk.Label(tap_tabla, text = "C").grid(row = 0, column = 3, padx = 10)
tap_D = ttk.Label(tap_tabla, text = "D").grid(row = 0, column = 4, padx = 10)
tap_E = ttk.Label(tap_tabla, text = "E").grid(row = 0, column = 5, padx = 10)
tap_F = ttk.Label(tap_tabla, text = "F").grid(row = 0, column = 6, padx = 10)

# Lista de Waiting Disk
waitingDisk = []

waitingDiskframe = ttk.Frame(ventana)
waitingDiskframe.place(x = 845, y = 300)
waitingDisk_tabla = ttk.Frame(waitingDiskframe)
waitingDisk_tabla.pack()
waitingDisk_tabla_titulo = ttk.Label(waitingDisk_tabla, text = "Waiting Disk").grid()
waitingDisk_numero = ttk.Label(waitingDisk_tabla, text = "")
waitingDisk_numero.grid(row = 1)

# Lista de Using Disk
usingDisk = []

UsingDiskframe = ttk.Frame(ventana)
UsingDiskframe.place(x = 845, y = 250)
UsingDisk_tabla = ttk.Frame(UsingDiskframe)
UsingDisk_tabla.pack()
UsingDisk_tabla_titulo = ttk.Label(UsingDisk_tabla, text = "Using Disk").grid()
UsingDisk_numero = ttk.Label(UsingDisk_tabla, text = "")
UsingDisk_numero.grid(row = 1)

# ------------------------------------------------------------------------------------------------------------------------------

# Imágen de pinguino
piwi = tkinter.Canvas(ventana, width = 76, height = 99, bd = '0', highlightthickness = '0')
img = tkinter.PhotoImage(file = "C:/projects/python/os/Proyecto1/penguin.png")
piwi.config(background = "#464646")

piwi.create_image(39,52, image = img)
pinguinox = 1350
pinguinoy = 420
piwi.place(x = pinguinox, y = pinguinoy)

igloo = tkinter.Canvas(ventana, width = 200, height = 168, highlightthickness = '0')
imgigloo = tkinter.PhotoImage(file = "C:/projects/python/os/Proyecto1/igloo.png")
igloo.config(background = "#464646")

igloo.create_image(95, 85, image = imgigloo)
igloo.image = imgigloo
igloo.place(x = 1250, y = 370)

ventana.mainloop()