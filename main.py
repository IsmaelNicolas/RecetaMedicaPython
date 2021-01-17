from datetime import datetime
import tkinter as tk
from tkinter import Frame, ttk 
from tkinter.constants import BOTH, BOTTOM, END,  FLAT, LEFT, N,  SOLID, SUNKEN, TOP, W
import time
from fpdf import FPDF

class RecetaMedica(tk.Frame):
    
    def __init__(self,master=None,Medico = " ",Cedula = " "):
        super().__init__(master)
        #self.Medico()
        self.nombreM = Medico
        self.cedulaM = Cedula

        self.now = datetime.now()
        self.num = 1
        self.data = []

     
        self.master=master
        self.master.focus()
        self.pack()
        self.config(background="white")
        self.master.title("Receta medica")
        self.master.geometry("550x650")
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
        self.spnUnit = tk.Spinbox(añadir,from_=1,to=7,width=7)
        self.spnUnit.grid(row=1,column=1,sticky="w",pady=7)

        tk.Label(añadir,text="Periodo:",fg="black",font="Times 14 ",justify=tk.RIGHT,background="white").grid(row=1,column=2,sticky="w")
        self.txtPeriod = tk.Entry(añadir,relief=SOLID)#tk.Spinbox(añadir,from_=1,to=24,width=7).grid(row=1,column=3,sticky="w")
        #tk.Label(añadir,text="Horas",fg="black",font="Times 14 ",justify=tk.RIGHT,background="white").grid(row=1,column=4,sticky="w",pady=7)
        self.txtPeriod.grid(row=1,column=3,sticky="e")

        tk.Label(añadir,text="Observaciones: ",fg="black",font="Times 14 ",justify=tk.LEFT,background="white").grid(row=2,column=0,sticky="w")
        self.txtObservation = tk.Entry(añadir,relief=SOLID)
        self.txtObservation.grid(row=2,column=1,sticky="wnse",columnspan=4,pady=7)

        ttk.Label(añadir,text="Duracion Tratamiento: ",font="Times 14",justify=tk.CENTER,background="white").grid(row=3,column=0,sticky="w") #ttk.Label(frmDatos,text="Sexo",fg="black",font="Times 14 ",justify=tk.LEFT).grid(row=3,column=0,sticky="w")
        self.spnDuration = tk.Spinbox(añadir,from_=1,to=7,width=7)
        tk.Label(añadir,text="Dias",fg="black",font="Times 14 ",justify=tk.LEFT,background="white").grid(row=3,column=2,sticky="w",pady=7)
        self.spnDuration.grid(row=3,column=1,sticky="w")

        self.btnAñadir = tk.Button(añadir,text="Añadir",background="#16398a",fg="white",command=self.guardarEnLista)
        self.btnAñadir.grid(row=3,column=3,columnspan=2,sticky="nsew",pady=7)
        
    def IndicacionesAdicionales(self):
        self.frmIndicaciones = tk.Frame(self,relief=SOLID,bd=1,height=7)
        self.frmIndicaciones.config(background="white")
        tk.Label(self.frmIndicaciones,text="Indicaciones generales:",
        justify=tk.LEFT,anchor=W,
        background="white",relief=FLAT,
        font="Times 11").pack(side=TOP,expand=False,fill="x")
        self.Indicaciones = tk.Text(self.frmIndicaciones,relief=FLAT,height=4,font="Times 13")
        self.Indicaciones.pack(side=LEFT,expand=False)

        self.frmIndicaciones.pack(padx=15,fill="x")

    def MedicoEncargado(self):
        self.frmMedico = tk.Frame(self,relief=FLAT,height=10)

        tk.Label(self.frmMedico,text="Cedula:  " + self.cedulaM ,justify=tk.CENTER,anchor=W,background="white",relief=FLAT,font="Times 15").pack(side=BOTTOM,expand=False,fill="x")
        tk.Label(self.frmMedico,text="Medico:  " + self.nombreM ,justify=tk.CENTER,anchor=W,background="white",relief=FLAT,font="Times 15").pack(side=BOTTOM,expand=False,fill="x")
        #tk.Label(self.frmMedico,text="Firma,sello del medico",justify=tk.LEFT,anchor=N,background="white",relief=FLAT,font="Times 10").pack(side=BOTTOM,expand=False,fill="x")
        #tk.Text(self.frmMedico,relief=FLAT,height=3).pack(side=LEFT,expand=False)
        #ttk.Separator(self.frmMedico,orient=tk.HORIZONTAL).place(x=30,y=55,width=180)
                
        
        self.frmMedico.pack(padx=155,pady=2,fill="x")

   
    def guardarEnLista(self):

        preescripcion = str(self.txtPresscripcion.get())
        unidad = str(self.spnUnit.get())
        periodo = str(self.txtPeriod.get())
        observacion = str(self.txtObservation.get())
        duracion = str(self.spnDuration.get())
        datos = [self.num,preescripcion,unidad,periodo,duracion,observacion]
        self.table.insert("",self.num,text = str(self.num),values= (self.num,preescripcion,unidad,periodo,observacion,duracion) )
        self.data.append(datos)
        self.num += 1
        self.txtPresscripcion.delete(0,END)
        self.txtPeriod.delete(0,END)
        self.txtObservation.delete(0,END)
        self.spnUnit.delete(0,END)
        self.spnDuration.delete(0,END)
        
    def crearTXT(self):
        self.FileName = str(self.txtNombre.get()) + ".pdf"
        
        pdf = PDF(nombre = str(self.txtNombre.get()),
                edad = str(self.txtEdad.get() ),
                celular = str(self.txtPhone.get()),
                sexo = str(self.cmbSex.get()),
                cedula= str(self.txtCI.get()),
                correo=  str(self.txtEmail.get()),
                fecha= str(self.now.day),
                data= self.data, 
                medico = str(self.nombreM),
                CMedico= str(self.cedulaM),
                indicaciones= str(self.Indicaciones.get("1.0",END)),
                Narchivo= self.FileName
        )
        pdf.crearPDF()

        #limpieza
        self.txtNombre.delete(0,END)
        self.txtCI.delete(0,END)
        self.txtEdad.delete(0,END)
        self.txtEmail.delete(0,END)
        self.txtPhone.delete(0,END)
        self.cmbSex.delete(0,END)
        #self.Indicaciones.delete("1.0",END)


        
        print("Receta creada exitosamente .....")
       

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

