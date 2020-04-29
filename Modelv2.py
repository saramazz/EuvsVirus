''' model bluethoot e AC '''
import random
 #model Corona Analytica
r0=2; #coeff diffusione
l=2; #livelli di profondità albero
adp=0.2; #adoption
subjects=[] #lista vuota, avrà lunghezza r0^l con tutte le persone;
for i in range(0, r0**l):
    subjects.append(random.randint(0,1))
notified_CA=sum(subjects)*adp;
print(subjects)
print("People notified by Corona Analytica %d" % (notified_CA))

#model Bluethoot only
class Albero:
  def __init__(self, Contenuto, Sinistra=None, Destra=None):
    self.Contenuto = Contenuto
    self.Sinistra  = Sinistra
    self.Destra = Destra
  def __str__(self):
    return str(self.Contenuto)
  #somma dei contenuti
  def Totale(Albero): #somma del contenuto dei singoli nodi
        if Albero == None: return 0
        return Albero.Contenuto + Totale(Albero.Sinistra) + Totale(Albero.Destra)
   def Totale(Albero): #somma del contenuto nodi secondo Bluet
        if Albero == None: return 0
         if Albero. #se il figlio e il padre sono entrambi malati e con l'app ??
          return Albero.Contenuto + Totale(Albero.Sinistra) + Totale(Albero.Destra)
        
#main
def StampaAlberoIn(Albero):
  if Albero == None: return
  StampaAlberoIn(Albero.Sinistra)
  print (Albero.Contenuto,
  StampaAlberoIn(Albero.Destra))

def status():
        return random.randint(0,1) #1 malato, 0 sano


tree = Albero(random.randint(0,1), Albero(random.randint(0,1)), Albero(random.randint(0,1)))#(1,0,1)
##Albero(contenuto, FiglioSinistra, FiglioDestra)

StampaAlberoIn(tree)
notified_BL=(tree.Totale)
print("People notified by bluetooth only")
print(notified_BL)
 
#efficacia: percentuale di persone che il BL si è perso rispetto il CAù
total=r0**l
efficacia=(notified_CA-notified_BL)/total*100
print("Efficacia %d" %(efficacia))
 
#da controllare probabilità adoption e modificare probabilità di
#contagio, qui è 0 o 1 (al 50%) e il calcolo dei notificati nel bluethooth
