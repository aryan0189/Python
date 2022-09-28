import pickle
import time
from os import remove, rename
def clear():
  for i in range (4):
    print()
def create():
    clear()
    fobj= open("crimerec.dat","wb")
    crimedets=[]
    while True:
        cid = int(input("ID of Criminal: "))
        cname = input("Enter Criminal name: ")
        cadres = input("Enter Criminal Address: ")
        cdob= input("Enter Criminal D.O.B(DD/MM/YYYY): ")
        cpno = input("Enter Criminal Phone No.: ")
        cgen = input("Enter Criminal gender(m/f): ")
        cbg = input("Enter Criminal Blood Group: ")
        cjt= int(input("Enter Jail term (years): "))
        crim = input("Enter Crime commited: ")
        cpd = input("Enter Physical Description (Height/Complexion/Weight/Haircolor/Eyecolor): ")
        fname = input("Enter Family name: ")
        fpno = input("Enter Family Phone No.: ")
        cjs = input("Enter status(Jail/Free): ")
        cjadres= input("Enter Jail address: ")
        crimedets+= [[cid,cname,cadres,cdob,cpno,cgen,cbg,cjt,crim,cpd,fname,fpno,cjs,cjadres]]
        ans= input("Want to add more(n/N) or (y/Y): ")
        if ans in ("n","N"):
            break
    pickle.dump(crimedets,fobj)
    fobj.close()

def displayall():
    clear()
    fin = open("crimerec.dat","rb")
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            print(r)
    except EOFError:
        fin.close()

def searchcid():
    clear()
    fin = open("crimerec.dat","rb")
    srid= int(input("Enter cid to search: "))
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[0] == srid:
                print("Criminal ID: ",r[0])
                print("Criminal Name: ",r[1])
                print("Criminal Address: ",r[2])
                print("Criminal D.O.B: ",r[3])
                print("Criminal Phone No.: ",r[4])
                print("Criminal Gender: ",r[5])
                print("Criminal Blood Group: ",r[6])
                print("Criminal Jail term: ",r[7])
                print("Crime: ",r[8])
                break
        else:
            print("no such record was found")
    except EOFError:
        fin.close()

def searchcname():
    clear()
    fin = open("crimerec.dat","rb")
    srcn = input("Enter Criminal Name to search: ")
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[1] == srcn:
                print("Criminal ID: ",r[0])
                print("Criminal Name: ",r[1])
                print("Criminal Address: ",r[2])
                print("Criminal D.O.B: ",r[3])
                print("Criminal Phone No.: ",r[4])
                print("Criminal Gender: ",r[5])
                print("Criminal Blood Group: ",r[6])
                print("Criminal Jail term: ",r[7])
                print("Crime: ",r[8])
                break
        else:
            print("no such record was found")
    except EOFError:
        fin.close()

def searchadres():
    clear()
    fin = open("crimerec.dat","rb")
    srt= input("Enter Criminal Address to search: ")
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[2] == srt:
                print("Criminal ID: ",r[0])
                print("Criminal Name: ",r[1])
                print("Criminal Address: ",r[2])
                print("Criminal D.O.B: ",r[3])
                print("Criminal Phone No.: ",r[4])
                print("Criminal Gender: ",r[5])
                print("Criminal Blood Group: ",r[6])
                print("Criminal Jail term: ",r[7])
                print("Crime: ",r[8])
                break
        else:
            print("no such record was found")
    except EOFError:
        fin.close()
    
def searchdob():
    clear()
    fin = open("crimerec.dat","rb")
    srt= input("Enter Criminal D.O.B to search: ")
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[3] == srt:
                print("Criminal ID: ",r[0])
                print("Criminal Name: ",r[1])
                print("Criminal Address: ",r[2])
                print("Criminal D.O.B: ",r[3])
                print("Criminal Phone No.: ",r[4])
                print("Criminal Gender: ",r[5])
                print("Criminal Blood Group: ",r[6])
                print("Criminal Jail term: ",r[7])
                print("Crime: ",r[8])
                break
        else:
            print("no such record was found")
    except EOFError:
        fin.close()

