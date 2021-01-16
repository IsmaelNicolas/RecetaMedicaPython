
from enum import Flag
import tkinter as tk
from tkinter import Frame, ttk 
from tkinter.constants import BOTH, BOTTOM,  FLAT, LEFT, N,  SOLID, SUNKEN, TOP, W
import time
from typing import Generator



class RecetaMedica(tk.Frame):
    
    def __init__(self,master=None,Medico = " ",Cedula = " "):
        super().__init__(master)
        #self.Medico()
        self.nombreM = Medico
        self.cedulaM = Cedula

        self.master=master
        self.master.focus()
        self.pack()
        self.config(background="white")
        self.master.title("Receta medica")
        self.master.geometry("550x700")
        self.Encabezado()
        self.DatosDelPaciente()
        self.Preescripcion()
        self.AñadirReceta()
        self.IndicacionesAdicionales()
        self.MedicoEncargado()
        tk.Button(self,text="Guardar",background="#16398a",fg="white",font="Times 14 ",command= self.crearTXT ).pack(side=LEFT,fill=BOTH,padx=10,pady=5)

    def Encabezado(self):
        encabezado = """ ESCUELA SUPERIOR POLITECNICA DE CHIMBORAZO \n    FACULTAD DE SALUD PUBLICA \nCARRERA DE MEDICINA\n\nRECETA ELECTRÓNICA"""   
        self.frmEncabezado = Frame(self,background="white")

        #canv = tk.Canvas(self, width=70, height=70)
        #logo1 =  tk.PhotoImage(file='Logo2.png')
        #canv.create_image(20,20, anchor=NW, image=logo1)
        #canv.place(x=40,y=30)

        imgPath = r"logo1.png"
        logo1 =  tk.PhotoImage(file=imgPath,master=self)
        lbl = tk.Label(self,image=logo1,background="white")
        lbl.image = logo1
        lbl.place(x=50,y=35)

        imgPath = r"Logo2.png"
        logo2 =  tk.PhotoImage(file=imgPath,master=self)
        lbl1 = tk.Label(self,image=logo2,background="white")
        lbl1.image = logo2
        lbl1.place(x=400,y=35)

        self.lblencabezado = tk.Label(self.frmEncabezado,text=encabezado,fg="black",font="Times 12 bold",justify=tk.CENTER,background="white").grid(row=0,column=1)
        
        self.frmEncabezado.pack()
    
    def DatosDelPaciente(self):
        self.frmDatos = Frame(self,background="white")
        self.frmDatos.rowconfigure(1, weight=1)
        self.frmDatos.columnconfigure(1, weight=1)

        #NOMBRE
        self.lblNombre = tk.Label(self.frmDatos,text="Nombre :",fg="black",font="Times 14 ",justify=tk.LEFT,background="white").grid(row=0,column=0,sticky="ws")
        self.txtNombre = tk.Entry(self.frmDatos,relief=FLAT,width=23)
        ttk.Separator(self,orient=tk.HORIZONTAL).place(x=120,y=138,width=125)
        self.txtNombre.focus()
        self.txtNombre.grid(row=0,column=1,sticky="nws")

        #RECETA
        tk.Label(self.frmDatos, text= " N° Receta : " , fg="black",font="Times 14 ",justify=tk.RIGHT,background="white").grid(row=0,column=3,sticky="w")
        self.txtReceta = tk.Entry(self.frmDatos,relief=FLAT)
        ttk.Separator(self,orient=tk.HORIZONTAL).place(x=390,y=140,width=123)
        self.txtReceta.grid(row=0,column=4,sticky="e")

        #EDAD
        tk.Label(self.frmDatos,text="Edad :",fg="black",font="Times 14 ",justify=tk.LEFT,background="white").grid(row=1,column=0,sticky="w")
        self.txtEdad = tk.Spinbox(self.frmDatos,from_=1,to=100,width=7)
        self.txtEdad.grid(row=1,column=1,sticky="w")

        #CEDULA
        self.lblCI = tk.Label(self.frmDatos,text="CI :",fg="black",font="Times 14 ",justify=tk.RIGHT,background="white").grid(row=1,column=3,sticky="w")
        self.txtCI = tk.Entry(self.frmDatos,relief=FLAT)
        ttk.Separator(self,orient=tk.HORIZONTAL).place(x=390,y=165,width=123)
        self.txtCI.grid(row=1,column=4,sticky="e")

        #CELULAR
        self.lblPhone = tk.Label(self.frmDatos,text="Celular : ",fg="black",font="Times 14 ",justify=tk.LEFT,background="white").grid(row=2,column=0,sticky="w")
        self.txtPhone = tk.Entry(self.frmDatos,relief=FLAT)
        ttk.Separator(self,orient=tk.HORIZONTAL).place(x=120,y=190,width=120)
        self.txtPhone.grid(row=2,column=1,sticky="w")

        #CORREO
        self.lblEmail = tk.Label(self.frmDatos,text="Email :",fg="black",font="Times 14 ",justify=tk.RIGHT,background="white").grid(row=2,column=3,sticky="w")
        self.txtEmail = tk.Entry(self.frmDatos,relief=FLAT)
        ttk.Separator(self,orient=tk.HORIZONTAL).place(x=390,y=190,width=123)
        self.txtEmail.grid(row=2,column=4,sticky="e")

        #SEXO
        self.lblSex = ttk.Label(self.frmDatos,text="Sexo : ",font="Times 14",justify=tk.LEFT,background="white").grid(row=3,column=0,sticky="w") #ttk.Label(frmDatos,text="Sexo",fg="black",font="Times 14 ",justify=tk.LEFT).grid(row=3,column=0,sticky="w")
        self.cmbSex = ttk.Combobox(self.frmDatos,width=17,values=["Masculino","Femenino"])
        self.cmbSex.grid(row=3,column=1,sticky="w")

        #FECHA
        self.lblDate = tk.Label(self.frmDatos,text="Fecha : ",fg="black",font="Times 14 ",justify=tk.RIGHT,background="white").grid(row=3,column=3,sticky="w")
        self.txtDate = tk.Label(self.frmDatos,background="white",text=time.strftime("%x"),fg="black",font="Times 14 ",justify=LEFT)
        self.txtDate.grid(row=3,column=4,sticky="w")

        self.frmDatos.pack(padx=40,pady=15,fill="x")

    def Preescripcion(self):
        self.frmTabla = tk.Frame(self,relief=SUNKEN,bd=1,background="white")

        tk.Label(self.frmTabla,text="Posologia",background="white").pack(side=TOP)
        self.scroll = ttk.Scrollbar(self.frmTabla,orient="horizontal")
        self.scroll.pack(side='bottom', fill="x")
        

        self.table = ttk.Treeview(
            self.frmTabla,
            height=3,
            columns=("#1", "#2", "#3","#4", "#5", "#6"),
            selectmode="none",
            show="headings"
            )

    
        self.table.heading('#1', text='N°', anchor=tk.CENTER)
        self.table.heading("#2", text="Preescripcion", anchor=tk.CENTER)
        self.table.heading("#3", text="Unidades por toma", anchor=tk.W)
        self.table.heading('#4', text='Periodo entre toma', anchor=tk.CENTER)
        self.table.heading("#5", text="Observaciones", anchor=tk.CENTER)
        self.table.heading("#6", text="Duracion", anchor=tk.W)

        self.table.column("#1", stretch=False, width=30)
        self.table.column("#2", stretch=False, width=300)
        self.table.column("#3", stretch=False, width=130)
        self.table.column("#4", stretch=False, width=150)
        self.table.column("#5", stretch=False, width=150)
        self.table.column("#6", stretch=False, width=70)
        
        self.table.configure(xscrollcommand=self.scroll.set)
        self.table.pack(side=LEFT, fill=BOTH, expand=False)

        self.scroll.config(command= self.table.xview)
        

        self.frmTabla.pack(padx=15,pady=10,fill="x")

    def AñadirReceta(self):
        self.frmLlenar = Frame(self,background="white")

        self.btnAdd = tk.Button(self.frmLlenar,
        text="Añadir receta",font="Times 14",
        background="#16398a",
        fg="white",
        relief="groove",
        command= self.Añadirdatos)
        self.btnAdd.pack(fill="x",padx=40)


        self.frmLlenar.pack(padx=5,pady=7,fill="x")

    def Añadirdatos(self):
        añadir = tk.Toplevel(self)
        añadir.title("Añadir datos")
        añadir.config(background="white")

        #añadir.overrideredirect(True)
        
        añadir.focus()

        lbl1 = tk.Label(añadir,text="Preescripcion :",fg="black",font="Times 14 ",justify=tk.LEFT,background="white").grid(row=0,column=0,sticky="w")
        self.txtPresscripcion = tk.Entry(añadir, width=50,relief=SOLID)
        self.txtPresscripcion.focus()
        self.txtPresscripcion.grid(row=0,column=1,sticky="wnse",columnspan=4,pady=7)

        tk.Label(añadir,text="Unidades por toma:",fg="black",font="Times 14 ",justify=tk.LEFT,background="white").grid(row=1,column=0,sticky="w")
        self.spnUnit = tk.Spinbox(añadir,from_=1,to=7,width=7).grid(row=1,column=1,sticky="w",pady=7)

        tk.Label(añadir,text="Periodo:",fg="black",font="Times 14 ",justify=tk.RIGHT,background="white").grid(row=1,column=2,sticky="w")
        self.spnPeriod = tk.Entry(añadir,relief=SOLID).grid(row=1,column=3,sticky="e")#tk.Spinbox(añadir,from_=1,to=24,width=7).grid(row=1,column=3,sticky="w")
        #tk.Label(añadir,text="Horas",fg="black",font="Times 14 ",justify=tk.RIGHT,background="white").grid(row=1,column=4,sticky="w",pady=7)

        tk.Label(añadir,text="Observaciones: ",fg="black",font="Times 14 ",justify=tk.LEFT,background="white").grid(row=2,column=0,sticky="w")
        self.txtObservation = tk.Entry(añadir,relief=SOLID).grid(row=2,column=1,sticky="wnse",columnspan=4,pady=7)

        ttk.Label(añadir,text="Duracion Tratamiento: ",font="Times 14",justify=tk.CENTER,background="white").grid(row=3,column=0,sticky="w") #ttk.Label(frmDatos,text="Sexo",fg="black",font="Times 14 ",justify=tk.LEFT).grid(row=3,column=0,sticky="w")
        self.spnDuration = tk.Spinbox(añadir,from_=1,to=7,width=7).grid(row=3,column=1,sticky="w")
        tk.Label(añadir,text="Dias",fg="black",font="Times 14 ",justify=tk.LEFT,background="white").grid(row=3,column=2,sticky="w",pady=7)

        btnAñadir = tk.Button(añadir,text="Añadir",background="#16398a",fg="white").grid(row=3,column=3,columnspan=2,sticky="nsew",pady=7)
        
    def IndicacionesAdicionales(self):
        self.frmIndicaciones = tk.Frame(self,relief=SOLID,bd=1,height=7)
        self.frmIndicaciones.config(background="white")
        tk.Label(self.frmIndicaciones,text="Indicaciones generales:",
        justify=tk.LEFT,anchor=W,
        background="white",relief=FLAT,
        font="Times 11").pack(side=TOP,expand=False,fill="x")
        self.Indicaciones = tk.Text(self.frmIndicaciones,relief=FLAT,height=4,font="Times 13").pack(side=LEFT,expand=False)
        

        self.frmIndicaciones.pack(padx=15,fill="x")

    def MedicoEncargado(self):
        self.frmMedico = tk.Frame(self,relief=FLAT,height=50)

        tk.Label(self.frmMedico,text="Cedula:  " + self.cedulaM ,justify=tk.LEFT,anchor=W,background="white",relief=FLAT,font="Times 10").pack(side=BOTTOM,expand=False,fill="x")
        tk.Label(self.frmMedico,text="Nombre:  " + self.nombreM ,justify=tk.LEFT,anchor=W,background="white",relief=FLAT,font="Times 10").pack(side=BOTTOM,expand=False,fill="x")
        tk.Label(self.frmMedico,text="Firma,sello del medico",justify=tk.LEFT,anchor=N,background="white",relief=FLAT,font="Times 10").pack(side=BOTTOM,expand=False,fill="x")
        tk.Text(self.frmMedico,relief=FLAT,height=3).pack(side=LEFT,expand=False)
        ttk.Separator(self.frmMedico,orient=tk.HORIZONTAL).place(x=30,y=55,width=180)
                
        
        self.frmMedico.pack(padx=155,pady=2,fill="x")

   
    def Medico(self):
        #registra = tk.Toplevel()
        #registra.title("Añadir datos")
        #registra.config(background="white")
        pass
        
    def crearTXT(self):
        self.FileName = str(self.txtNombre.get()) + ".txt"
        print(self.FileName)   
        archivo = open(self.FileName, 'a') # abre el archivo datos.txt
        archivo.write('\t\t\t\tESCUELA SUPERIOR POLITECNICA DE CHIMBORAZO\n') #escribir en el archivo  
        archivo.write('\t\t\t\t\tFACULTAD DE SALUD PUBLICA\n')
        archivo.write('\t\t\t\t\tCARRERA DE MEDICINA \n') 
        archivo.write('\t\t\t\t\tRECETA ELECTRONICA\n') 
        archivo.write('\tDATOS DEL PACIENTE\n') 
        archivo.write('\tNOMBRES Y APELLIDOS: ' + str(self.txtNombre.get()) + '\tReceta N°: 1\n' ) 
        archivo.write('\tEDAD:' + str(self.txtEdad.get() ) +  '\t\tFecha de peticion' + str(self.now.day) + '\n')
        archivo.write('\tCELULAR:' + str(self.txtPhone.get()) + '\n')
        archivo.write('\tSEXO:' + str(self.cmbSex.get()) + '\n')
        archivo.write('\tCORREO: ' + str(self.txtEmail) + '\n')
        archivo.write('\n\t------------------------ R E C E T A  --------------------\n')

        archivo.write('\n\t\t\t|--Medico encargado---------|\n')    
        archivo.write('\t\t\t|Nombre: ' + self.nombreM + '\n')         
        archivo.write('\t\t\t|CI: '+ self.cedulaM +'\n') 


        print("Receta creada exitosamente .....")
        archivo.close() #cerrar el archivo

