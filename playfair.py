import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, uic

 
qtCreatorFile = "Playfair.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
         
def matrix(kluc):

    symboly = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
    
       
    symboly = symboly.replace("Q","O")  
    matrix = []
    
    for char in kluc.upper():
        if char not in matrix and char in symboly:
            matrix.append(char)
    for char in symboly:
        if char not in matrix:
            matrix.append(char)

    return matrix 
    

def pairs(text):
    
 msg = []
 text = text.replace("Q","O")
 text = text.replace("q","o")
 for char in text.upper():
    msg.append(char)

    i = 0
    l = int(len(msg)/2)

    i=0


 for both in range(0,l,2):
    if msg[both] == msg[both+1]:
        msg.insert(both+1,'X')
        both = both+2      
  
 if msg[-1] == 'X' and len(msg)%2==1:
       msg.append('W') 
              
 if len(msg)%2==1:
       msg.append('X')
        
      
 text_pairs=[]

 l=int(len(msg)/2)+1

 for x in range(1,l):
      text_pairs.append(msg[i:i+2])
      i=i+2 
  
     
 return text_pairs 

def sifra_pairs(text1):
    
 msg = []
 for char in text1.upper():
    msg.append(char)

    i = 0 

    sifra_pairs=[]

    l=int(len(msg)/2)+1

 for x in range(1,l):    
    sifra_pairs.append(msg[i:i+2])
    i=i+2 

 return sifra_pairs

                   