def searchpno():
    clear()
    fin = open("crimerec.dat","rb")
    srs= input("Enter Criminal Phone No. to search: ")
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[4] == srs:
                print("Criminal ID: ",r[0])
                print("Criminal Name: ",r[1])
                print("Criminal Address: ",r[2])
                print("Criminal D.O.B: ",r[3])
                print("Criminal Phone No.: ",r[4])
                print("Criminal Gender: ",r[5])
                print("Criminal Blood Group: ",r[6])
                print("Criminal Jail term: ",r[7])
                print("Crime: ",r[8])
                break
        else:
            print("no such record was found")
    except EOFError:
        fin.close()

def searchgen():
    clear()
    fin = open("crimerec.dat","rb")
    srr= input("Enter Criminal Gender to search: ")
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[5] == srr:
                print("Criminal ID: ",r[0])
                print("Criminal Name: ",r[1])
                print("Criminal Address: ",r[2])
                print("Criminal D.O.B: ",r[3])
                print("Criminal Phone No.: ",r[4])
                print("Criminal Gender: ",r[5])
                print("Criminal Blood Group: ",r[6])
                print("Criminal Jail term: ",r[7])
                print("Crime: ",r[8])
                break
        else:
            print("no such record was found")
    except EOFError:
        fin.close()

def searchbg():
    clear()
    fin = open("crimerec.dat","rb")
    srr= input("Enter Criminal Blood Group to search: ")
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[6] == srr:
                print("Criminal ID: ",r[0])
                print("Criminal Name: ",r[1])
                print("Criminal Address: ",r[2])
                print("Criminal D.O.B: ",r[3])
                print("Criminal Phone No.: ",r[4])
                print("Criminal Gender: ",r[5])
                print("Criminal Blood Group: ",r[6])
                print("Criminal Jail term: ",r[7])
                print("Crime: ",r[8])
                break
        else:
            print("no such record was found")
    except EOFError:
        fin.close()

def searchjt():
    clear()
    fin = open("crimerec.dat","rb")
    srr= int(input("Enter Criminal Jail Term to search: "))
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[7] == srr:
                print("Criminal ID: ",r[0])
                print("Criminal Name: ",r[1])
                print("Criminal Address: ",r[2])
                print("Criminal D.O.B: ",r[3])
                print("Criminal Phone No.: ",r[4])
                print("Criminal Gender: ",r[5])
                print("Criminal Blood Group: ",r[6])
                print("Criminal Jail term: ",r[7])
                print("Crime: ",r[8])
                break
        else:
            print("no such record was found")
    except EOFError:
        fin.close()

def searchcrim():
    clear()
    fin = open("crimerec.dat","rb")
    srr= input("Enter Crime to search: ")
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[8] == srr:
                print("Criminal ID: ",r[0])
                print("Criminal Name: ",r[1])
                print("Criminal Address: ",r[2])
                print("Criminal D.O.B: ",r[3])
                print("Criminal Phone No.: ",r[4])
                print("Criminal Gender: ",r[5])
                print("Criminal Blood Group: ",r[6])
                print("Criminal Jail term: ",r[7])
                print("Crime: ",r[8])
                break
        else:
            print("no such record was found")
    except EOFError:
        fin.close()

def count():
    clear()
    fin = open("crimerec.dat","rb")
    ctr=0
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            ctr+=1
    except EOFError:
        fin.close()
    print("Number of Records are ",ctr)

def countcrime():
    clear()
    fin = open("crimerec.dat","rb")
    ctr=0
    bty= input("Enter crime Commited: ")
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[8] == bty:
                ctr+=1
    except EOFError:
        fin.close()
    print("Total crime commited = ",ctr)


def countcname():
    clear()
    fin = open("crimerec.dat","rb")
    ctr=0
    cname= input("Enter Criminal Name: ")
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[1] == cname:
                ctr+=1
    except EOFError:
        fin.close()
    print("Total Criminals with this name: ",ctr)


def countgen():
    clear()
    fin = open("crimerec.dat","rb")
    ctr=0
    nst= input("Enter Gender: ")
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[5] == nst:
                ctr+=1
    except EOFError:
        fin.close()
    print("Total number of Criminals of "+nst+" Gender = ",ctr)


def countjt():
    clear()
    fin = open("crimerec.dat","rb")
    ctr=0
    ttp= int(input("Enter Jail Term: "))
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[7] == ttp:
                ctr+=1
    except EOFError:
        fin.close()
    print("Total number of Criminals from years = ",ctr)

