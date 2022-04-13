# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 22:23:03 2022

@author: mathi
"""
import pyvisa as visa
import numpy as np
import time
from graphe_serie_donnes import *
import os

rm=visa.ResourceManager()

print(rm.list_resources())
myScope = rm.open_resource('USB0::0x0957::0x17A8::MY60472399::0::INSTR')
myGBF=rm.open_resource('USB0::0x0957::0x0407::MY44060253::0::INSTR')
print(myScope.query("*IDN?"))
print(myGBF.query('*IDN?'))


def setupmyScope():
    myScope.write("*rst")
    print("reset Oscillo done")
    myScope.timeout = 10000
    print ("timeout oscillo set to 10 000")
    myScope.write(":ACQuire:TYPE AVERage")
    myScope.write(":ACQuire:COMPlete 100")
    myScope.write(":ACQuire:COUNt 4")
    average=myScope.query_ascii_values(":ACQuire:COUNt?")
    print( "Average number : {}".format(average) )
    myScope.write(":TIMebase:DELay 0")
    myScope.write(":TIMebase:REFerence CENTer")
    myScope.write(":TRIGger:SWEep NORMal") #trigger
    myScope.write(":TRIGger:LEVel -0.02")
    print("Trig level {}".format(myScope.query_ascii_values(":TRIGger:LEVel?")))
    myScope.write(":TRIGger:SLOPe POSitive")
    myScope.write(":ACQuire:TYPE NORMal")
    
    voltpardiv1=2.6/8
    volt8div1=voltpardiv1*8
    voltpardiv2=2.4/8
    volt8div2=voltpardiv2*8
    
    myScope.write (":CHANnel1:RANGe {}".format(volt8div1))
    print ("Vert Ch1 range set to {}/8 /div ".format(myScope.query_ascii_values(":CHANnel1:RANGe?")) )
    myScope.write (":CHANnel1:OFFSet 0")
    print ("Offset Ch1 set to {}".format(myScope.query_ascii_values(":CHANnel1:OFFSet?")) )
    myScope.write (":CHANnel2:RANGe {}".format(volt8div2))
    print ("Vert Ch2 range set to {}/8 /div".format(myScope.query_ascii_values(":CHANnel2:RANGe?")) )
    myScope.write (":CHANnel2:OFFSet 0")
    print ("Offset Ch2 set to {}".format(myScope.query_ascii_values(":CHANnel2:OFFSet?")) )
    print("Setup done")

def setupGBF():
    myGBF.write("*rst")
    print("reset GBF done")
    myGBF.timeout = 10000
    print ("timeout GBF set to 10 000")
    myGBF.write("FUNCtion SINusoid")
    myGBF.write("FREQuency 2500")
    print("frequency set to {}".format(myGBF.query_ascii_values("FREQuency?")))
    myGBF.write("VOLTage 1")
    print("Vpp set to {}".format(myGBF.query_ascii_values("VOLTage?")))
    myGBF.write("VOLTage:OFFSet 0")
    print("offset set to {}".format(myGBF.query_ascii_values("VOLTage:OFFSet?")))
    myGBF.write("OUTPut ON")
    
    
def setfreqencyGBF(freq):
    f=str(freq)
    myGBF.write("FREQuency {}".format(f))
    print("frequency set to {}".format(myGBF.query_ascii_values("FREQuency?")))
    

def interfacemyScope():

    
    freq=float(myScope.query_ascii_values(":MEASure:FREQuency? CHANnel1")[0])
    
    if freq>9.9*10**20:
        myScope.write (":TIMebase:MODE MAIN")
        myScope.write (":TIMebase:RANGe 2")
        print("Horiz range {}/10 sec/div".format(myScope.query_ascii_values(":TIMebase:RANGe?")))
        freq=float(myScope.query_ascii_values(":MEASure:FREQuency? CHANnel1")[0])
    T=1/freq
    tempspardiv=2*T/10
    temps10div=tempspardiv*10
    myScope.write (":TIMebase:RANGe {}".format(temps10div))
    print("Horiz range {}/10 sec/div".format(myScope.query_ascii_values(":TIMebase:RANGe?")))
        

       
    
    
    Ue=float(myScope.query_ascii_values(":MEASure:VPP? CHANnel1")[0])
    Us=float(myScope.query_ascii_values(":MEASure:VPP? CHANnel2")[0])
    

    return Ue,Us
    



def acquiremyScope()  :
    


    #myScope.write(":MEASure:SOURce CHANnel1")
    #qresult = myScope.query_ascii_values(":MEASure:SOURce?")
    #print( "Measure source : {}".format(qresult) )
    Ue=float(myScope.query_ascii_values(":MEASure:VPP? CHANnel1")[0])
    print( "Ue : {}".format(Ue))
    lUe=list()
    time.sleep(0.5)
    for i in range(4):
        lUe.append(float(myScope.query_ascii_values(":MEASure:VPP? CHANnel1")[0]))
        time.sleep(0.5)
    DUe=max(lUe)-min(lUe)
    print( "DUe : {}".format(DUe) )
    Us=float(myScope.query_ascii_values(":MEASure:VPP? CHANnel2")[0])
    print( "Us : {}".format(Us) )
    lUs=list()
    time.sleep(0.5)
    for i in range(4):
        lUs.append(float(myScope.query_ascii_values(":MEASure:VPP? CHANnel2")[0]))
        time.sleep(0.5)
    DUs=max(lUs)-min(lUs)
    print( "DUs : {}".format(DUs) )
    freq=float(myScope.query_ascii_values(":MEASure:FREQuency? CHANnel1 ")[0])
    print( "Frequence : {}".format(freq) )
    lfreq=list()
    time.sleep(0.5)
    for i in range(4):
        lfreq.append(float(myScope.query_ascii_values(":MEASure:FREQuency? CHANnel1")[0]))
        time.sleep(0.5)
    Dfreq=max(lfreq)-min(lfreq)
    print( "Dfreq : {}".format(Dfreq) )
    phase=float(myScope.query_ascii_values(":MEASure:PHASe?")[0])
    print( "phase : {}".format(phase))
    lphase=list()
    time.sleep(0.5)
    for i in range(4):
        phase=myScope.query_ascii_values(":MEASure:PHASe?")[0]
        if phase>300:
            phase=phase-360
            lphase.append(phase)
        else:
            lphase.append(phase)
        time.sleep(0.5)
    Dphase=max(lphase)-min(lphase)
    print( "Dphase : {}".format(Dphase) )
    return [freq, Dfreq, Ue, DUe, Us, DUs,  phase, Dphase]

def acquiremyScope2()  :
    Ue=float(myScope.query_ascii_values(":MEASure:VRMS? CHANnel1")[0])
    #print( "Ue : {}".format(Ue))            
    Us=float(myScope.query_ascii_values(":MEASure:VRMS? CHANnel2")[0])
    #print( "Us : {}".format(Us) )       
    freq=float(myScope.query_ascii_values(":MEASure:FREQuency? CHANnel1 ")[0])
    #print( "Frequence : {}".format(freq) )       
    phase=float(myScope.query_ascii_values(":MEASure:PHASe?")[0])
    
    #print( "phase : {}".format(phase))   
    myScope.write(":MEASure:STATistics MEAN STDDev COUNt")
    
    print(myScope.query_ascii_values(":MEASure:RESults?",container=np.array))
    
    while True:
        if float(myScope.query_ascii_values(":MEASure:RESults?")[2])>5:
            print(float(myScope.query_ascii_values(":MEASure:RESults?")[2]))
            break
        else:
            time.sleep(0.1)
            print(float(myScope.query_ascii_values(":MEASure:RESults?")[2]))
    Ue=float(myScope.query_ascii_values(":MEASure:RESults?")[0])
    print( "Ue : {}".format(Ue))          
    DUe=float(myScope.query_ascii_values(":MEASure:RESults?")[1])
    print( "DUe : {}".format(DUe) )
    Us=float(myScope.query_ascii_values(":MEASure:RESults?")[3])
    print( "Us : {}".format(Us) )
    DUs=float(myScope.query_ascii_values(":MEASure:RESults?")[4])
    print( "DUs : {}".format(DUs) )
    freq=float(myScope.query_ascii_values(":MEASure:RESults?")[6])
    print( "Frequence : {}".format(freq) )   
    Dfreq=float(myScope.query_ascii_values(":MEASure:RESults?")[7])   
    print( "Dfreq : {}".format(Dfreq) )
    phase=float(myScope.query_ascii_values(":MEASure:RESults?")[9]) 
    if phase>300:
        phase=phase-360
    print( "phase : {}".format(phase)) 
    Dphase=float(myScope.query_ascii_values(":MEASure:RESults?")[10]) 
    print( "Dphase : {}".format(Dphase) )
    myScope.write (":MEASure:STATistics:RESet")
    
    return [freq, Dfreq, Ue, DUe, Us, DUs,  phase, Dphase]
            
 
        



#main program
setupGBF()
setupmyScope()
while True:   
    R=input("Entrer valeur R initiale")
    
    answer=input("confirmer 'y' sinon 'n': ")
    if answer=='y':
        break
    
subseuil=input("taper 'y' ou enter si c inf a 0.125% ou non : ")
if subseuil=='y':
    sweep=[50,100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000,5000000]
else:

    sweep=[1,2,5,10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000,2000000,5000000]
data=np.empty((len(sweep),9))

for i in range(len(sweep)):    
    setfreqencyGBF(sweep[i])
    Ue,Us=interfacemyScope()
    q=Us/Ue
    print(q)
    while q>0.7 or q<0.02:
        
        if q>0.7:
            
            while True:   
                R=input("La résistance est trop grande pour cette fréquence. Entrer valeur R")
                answer=input("confirmer 'y' sinon 'n': ")
                if answer=='y':
                    break
                
            Ue,Us=interfacemyScope()
            q=Us/Ue
            
        if q<0.02:
            while True:   
                R=input("La résistance est trop petite pour cette fréquence. Entrer valeur R")
                answer=input("confirmer 'y' sinon 'n': ")
                if answer=='y':
                    break
            Ue,Us=interfacemyScope()
            q=Us/Ue
            
    ligne=acquiremyScope()
    ligne.insert(0,R)
    data[i]=ligne
    #input("Enter pour mesure suivante")

filename=input('Nom du fichier pour cette série de données (sans .txt) :' )  
parent_dir=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation"
path=os.path.join(parent_dir, filename)
os.mkdir(path+'_dir')
path2=path+'_dir\{}.txt'.format(filename)
np.savetxt(path2, data)
calculs(filename)
graph(filename)




