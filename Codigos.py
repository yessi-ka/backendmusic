from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import getpass #obtener user de la compu


class Co:
    def __init__(self):    
        self.vector=[["Usuario","Maestro","admin","admin","admin"]]
        self.contador = 1
        self.musica=[] 
        self.ID=0
        self.UserActivo=0

    def Userss(self):
        from reportlab.lib.pagesizes import A4
        doc = SimpleDocTemplate("C:/Users/"+getpass.getuser()+"/Downloads/Usuarios.pdf", pagesize = A4)
        story=[]
        datos = []
        datos = [("Nombre", "Apellido", "Usuario")]
        for i in range(0,len(self.vector)):
            nuevo=[self.vector[i][0],self.vector[i][1],self.vector[i][2]]
            datos.append(nuevo)
        
        tabla = Table(data = datos,
        style = [
        ('GRID',(0,0),(-1,-1),0.5,colors.black),
        ('BOX',(0,0),(-1,-1),2,colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ]
        )
        story.append(tabla)
        story.append(Spacer(0,15))
        doc.build(story)
        return "{\"data\":\"true\"}"

    def VerUsers(self):
        texto="[\n"
        for i in range(0,len(self.vector)):
                texto+="{" 
                for j in range(0,5):
                    if j==0:
                        texto+="\"n\":\""+self.vector[i][j]+"\","                                      
                    elif j==1:
                        texto+="\"a\":\""+self.vector[i][j]+"\"," 
                    elif j==2:
                        texto+="\"u\":\""+self.vector[i][j]+"\"}," 
        texto+='{'+"\"f\":\"\"}]"
        return texto 

    def Eliminaa(self,id):
        for i in range(0,len(self.musica)):
                if id ==self.musica[i][0]:                    
                    self.musica.pop(i)
                    return True
                    break
        else:
            return False

    def registrar(self, nombre, apellido, nusuario, contra, ccontra):
        usuario = [nombre,apellido,nusuario,contra,ccontra]
        self.vector.append(usuario)
        print(self.vector)
        return True
    
    def Ingresar(self,nusuario,contra):
        for i in range(0,len(self.vector)):
            if self.vector[i][2]==nusuario and self.vector[i][3]==contra:
                self.UserActivo=i
                return True
        return False  

    def Recuperar(self,nusuario):
        for i in range(0,len(self.vector)):
            if self.vector[i][2]==nusuario:
                contraseña="{\"datas\":\""+self.vector[i][3]+"\"}"
                return contraseña
                break
        recu="{\"datas\":\"recup\"}"
        return recu

    def archivo(self,nombre,artista,album,fecha,imagen,spo,you):  
            fila=[str(self.contador),nombre,artista,album,fecha,imagen,spo,you]                                 
            self.musica.append(fila)
            self.contador+=1
            return "{\"data\":\"true\"}"
 
    def musicajson(self):
        texto="[\n"
        for i in range(0,len(self.musica)):
                texto+="{" 
                for j in range(0,8):
                    if j==0:
                        texto+="\"id\":\""+self.musica[i][j]+"\","                                      
                    elif j==1:
                        texto+="\"nombre\":\""+self.musica[i][j]+"\"," 
                    elif j==2:
                        texto+="\"artista\":\""+self.musica[i][j]+"\"," 
                    elif j==3:
                        texto+="\"album\":\""+self.musica[i][j]+"\"," 
                    elif j==4:                       
                        texto+="\"fecha\":\""+self.musica[i][j]+"\","
                    elif j==5:                       
                        texto+="\"imagen\":\""+self.musica[i][j]+"\","
                    elif j==6:                       
                        texto+="\"spo\":\""+self.musica[i][j]+"\","
                    elif j==7:                       
                        texto+="\"you\":\""+self.musica[i][j]+"\""            
                        texto+="},"
        texto+='{'+"\"f\":\"\"}]"
        return texto 

    def Genera(self): #genera canciones
        from reportlab.lib.pagesizes import A3
        from reportlab.pdfgen import canvas

        doc = SimpleDocTemplate("C:/Users/"+getpass.getuser()+"/Downloads/Musica.pdf", pagesize = A3)


        story=[]
        datos = []
        datos = [("ID","Nombre", "Artista", "Album", "Fecha")]
        for i in range(0,len(self.musica)):
            nuevo=[self.musica[i][0],self.musica[i][1],self.musica[i][2],self.musica[i][3],self.musica[i][4]]
            datos.append(nuevo)
        
        tabla = Table(data = datos,
        style = [
        ('GRID',(0,0),(-1,-1),0.5,colors.black),
        ('BOX',(0,0),(-1,-1),2,colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ]
        )
        story.append(tabla)
        story.append(Spacer(0,10))
        doc.build(story)
        return "{\"data\":\"true\"}" 
    
    def id(self,id):
        for i in range(0,len(self.musica)):
                if id ==self.musica[i][0]:
                    self.ID=i
                    return True
                    break
        else:
            return False

    def ModiCancionData(self):
        texto="[\n"
        texto+="{\"ID\":\""+self.musica[self.ID][0]+"\"," 
        texto+="\"Nombre\":\""+self.musica[self.ID][1]+"\","  
        texto+="\"Arista\":\""+self.musica[self.ID][2]+"\"," 
        texto+="\"Album\":\""+self.musica[self.ID][3]+"\"," 
        texto+="\"Fecha\":\""+self.musica[self.ID][4]+"\"," 
        texto+="\"Ima\":\""+self.musica[self.ID][5]+"\"," 
        texto+="\"Links\":\""+self.musica[self.ID][6]+"\"," 
        texto+="\"Linky\":\""+self.musica[self.ID][7]+"\"\n}]" 
        return texto

    def MusicaModificar(self,t,u,c,d,de,p,l):                             
        self.musica[self.ID][1]=t
        self.musica[self.ID][2]=u
        self.musica[self.ID][3]=c
        self.musica[self.ID][4]=d
        self.musica[self.ID][5]=de
        self.musica[self.ID][6]=p
        self.musica[self.ID][7]=l
        return True


    def DataUser(self):
        texto="[\n"
        texto+="{\"nombre\":\""+self.vector[self.UserActivo][0]+"\","    
        texto+="\"apellido\":\""+self.vector[self.UserActivo][1]+"\"," 
        texto+="\"username\":\""+self.vector[self.UserActivo][2]+"\","
        texto+="\"password\":\""+self.vector[self.UserActivo][3]+"\","
        texto+="\"Cpassword\":\""+self.vector[self.UserActivo][3]+"\"\n}]"
        return texto

   
    def ModifiCaUser(self,n,a,u,p,cp):                 
        self.vector[self.UserActivo][0]=n
        self.vector[self.UserActivo][1]=a
        self.vector[self.UserActivo][2]="admin"
        self.vector[self.UserActivo][3]=p
        self.vector[self.UserActivo][4]=cp
        return True 
 

    