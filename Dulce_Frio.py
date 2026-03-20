import tkinter as tk #importo tkinter y lo defuno como tk para no tener que escribirlo cada vez
from PIL import Image, ImageTk # librería para manejar imágenes en tkinter

# ===== CARGA DE ARCHIVOS ===== # si quiero modificar algo solo modifico el archivo de texto, no el código
def creo_sabores(): #abro el archivo sabores, lo leeo linea a linea y guardo lo leido e una lista
    Archivo_sabores=open("sabores.txt", "r")
    linea=Archivo_sabores.readline()
    lista_sabores=[]
    while linea:
        lista_sabores.append(linea.strip())
        linea=Archivo_sabores.readline()
    Archivo_sabores.close()
    return lista_sabores

def creo_sabores_palitos():# abro y guardo mis datos de sabores de palitos
    Archivo_palitos=open("palitos.txt", "r")
    linea=Archivo_palitos.readline()
    lista_palitos=[]
    while linea:
        lista_palitos.append(linea.strip())
        linea=Archivo_palitos.readline()
    Archivo_palitos.close()
    return lista_palitos

def creo_precios():
    Archivo_precios=open("precios.txt", "r") #creo un diccionario de precios, con clave y dato para acceder mas facil
    linea=Archivo_precios.readline()
    diccionario_precios={} # inicio mi diccionario
    while linea:
        linea=linea.strip().split(",") #el archivo tiene los datos de producto, y precio separados con una coma
        producto=linea[0] # el primer dato que me aparece va a ser la clave, o el tipo de producto al que despues llamo
        precio=int(linea[1]) # el segundo es mi precio, lo convierto a un entero para poder hacer operaciones matematicas despues
        diccionario_precios[producto]=precio # guardo en mi diccionario el producto y su precio
        linea=Archivo_precios.readline()
    Archivo_precios.close()
    return diccionario_precios

# ===== VARIABLES GLOBALES =====
lista_sabores = creo_sabores() 
lista_palitos = creo_sabores_palitos()
precios = creo_precios()

pedido_actual = []
ventas_dia = []

# ===== FUNCIONES DE LA INTERFAZ =====

def limpiar_pantalla(tipo):
    for widget in ventana.winfo_children(): # me devuelve una lista con todos los hijo(elementos) de mi ventana(boton,texto,etc.), y los destruyo para limpiar la pantalla
        widget.destroy()
    
    if tipo == "inicio": # para poder usar fondos distintos, cada que uso esta funcion y le doy el parametro 'tipo', le indico que fondo quiero
        archivo_foto = fondo_inicio 
    elif tipo == "opciones":
        archivo_foto = fondo_opciones
    else:
        archivo_foto = fondo_general

#de esta forma defino solo 1 vez la ventana, y solo le digo que fondo quiero ver
    if archivo_foto: # si el fondo se cargo correctamente, lo muestro en la ventana con un label que ocupa toda la ventana
        label_fondo = tk.Label(ventana, image=archivo_foto)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1) # doy formato al label/ventana

def pantalla_bienvenida(): # pantalla de inicio con boton para comenzar el pedido
    limpiar_pantalla("inicio")
    tk.Button(ventana, text="INICIAR PEDIDO", font=("Arial", 16, "bold"), 
              bg="#FF6B6B", fg="white", bd=5,
              command=pantalla_principal).place(x=325, y=400) #le doy color, formato y le indico que al hacer click me lleve a la pantalla principal

def pantalla_principal(): # primeras opciones generales, de todo lo que se puede hacer en la heladeria, cada boton me lleva a una pantalla distinta
    limpiar_pantalla("opciones")
    tk.Button(ventana, text="Comprar Helado",bg="#E78E9D", fg="white", bd=5, width=20, command=pantalla_seleccion_tipo).place(x=325, y=200)# me lleva a la pantalla de compra, donde elijo el tipo de helado y los sabores
    tk.Button(ventana, text="Ver Carrito / Ticket",bg="#A5F7E5", fg="black", bd=5, width=20, command=pantalla_ticket).place(x=325, y=250)# me lleva a la pantalla donde veo el resumen de mi pedido, y puedo finalizar la compra o volver a la pantalla principal
    tk.Button(ventana, text="Cierre de Caja",bg="#E78E9D", fg="white", bd=5, width=20, command=pantalla_estadisticas).place(x=325, y=300)# me muestra las estadisticas
    tk.Button(ventana, text="Salir", width=20,bg="#A5F7E5", fg="black", bd=5, command=ventana.quit).place(x=325, y=350)# salgo del programa