def countbg():
    clear()
    fin = open("crimerec.dat","rb")
    ctr=0
    ttp= input("Enter Blood Group: ")
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            if r[6] == ttp:
                ctr+=1
    except EOFError:
        fin.close()
    print("Total number of Criminals with "+ttp+" Blood Group = ",ctr)



def editcid():
    clear()
    fin = open("crimerec.dat","rb+")
    cid= int(input("Enter Criminal ID to edit: "))
    ctr=0
    try:
        crecs= pickle.load(fin)
        for r in crecs:     
          if r[0]==cid:
              ctr+=1
              r[0]= int(input("Enter Criminal ID: "))
              r[1]= input("Enter Criminal Name: ")
              r[2]= input("Enter Criminal Address: ")
              r[3]= input("Enter Criminal D.O.B: ")
              r[4]= input("Enter Criminal Phone No.: ")
              r[5]= input("Enter Criminal Gender: ")
              r[6]= input("Enter Criminal Blood Group: ")
              r[7]= int(input("Enter Criminal Jail Term: "))
              r[8]= input("Enter Crime: ")
              break
        if ctr==0:
              print("Criminal with this ID was not found")
        else:
              fin.seek(0)
              pickle.dump(crecs,fin)
              print("data updated inside the file")
              fin.close()
              
    except EOFError:
      fin.close()
        


def editcname():
    clear()
    fin = open("crimerec.dat","rb+")
    cname= input("Enter Criminal name to edit: ")
    ctr=0
    try:
        crecs= pickle.load(fin)
        for r in crecs:
          if r[1]== cname:
              ctr+=1
              r[0]= int(input("Enter Criminal ID: "))
              r[1]= input("Enter Criminal Name: ")
              r[2]= input("Enter Criminal Address: ")
              r[3]= input("Enter Criminal D.O.B: ")
              r[4]= input("Enter Criminal Phone No.: ")
              r[5]= input("Enter Criminal Gender: ")
              r[6]= input("Enter Criminal Blood Group: ")
              r[7]= int(input("Enter Criminal Jail Term: "))
              r[8]= input("Enter Crime: ")
              break
        if ctr==0:
              print("Criminal with this name was not found")
        else:
              fin.seek(0)
              pickle.dump(crecs,fin)
              print("data updated inside the file")
              fin.close()
              
    except EOFError:
      fin.close()
 
def append():
    clear()
    print("Enter the Record to be inserted")
    cid = int(input("ID of Criminal: "))
    cname = input("Enter Criminal name: ")
    cadres = input("Enter Criminal Address: ")
    cdob= input("Enter Criminal D.O.B(DD/MM/YYYY): ")
    cpno = input("Enter Criminal Phone No.: ")
    cgen = input("Enter Criminal gender(m/f): ")
    cbg = input("Enter Criminal Blood Group:  ")
    cjt= int(input("Enter Jail term (years): "))
    crim = input("Enter Crime commited: ")
    cpd = input("Enter Physical Description (Height/Complexion/Weight/Haircolor/Eyecolor): ")
    fname = input("Enter Family name: ")
    fpno = input("Enter Family Phone No.: ")
    cjs = input("Enter status(Jail/Free): ")
    cjadres= input("Enter Jail address: ")
    newdets=[cid,cname,cadres,cdob,cpno,cgen,cbg,cjt,crim,cpd,fname,fpno,cjs,cjadres]
    fin = open("crimerec.dat","rb+")
    try:
        crecs= pickle.load(fin)
        crecs.append(newdets)
        fin.seek(0)
        pickle.dump(crecs,fin)
        fin.close()
    except EOFError:
        fin.close()

def  insertcid():
    clear()
    fin = open("crimerec.dat","rb+")
    cid= int(input("Enter Criminal ID to add: "))
    ctr, found = 0,"n"
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            ctr+=1
            if r[0] ==cid:
                cid = int(input("ID of Criminal: "))
                cname = input("Enter Criminal name: ")
                cadres = input("Enter Criminal Address: ")
                cdob= input("Enter Criminal D.O.B(DD/MM/YYYY): ")
                cpno = input("Enter Criminal Phone No.: ")
                cgen = input("Enter Criminal gender(m/f): ")
                cbg = input("Enter Criminal Blood Group:  ")
                cjt= int(input("Enter Jail term (years): "))
                crim = input("Enter Crime commited: ")
                cpd = input("Enter Physical Description (Height/Complexion/Weight/Haircolor/Eyecolor): ")
                fname = input("Enter Family name: ")
                fpno = input("Enter Family Phone No.: ")
                cjs = input("Enter status(Jail/Free): ")
                cjadres= input("Enter Jail address: ")
                newdets= [cid,cname,cadres,cdob,cpno,cgen,cbg,cjt,crim,cpd,fname,fpno,cjs,cjadres]
                crecs.insert(ctr-1,newdets)
                found = "y"
                break
            else:
                print("record was not found")
        if found=="y":
            fin.seek(0)
            pickle.dump(crecs,fin)
            fin.close()
    except EOFError:
        fin.close()