class PDF():
    def __init__(self,nombre = "" ,edad = " " ,
                 cedula = " ",celular = " ",sexo = " ",
                 fecha = " ", correo = " ",data = [],
                 indicaciones = "",medico = "",CMedico = "" , Narchivo = ""):
        super().__init__()
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.celular = celular
        self.sexo = sexo
        self.fecha = fecha
        self.correo = correo
        self.data = data
        self.indicaciones = indicaciones
        self.medico = medico
        self.CMedico = CMedico
        self.NombreArchivo = Narchivo

    def crearPDF(self):
        pdf = FPDF()
        pdf.add_page()
        #file = open(self.FileName,"r")
        #Crear encabezado
        pdf.set_font('Times','B',13)
        pdf.image('logo2.png', 10, 8, 33)
        pdf.image('logo1.png', 167, 8, 33)
        pdf.cell(0,15,"\t\t\t\tESCUELA SUPERIOR POLITECNICA DE CHIMBORAZO",align='C',ln=1)
        pdf.cell(0,0,"FACULTAD DE SALUD PUBLICA",align='C',ln=1)
        pdf.cell(0,15,"CARRERA DE MEDICINA",align='C',ln=1)
        pdf.cell(0,15,"RECETA ELECTRONICA",align='C',ln=1)

        #datos del paciente
        pdf.set_font('Times','B',size=13)
        pdf.cell(0,10,"Datos del paciente: ",align='L',ln=1)
        pdf.set_font('Times',size=12.5)
        pdf.cell(0,0,"Nombre y apellido : " + self.nombre ,align='L',ln=1)
        pdf.cell(0,10,"Edad : " + self.edad ,align='L',ln=1)
        pdf.cell(0,0,"Cedula : " + self.cedula ,align='L',ln=2)
        pdf.cell(0,10,"Celular : " + self.celular ,align='L',ln=1)
        pdf.cell(0,0,"Correo : " + self.correo ,align='L',ln=2)
        
        #Tabla

        pdf.set_font('Times','B',size=12)
        pdf.cell(0,7,ln=2)
        x = pdf.get_x()
        y = pdf.get_y()
        pdf.multi_cell(110,7,"POSOLOGIA",border=1,align='C')
        pdf.set_xy(x+110,y)
        pdf.multi_cell(80,7,"INDICACIONES",border=1,align='C')
        #Tabla posologia
        pdf.set_font('Times',size=12)
        x = pdf.get_x()
        y = pdf.get_y()
        pdf.set_xy(x,y)       
        pdf.multi_cell(10,15," N° ",border=1,align='C')
        pdf.set_xy(x+10,y)       
        pdf.multi_cell(46,15,"Preescripcion",border=1,align='C')
        pdf.set_xy(x+56,y)       
        pdf.multi_cell(27,7.5,"Unidades por toma(dias)",border=1,align='C')
        pdf.set_xy(x+83,y)       
        pdf.multi_cell(27,7.5,"Periodo entre toma",border=1,align='C')
        #Tabla indicaciones
        pdf.set_xy(x+110,y)       
        pdf.multi_cell(40,15,"Obsevaciones",border=1,align='C')
        pdf.set_xy(x+150,y)       
        pdf.multi_cell(20,15,"Duracion",border=1,align='C')
        pdf.set_xy(x+170,y)       
        pdf.multi_cell(20,7.5,"Fecha final",border=1,align='C')

        #llenar tabla

        for i in range(0,len(self.data)):
            x = pdf.get_x()
            y = pdf.get_y()
            for j in range(0,5):
                str(self.data[i][j])
                pdf.set_xy(x,y)   
                #posologia    
                pdf.multi_cell(10,10,str(self.data[i][0]),border=1,align='C')
                pdf.set_xy(x+10,y)       
                pdf.multi_cell(46,10,str(self.data[i][1]),border=1,align='C')
                pdf.set_xy(x+56,y)       
                pdf.multi_cell(27,10,str(self.data[i][2]),border=1,align='C')
                pdf.set_xy(x+83,y)       
                pdf.multi_cell(27,10,str(self.data[i][3]),border=1,align='C')
                #indicaciones
                pdf.set_xy(x+110,y)       
                pdf.multi_cell(40,10,str(self.data[i][5]),border=1,align='C')
                pdf.set_xy(x+150,y)       
                pdf.multi_cell(20,10,str(self.data[i][4]),border=1,align='C')
                pdf.set_xy(x+170,y)       
                pdf.multi_cell(20,10,"-- ",border=1,align='C')
            
        #Indicaciones Adicionales
        pdf.set_font('Times','B',size=13)
        pdf.cell(0,20,ln=2)
        pdf.cell(20,10,"Indicaciones Adicionales: ",align='L',ln=1)
        pdf.set_font('Times',size=13)
        pdf.cell(0,15,self.indicaciones,align='C',ln=1,border=1)

        #Medico encargado
        pdf.set_font('Times','B',size=13)
        pdf.cell(0,20,ln=2)
        x = pdf.get_x()
        y = pdf.get_y()
        pdf.set_xy(x+43,y)  
        pdf.cell(110,20,ln=2,border=0,align='C')
        pdf.cell(0,5,ln=2)
        pdf.line(x+50,y+20,160,y+20)
        pdf.set_line_width(1)
        pdf.cell(115,1,"FIRMA Y SELLO DEL PROF. MEDICO: ",align='C',ln=1)
        pdf.set_font('Times',size=13)
        pdf.cell(0,5,ln=2)
        pdf.cell(0,5,"Nombre: " + self.medico,align='C',ln=1)
        pdf.cell(0,5,"CI: " + self.CMedico,align='C',ln=1)

        #crear arcrivo
        pdf.output(self.NombreArchivo)




if __name__ == "__main__":
    
    root = tk.Tk()
    root.config(background="white")
    root.resizable(0,0)
    Register(master= root)
    root.mainloop()

    