def pantalla_seleccion_tipo(): # funcion de seleccion de TIPO DE HELADO, cada boton me lleva a la configuracion segun el producto
    limpiar_pantalla("general") # muestra el fondo general
    tk.Label(ventana, text="¿Qué vas a llevar hoy?", font=("Arial", 16, "bold")).pack(pady=30) 
    tk.Button(ventana, text="Palitos",bg="#E78E9D", fg="white", bd=5, width=15, command=lambda: pantalla_compra("palitos")).place(x=345,y=150) #me lleva a la pantalla de compra especifica de los palitos
    tk.Button(ventana, text="Bochas",bg="#A5F7E5", fg="black", bd=5, width=15, command=lambda: pantalla_compra("bochas")).place(x=345,y=200) # me lleva a la pantalla de compra especifica de las bochas
    tk.Button(ventana, text="Por Kilo",bg="#E78E9D", fg="white", bd=5, width=15, command=lambda: pantalla_compra("kilo")).place(x=345,y=250)# me lleva a la pantalla de compra especifica del kilo
    tk.Button(ventana, text="Volver", command=pantalla_principal).place(x=380,y=400)# volver al menu principal




def pantalla_compra(tipo): #aca estan todas las configuracion segun el TIPO DE PRODUCTO. 
    limpiar_pantalla("general") # muestro el fondo definido como general
    seleccionados = [] # las selecciones del cliente se guardan en esta lista





    # ===== FUNCIONES INTERNAS BÁSICAS =====
    def actualizar_label():# me muestra en un label cuantos sabores se seleccionaron, y cuales son para verlo en tiempo real
        lbl_contador.config(text=f"Seleccionados: {len(seleccionados)} ({', '.join(seleccionados)})") #el.join es para unir todos los sabores separandolos con comas.


    def reiniciar_seleccion(): # esta funcion se llama cada vez que cambio la cantidad de bochas o el tamaño del kilo, para reiniciar la lista de sabores seleccionados y evitar errores de cantidad/sabores
        seleccionados.clear() # borro todo lo que habia en la lista de seleccionados
        actualizar_label()# actualizo el label para mostrar que no hay sabores seleccionados

    def seleccionar(s): # esta funcion se llama cada vez que se selecciona un sabor, y se encarga de agregarlo a la lista de seleccionados, pero antes verifica que no se haya superado el limite de sabores segun el tipo de producto y la cantidad elegida
        if tipo == "palitos":
            limite = 12 # limite de 12 unidades para los palitos
        elif tipo == "bochas":
            limite = int(opcion_bochas.get()) # el limite de sabores para las bochas depende de la cantidad de bochas elegida, que se obtiene del valor del radio button
        else: # kilo
            limite = 2 if opcion_kilo.get() == "1/4" else 3 if opcion_kilo.get() == "1/2" else 4 # el limite de sabores para el kilo depende del tamaño elegido, que se obtiene del valor del radio button

        if len(seleccionados) < limite: # mientras no se haya superado el limite, se agrega el sabor seleccionado a la lista de seleccionados
            seleccionados.append(s)
        actualizar_label()






    # ===== CONFIGURACIÓN SEGÚN TIPO =====
    if tipo == "palitos":
        #creo items_disponibles asi lo uso en cada variedad de productos y siempre guarda el menu de sabores que corresponde a ese producto
        items_disponibles = lista_palitos #ahora va a guardar los sabores de palitos
        texto_titulo = "Seleccione sus Palitos" # encabezado de dicha seccion

    elif tipo == "bochas":
        items_disponibles = lista_sabores # me va a guardar los sabores para las bochas
        opcion_bochas = tk.StringVar(value="1") # creo una variable de tipo StringVar para guardar la opcion de cantidad de bochas elegida, con valor inicial de 1
        #uso strinvar porque me devuelve lo que el usuario selecciono en los radio button, y cada vez que se selecciona una opcion, se llama a la funcion reiniciar_seleccion para evitar errores de cantidad/sabores


        tk.Label(ventana, text="Seleccione cantidad:",bg="#E78E9D", fg="white", font=("Arial", 12, "bold")).pack()
        # frame es un contenedor donde agrupo elementos que quiero mostrar juntitos
        frame_bochas = tk.Frame(ventana) # creo un frame para agrupar los radio button de las bochas, y que se muestre ordenado
        frame_bochas.pack() # .pack es pata darle formato a mi grupo de elementos (los agregaria como parametros)

        # Al cambiar la opción, reiniciamos la lista
        tk.Radiobutton(frame_bochas, text="1 bocha", variable=opcion_bochas, value="1", command=reiniciar_seleccion).pack(anchor="w")# creo un radio button para cada opcion de cantidad de bochas, con su texto, su valor, y le indico que al seleccionarlo se llame a la funcion reiniciar_seleccion para limpiar las selecciones anteriores
        #use variable para guardar la opcion elegida, value para darle un valor a cada opcion, y command para indicar que al seleccionar esa opcion se llame a la funcion reiniciar_seleccion
        tk.Radiobutton(frame_bochas, text="2 bochas", variable=opcion_bochas, value="2", command=reiniciar_seleccion).pack(anchor="w")
        tk.Radiobutton(frame_bochas, text="3 bochas", variable=opcion_bochas, value="3", command=reiniciar_seleccion).pack(anchor="w")
        texto_titulo = "Seleccione sabores" # encabezado para antes de los sabores(los muestro mas abajo)

    else:  # KILO
        items_disponibles = lista_sabores
        opcion_kilo = tk.StringVar(value="1") # creo una variable de tipo StringVar para guardar la opcion de tamaño de kilo elegida, con valor inicial de 1 (que corresponde a 1 kg)
        tk.Label(ventana, text="Seleccione el tamaño:",bg="#E78E9D", fg="white", font=("Arial", 12, "bold")).pack()
        frame_kilo = tk.Frame(ventana) #creo otro frame para agrupar los radio button del kilo, y que se muestre ordenado
        frame_kilo.pack()#aca les daria formato si quiero, sino se muestran uno debajo del otro por defecto
        
        
        # Al cambiar la opción, reiniciamos la lista
        tk.Radiobutton(frame_kilo, text="1/4 Kg (máx 2)", variable=opcion_kilo, value="1/4", command=reiniciar_seleccion).pack(anchor="w")# creo un radio button para cada opcion de tamaño de kilo, con su texto, su valor, y le indico que al seleccionarlo se llame a la funcion reiniciar_seleccion para limpiar las selecciones anteriores
        #antes use variable para guardar la opcion elegida, value para darle un valor a cada opcion, y command para indicar que al seleccionar esa opcion se llame a la funcion reiniciar_seleccion
        tk.Radiobutton(frame_kilo, text="1/2 Kg (máx 3)", variable=opcion_kilo, value="1/2", command=reiniciar_seleccion).pack(anchor="w")
        tk.Radiobutton(frame_kilo, text="1 Kg (máx 4)", variable=opcion_kilo, value="1", command=reiniciar_seleccion).pack(anchor="w")
        texto_titulo = "Seleccione sabores"

    # ===== MOSTRAR PRECIOS ===== 
    #ya que tengo configurado la seccion de seleccion de cantidad/tamaño, ahora muestro los precios correspondientes a cada opcion, para que el cliente pueda ver cuanto cuesta cada una
    frame_precios = tk.Frame(ventana) # creo un frame para agrupar los precios, y que se muestre ordenado
    frame_precios.pack(pady=5)#el formato que le doy es un padding en y para separarlo un poco del resto de elementos



    if tipo == "palitos": # muestro el precio por unidad de los palitos, que obtengo del diccionario de precios con la clave "palito"
        tk.Label(frame_precios,bg="#E78E9D", fg="white", text=f"Precio por unidad: ${precios.get('palito', 0)}").pack()
        #el .get del diccionario me permite darle la clave(que producto es) y como el precio esta vinculado a esta me lo devuelve 
    elif tipo == "bochas":# muestro el precio de cada opcion de cantidad de bochas, que obtengo del diccionario de precios con las claves "(1)bocha", "(2)bocha" y "(3)bocha"
        tk.Label(frame_precios,bg="#E78E9D", fg="white", text=f"1 bocha: ${precios.get('(1)bocha', 0)} | 2 bochas: ${precios.get('(2)bocha', 0)} | 3 bochas: ${precios.get('(3)bocha', 0)}").pack()
    elif tipo == "kilo":# muestro el precio de cada opcion de tamaño de kilo, que obtengo del diccionario de precios con las claves "(1/4)kilo", "(1/2)kilo" y "(1)kilo"
        tk.Label(frame_precios,bg="#E78E9D", fg="white", text=f"1/4 kg: ${precios.get('(1/4)kilo', 0)} | 1/2 kg: ${precios.get('(1/2)kilo', 0)} | 1 kg: ${precios.get('(1)kilo', 0)}").pack()



    tk.Label(ventana, text=texto_titulo, font=("Arial", 14, "bold")).pack(pady=10)
    lbl_contador = tk.Label(ventana,bg="#A5F7E5", fg="black", text="Seleccionados: 0") # creo un label para mostrar la cantidad de sabores seleccionados, con un texto inicial de "Seleccionados: 0"
    lbl_contador.pack() #los muestro con el formato por defecto


