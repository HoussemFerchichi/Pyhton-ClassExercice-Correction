from numpy import*
class User :
    nom:str
    prenom:str
    Code:str
t=zeros(50,dtype=User)

def saisie():
    n=int(input("donner n:"))
    return n

def remplirUser(n):
    for i in range(n):
        t[i]=User()
        t[i].nom=(input("entrer le nom :"))
        t[i].prenom=(input("entrer le prenom :"))
        t[i].Code=(input("entrer le code :"))
    return t
def enregistrer(n,t):
    f=open("user.dat","wb")
    for i in range(n):
        f.write((t[i].nom+' '+t[i].prenom+' '+t[i].Code + "\n").encode("ascii"))
    f.close()
    
def affiche(n,size):
    f=open("user.dat","rb")
    for i in range(n):
        ch = f.readline().decode("ascii")
        enregistrer2(ch,n,size)
    f.close() 
    
def enregistrer2(ch,n,size):
    mot=array([int]*20)
    i=-1
    ch1=ch
    while (ch1.find(" ")!=-1):
        i=i+1
        mot[i]=ch1[0:ch1.find(" ")]
        ch1=ch1[ch1.find(" ")+1:len(ch)]
    mot[i+1]=ch1[0:ch1.find("\n")]
    correction(mot,i+1,n,ch)
    Matrice(str(mot[i+1]),n,size)

def correction(mot,m,n,ch):
    mot1=array([int]*m)
    for i in range(m):
        mot1[i]=mot[i][0].upper()+mot[i][1:len(mot[i])]
    Save(mot1[0],mot1[1])
    

def Save(ch,ch1):
    f2 = open("output.txt","a")
    f2.write(str(ch) + " "+ str(ch1) + "\n")
    f2.close()

def biggestlen():
    f=open("user.dat","rb")
    ch=(f.readline()).decode("ascii")
    for i in range(n-1):
        ch1 = (f.readline()).decode("ascii")
        if (len (ch1)>len(ch)):
            ch = ch1
    f.close() 
    return(findbiggestcode(ch))

def findbiggestcode(ch):
    i=-1
    ch1=ch
    while (ch1.find(" ")!=-1):
        i=i+1
        k=ch1[0:ch1.find(" ")]
        ch1=ch1[ch1.find(" ")+1:len(ch)]
    while(ch1[-1]== " ")or (ch1[-1]=="\n"):
        ch1 = ch1[:-1]
    return len (ch1)
    
mat = []
def Matrice(ch,n,size):
    global mat
    if (mat== []):
        for i in range (n):
            m=[]
            for j in range (size):
                m.append(j)
            mat.append(m)
    for i in range (n):
        for j in range(size):
            if (j<len(ch)):
                mat[i][j]= ch[j]
            else:
                mat[i][j]= "*"
    print(mat)

n = saisie()
t = remplirUser(n)
enregistrer(n,t)
ch = biggestlen() 
affiche(n,ch)