class Register(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)

        self.master=master
        self.master.title("Registrar médico")
        

        ancho_ventana = 250
        alto_ventana = 123

        x_ventana = self.master.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.master.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.master.geometry(posicion)

        self.master.resizable(0,0)
        #self.master.wm_attributes('-type', 'splash')
        self.master.overrideredirect(True)
        x=5
        y=7
        #self.master.geometry("550x700")
        tk.Label(text="Medico: ",font="Times 12").grid(row=0,column=0,padx=x,pady=y)
        self.txtmedico = tk.Entry(font="Times 12")#.grid(row=0,column=1)
        tk.Label(text="Cedula: ",font="Times 12").grid(row=1,column=0,padx=x,pady=y)
        self.txtcedula = tk.Entry(font="Times 12")
        tk.Button(text="Aceptar",font="Times 12",command=self.receta,background="#16398a",fg="white").grid(row=2,column=1,sticky="news",padx=x,pady=y)
        tk.Button(text="Salir",font="Times 12",command=self.salir,background="#ba0918",fg="white").grid(row=2,column=0,sticky="news",padx=x,pady=y)
        
        #self.pack(padx=100,pady=10)
        self.txtcedula.grid(row=1,column=1,padx=x,pady=y)
        self.txtmedico.grid(row=0,column=1,padx=x,pady=y)

    def receta(self):
        self.root1 = tk.Tk()
        self.root1.config(background="white")
        self.root1.resizable(0,0)    
         
        self.root1.iconbitmap("icono.ico")
        self.root1.focus() 
        self.root1.deiconify()  
        app = RecetaMedica(master= self.root1 , Medico=self.txtmedico.get() , Cedula= self.txtcedula.get() )
        self.root1.focus()
        self.master.destroy()
        self.root1.mainloop()
        
    def salir(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.config(background="white")
    root.resizable(0,0)
    Register(master= root)
    root.mainloop()

    