def deleterec():
    clear()
    fin = open("crimerec.dat","rb+")
    pos= int(input("Enter record no to delete: "))
    try:
        crecs= pickle.load(fin)
        crecs.pop(pos-1)
        fin.seek(0)
        pickle.dump(crecs,fin)
        print("data updated inside the file")
        fin.close()
    except EOFError:
        fin.close()

def deletecid():
    clear()
    cid=int(input("Enter Criminal ID to delete: "))
    fin = open("crimerec.dat","rb+")
    ctr,found= 0,"n"
    try:
        crecs= pickle.load(fin)
        for r in crecs:
            ctr+=1
            if r[0] ==cid:
                crecs.pop(ctr-1)
                found = "y"
                break
        if found =="y":
            fin.seek(0)
            pickle.dump(crecs,fin)
            print("data updated inside the file")
            fin.close()
    except EOFError:
        fin.close()
kl='''

                              =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                              :                                             :
                              :    WELCOME TO CRIMINAL RECORD MANAGEMENT    :
                              :    -------------------------------------    :
                              :                                             :
                              =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
print(kl)
kb='''
NOTE: This is just a prototype of the Criminal Record Management System.
Aryan Agrawal - 14636901
Delhi Public School, Vasant Kunj
Computer Science
'''
for i in kb:
    print(i,end="")
    time.sleep(0.02)
clear()
while True:
    mdd='''\n
 1. Create Criminal Record File :-\n
 2. Display all the Criminal details :-\n
 3. Search on  the basis of Criminal Id :-\n
 4. Search on the basis of Criminal Name :-\n
 5. Search on the basis of Criminal Address :-\n
 6. Search on the basis of Criminal D.O.B :-\n
 7. Search on the basis of Criminal Phone No. :-\n
 8. Search on the basis of Criminal Gender :-\n
 9. Search on the basis of Criminal Blood Group :-\n
 10.Search on the basis of Criminal Jail Term :-\n
 11.Search on the basis of Crime committed :-\n
 12.Count all records :-\n
 13.Count on the basis of Crime committed :-\n
 14.Count on the basis of Criminal Name :-\n
 15.Count on the basis of Criminal Gender :-\n
 16.Count on the basis of Criminal Jail Term :-\n
 17.Count on the basis of Criminal Blood Group :-\n
 18.Edit Criminal Identification number :-\n
 19.Edit on the basis of Criminal Name :-\n
 20.Insert on the basis of Criminal identification number :-\n
 21.Append new Criminal Details :-\n
 22.Delete a record :-\n
 23.Delete on the basis of Criminal identification number :-

 '''
    print(mdd)
    
##    for i in mdd:
##      print(i,end="")
##      time.sleep(0.00000000000009999999998899)

    ch=int(input("\n  Enter your choice : "))
    if ch==1:
        create()
    elif ch==2:
        displayall()
    elif ch==3:
        searchcid()
    elif ch==4:
        searchcname()
    elif ch==5:
        searchadres()
    elif ch==6:
        searchdob()
    elif ch==7:
        searchpno()
    elif ch==8:
        searchgen()
    elif ch==9:
        searchbg()
    elif ch==10:
        searchjt()
    elif ch==11:
        searchcrim()
    elif ch==12:
        count()
    elif ch==13:
        countcrime()
    elif ch==14:
        countcname()
    elif ch==15:
        countgen()
    elif ch==16:
        countjt()
    elif ch==17:
        countbg()
    elif ch==18:
        editcid()
    elif ch==19:
        editcname()
    elif ch==20:
        insertcid()
    elif ch==21:
        append()
    elif ch==22:
        deleterec()
    elif ch==23:
        deletecid()
    else:
        print("wrong choice")
    ans=input("\n want to continue(n/N)or(y/Y): ")
    if ans in("n","N"):
        break