def Sifruj(text,kluc):
        
    matica = matrix(kluc)
    sifra_text = ""
       
    for char1 , char2 in pairs(text):
        row1, col1 = divmod(matica.index(char1), 5)
        row2, col2 = divmod(matica.index(char2), 5)
 
        if row1 == row2:
            sifra_text += matica[row1 * 5 + (col1 + 1) % 5]
            sifra_text += matica[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            sifra_text += matica[((row1 + 1) % 5) * 5 + col1]
            sifra_text += matica[((row2 + 1) % 5) * 5 + col2]
        else:
            sifra_text += matica[row1 * 5 + col2]
            sifra_text += matica[row2 * 5 + col1]
 
    return sifra_text


def Desifruj(text1, kluc):
    
    matica = matrix(kluc)
    cisty_text = ""
 
    for char1, char2 in sifra_pairs(text1):
        row1, col1 = divmod(matica.index(char1), 5)
        row2, col2 = divmod(matica.index(char2), 5)
 
        if row1 == row2:
            cisty_text += matica[row1 * 5 + (col1 - 1) % 5]
            cisty_text += matica[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            cisty_text += matica[((row1 - 1) % 5) * 5 + col1]
            cisty_text += matica[((row2 - 1) % 5) * 5 + col2]
        else:
            cisty_text += matica[row1 * 5 + col2]
            cisty_text += matica[row2 * 5 + col1]      
            
    return cisty_text




def spaces (sifra, length):
    return ' '.join(sifra[i:i+length] for i in range(0,len(sifra),length))


def removeX(text):
   for char in text: 
    if text.endswith('X'):
        text = text[:-1]
    return text

def removeW(text):
   for char in text: 
    if text.endswith('W'):
        text = text[:-1]
    return text
                    
    
class Playfair(QMainWindow, Ui_MainWindow):
   
   
   
   def sifruj(self):
       
        text = self.text_edit.text()
        kluc = self.kluc1_edit.text() 
         
        text = text.replace("Q","O")
        text = text.replace("q","o")
        text = text.replace("Ř","R")
        text = text.replace("Ě","E")
        text = text.replace("Š","S")
        text = text.replace("Ž","Z")
        text = text.replace("Ý","Y")
        text = text.replace("Á","A")
        text = text.replace("Č","C")
        text = text.replace("Í","I")
        text = text.replace("É","E")
        text = text.replace("Ť","T")
        text = text.replace("Ď","D")
        text = text.replace("Ň","N")
        text = text.replace("Ú","U")
        text = text.replace("Ů","U")
        text = text.replace("ř","r")
        text = text.replace("ě","e")
        text = text.replace("š","s")
        text = text.replace("ž","z")
        text = text.replace("ý","y")
        text = text.replace("á","a")
        text = text.replace("č","c")
        text = text.replace("í","i")
        text = text.replace("é","e")
        text = text.replace("q","q")
        text = text.replace("ť","t")
        text = text.replace("ď","d")
        text = text.replace("ň","n")
        text = text.replace("ú","u")
        text = text.replace("ů","u")
        text = text.replace(" ","XMEZERAX")
        text = text.replace("0","CDAT")
        text = text.replace("1","BGKL")
        text = text.replace("2","ASVF")
        text = text.replace("3","FCYO")   
        text = text.replace("4","TRLC")
        text = text.replace("5","JPWN")
        text = text.replace("6","KYZJ")
        text = text.replace("7","IDBP")
        text = text.replace("8","ZHLS")
        text = text.replace("9","NCTG")
        text = text.replace("!","")
        text = text.replace("?","")
        text = text.replace(".","")
        text = text.replace(":","")
        text = text.replace(",","")
        text = text.replace("#","")
        text = text.replace("$","")
        text = text.replace("&","")
        text = text.replace("@","")
        text = text.replace("(","")
        text = text.replace(")","")

        kluc = kluc.replace("Q","O")
        kluc = kluc.replace("q","o")
        kluc = kluc.replace("Ř","R")
        kluc = kluc.replace("Ě","E")
        kluc = kluc.replace("Š","S")
        kluc = kluc.replace("Ž","Z")
        kluc = kluc.replace("Ý","Y")
        kluc = kluc.replace("Á","A")
        kluc = kluc.replace("Č","C")
        kluc = kluc.replace("Í","I")
        kluc = kluc.replace("É","E")
        kluc = kluc.replace("Ť","T")
        kluc = kluc.replace("Ď","D")
        kluc = kluc.replace("Ň","N")
        kluc = kluc.replace("Ú","U")
        kluc = kluc.replace("Ů","U")
        kluc = kluc.replace("ř","r")
        kluc = kluc.replace("ě","e")
        kluc = kluc.replace("š","s")
        kluc = kluc.replace("ž","z")
        kluc = kluc.replace("ý","y")
        kluc = kluc.replace("á","a")
        kluc = kluc.replace("č","c")
        kluc = kluc.replace("í","i")
        kluc = kluc.replace("é","e")
        kluc = kluc.replace("ť","t")
        kluc = kluc.replace("ď","d")
        kluc = kluc.replace("ň","n")
        kluc = kluc.replace("ú","u")
        kluc = kluc.replace("ů","u")
        kluc = kluc.replace("0","CDAT")
        kluc = kluc.replace("1","BGLK")
        kluc = kluc.replace("2","ASVF")
        kluc = kluc.replace("3","FCYO")
        kluc = kluc.replace("4","TRLC")
        kluc = kluc.replace("5","JPWN")
        kluc = kluc.replace("6","KYZJ")
        kluc = kluc.replace("7","IDBP")
        kluc = kluc.replace("8","ZHLS")
        kluc = kluc.replace("9","NCTG")
        kluc = kluc.replace("!","")
        kluc = kluc.replace("?","")
        kluc = kluc.replace(".","")
        kluc = kluc.replace(":","")
        kluc = kluc.replace(",","")
        kluc = kluc.replace("#","")
        kluc = kluc.replace("$","")
        kluc = kluc.replace("&","")
        kluc = kluc.replace("@","")
        kluc = kluc.replace("(","")
        kluc = kluc.replace(")","")
        kluc = kluc.replace("'","")
        
      
        sifra = Sifruj(text,kluc)

    
        self.matrix_browser.setText(str(matrix(kluc)))
        self.sifra_browser.setText(str(spaces(sifra,5)))

        self.text_pair_browser.setText(str(pairs(text)))
        self.vstup_text_browser.setText(str(text))

        

        
   def desifruj(self):
        
       
        
        text1 = self.s_text_edit.text()
        kluc = self.kluc2_edit.text()
        
        desif_text = Desifruj(text1,kluc)
        desif_text = removeX(desif_text)
        desif_text = removeW(desif_text)
        desif_text = desif_text.replace("XMEZERAX", " ") 
        desif_text = desif_text.replace("CDAT", "0")
        desif_text = desif_text.replace("BGKL", "1")
        desif_text = desif_text.replace("ASVF", "2")
        desif_text = desif_text.replace("FCYO", "3")
        desif_text = desif_text.replace("TRLC", "4")
        desif_text = desif_text.replace("JPWN", "5")
        desif_text = desif_text.replace("KYZJ", "6")
        desif_text = desif_text.replace("IDBP", "7")
        desif_text = desif_text.replace("ZHLS", "8")
        desif_text = desif_text.replace("NCTG", "9")


        self.matrix1_browser.setText(str(matrix(kluc)))
        self.d_text_browser.setText(str(desif_text))              
        self.sifra_pair_browser.setText(str(sifra_pairs(text1)))
      
        
        
   def vymaz(self):
        self.text_edit.clear()
        self.kluc1_edit.clear()
        self.vstup_text_browser.clear()
        self.sifra_browser.clear()
        self.s_text_edit.clear()
        self.kluc2_edit.clear()
        self.d_text_browser.clear()
        self.matrix_browser.clear()
        self.matrix1_browser.clear()
        self.text_pair_browser.clear()
        self.sifra_pair_browser.clear()
        
   def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.SifrujButton.clicked.connect(self.sifruj)
        self.DesifrujButton.clicked.connect(self.desifruj)
        self.ZmazButton.clicked.connect(self.vymaz)
        
if __name__ == "__main__":
   
    
   app = QApplication(sys.argv)
   window = Playfair()
   window.show()
   sys.exit(app.exec_())






            