#creo espacio donde estaran los botones de sabores, para que se muestre ordenado y separado del resto de elementos
    frame_sabores = tk.Frame(ventana) # creo un frame para agrupar los botones de sabores, y que se muestre ordenado
    frame_sabores.pack(pady=10) # le doy un formato con un padding en y para separarlo un poco del resto de elementos, y que se vea mejor
    # ===== BOTONES DE SABORES =====
    for i, sabor in enumerate(items_disponibles): # recorro la lista de sabores y a cada uno le creo un boton con su nombre, y le indico que al hacer click se llame a la funcion seleccionar con el sabor correspondiente como parametro
        tk.Button(frame_sabores, text=sabor, width=15,
                  command=lambda s=sabor: seleccionar(s)).grid(row=i//4, column=i%4, padx=2, pady=2)# uso .grid para mostrar los botones en una cuadrícula, con 4 columnas, y le doy un formato con un padding en x e y para separarlos un poco y que se vea mejor


    def confirmar(): # esta funcion se llama al hacer click en el boton de "AGREGAR AL CARRITO", y se encarga de calcular el subtotal del producto seleccionado, crear un diccionario con la informacion del producto (tipo, sabores y precio) y agregarlo a la lista de pedido_actual, para luego volver a la pantalla principal
        if not seleccionados: return # si no se selecciono ningun sabor, no hace nada al hacer click en confirmar
        
        #creo una llave ya que en el ticket quiero mostrar algo como "3 palitos" o "1/2 kilo", y esta informacion la tengo que armar con la cantidad y el tipo de producto, para luego mostrarla en el resumen del pedido
        if tipo == "palitos":# calculo el subtotal  y creo una llave para el ticket con la cantidad de palitos
            subtotal = precios.get("palito", 0) * len(seleccionados)
            llave_ticket = f"{len(seleccionados)} Palitos"

        elif tipo == "bochas":
            cantidad = opcion_bochas.get()# obtengo la cantidad de bochas elegida del valor del radio button, para calcular el subtotal y crear la llave para el ticket
            subtotal = precios.get(f"({cantidad})bocha", 0) #obtengo el precio del diccionario
            llave_ticket = f"{cantidad} bochas"
        else:
            llave_precio = "(1/4)kilo" if opcion_kilo.get()=="1/4" else "(1/2)kilo" if opcion_kilo.get()=="1/2" else "(1)kilo" #obtengo la opcion elegida del 
            subtotal = precios.get(llave_precio, 0)#obtengo el precio del diccionario segun la opcion de tamaño de kilo elegida
            llave_ticket = f"Pote {llave_precio}"

        pedido_actual.append({"tipo": llave_ticket, "sabores": list(seleccionados), "precio": subtotal}) #guardo los datos con formato de diccionario en la lista de pedido_actual, para luego mostrarlo en el resumen del pedido
        pantalla_principal() #vuelvo a la pantalla principal despues de agregar el producto al pedido_actual

    tk.Button(ventana, text="AGREGAR AL CARRITO", bg="lightgreen", command=confirmar).pack(pady=10) #boton de que usa la funcion confirmar
    tk.Button(ventana, text="Cancelar",bg="#A81D34", fg="white", command=pantalla_principal).pack() # boton para volver a la pantalla principal sin agregar nada

def pantalla_ticket(): #resumen del pedido con cada producto 
    limpiar_pantalla("general")
    tk.Label(ventana, text="RESUMEN DEL PEDIDO", font=("Arial", 16, "bold"), fg="#E78E9D").pack(pady=10)
    total = sum(item['precio'] for item in pedido_actual) #en la lista de precios tengo guardados los productos que se agregaron al pedido, con su precio, entonces sumo todos

    for item in pedido_actual: # recorro la lista de pedido_actual y muestro cada producto con su tipo, sabores y precio, con un formato de texto
        tk.Label(ventana, text=f"{item['tipo']} ({', '.join(item['sabores'])}): ${item['precio']}").pack()
    
    tk.Label(ventana, text=f"TOTAL: ${total}", font=("Arial", 14, "bold"), fg="red").pack(pady=20)
    
    def finalizar():
        if total > 0:
            ventas_dia.append(total)# agrego el total del pedido a la lista de ventas_dia, para luego mostrarlo en las estadisticas
            pedido_actual.clear()# limpio la lista de pedido_actual para que no se muestre nada en el resumen del pedido cuando vuelva a la pantalla principal
            pantalla_principal()

    def eliminar():
        pedido_actual.clear()# borro lo guardado en el pedido actual, sin guardar nada
        pantalla_principal()

    tk.Button(ventana, text="COBRAR",bg="#36DB44", fg="black", width=15, command=finalizar).place(x=345,y=250)
    tk.Button(ventana, text="ELIMINAR PEDIDO",bg="#A81D34", fg="white", width=15, command=eliminar).place(x=345,y=300)
    tk.Button(ventana, text="VOLVER",bg="#E78E9D", fg="white", width=15, command=pantalla_principal).place(x=345,y=350)


    

def pantalla_estadisticas(): 
    limpiar_pantalla("general")
    tk.Label(ventana,bg="#E78E9D", fg="white", text="ESTADÍSTICAS DEL DÍA", font=("Arial", 16, "bold")).pack(pady=50)
    tk.Label(ventana,bg="#A5F7E5", fg="black", text=f"Ventas realizadas: {len(ventas_dia)}").pack(pady=50)
    tk.Label(ventana,bg="#E78E9D", fg="white", text=f"Total recaudado: ${sum(ventas_dia)}", font=("Arial", 14)).pack(pady=20)
    tk.Button(ventana, text="VOLVER", command=pantalla_principal).pack(pady=20)






# ===== INICIO =====
ventana = tk.Tk() #creo la ventana principal de mi programa, y la defino como "ventana" para poder usarla en todas las funciones sin tener que crearla cada vez
ventana.title("Dulce Frío")
ventana.geometry("800x500")

try: # intento cargar las imagenes para los fondos, y si no se pueden cargar por algun motivo, asigno None a las variables para evitar errores al mostrar los fondos
    fondo_inicio = ImageTk.PhotoImage(Image.open("foto_inicio.jpeg").resize((800, 500)))
    fondo_opciones = ImageTk.PhotoImage(Image.open("foto.jpeg").resize((800, 500)))
    fondo_general = ImageTk.PhotoImage(Image.open("menu.jpeg").resize((800, 500)))
    #si no funcionan las fotos, verficiar que esten en .jpeg y no en .png,ademas de que deben tener el nombre correcto,  sino cambiar este mismo
except:
    fondo_inicio = fondo_opciones = fondo_general = None

pantalla_bienvenida()
ventana.mainloop() #inicio el loop de la ventana para que se muestre y funcione, y que no se cierre al ejecutar el programa