# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 23:22:04 2022

@author: mathi
"""
import numpy as np
import os
from os.path import exists
from os import listdir
import matplotlib.pyplot as plt



def calculs(filename):
    

    path=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}.txt".format(filename,filename)


    with open(path) as file :
        l=[]
        liste=[line.strip().split('/n')[0] for line in file] 
        
        for j in range(len(liste)):
            l2=liste[j].split(' ')
            line=[]
            line=[float(a) for a in l2]
            l.append(line)
    array=np.array(l)

    indR=0
    indfreq=1
    indDfreq=2
    indUe=3
    indDUe=4
    indUs=5
    indDUs=6
    indphase=7
    indDphase=8
    calculs=np.empty((len(liste),30))
    
        
    
    L=3.3*10**(-3)
    DL=10**(-3)
    DS=7.85*10**(-5)
    S=7.85*10**(-3)
    C=114*10**(-12)
    DC=10*10**(-12)
    R0=10**6
    for i in range(len(liste)):
        sin=np.sin((np.pi/180)*array[i,indphase])
        cos=np.cos((np.pi/180)*array[i,indphase])
        R=array[i,indR]
        f=array[i,indfreq]
        Ue=array[i,indUe]
        Us=array[i,indUs]
        DUe=array[i,indDUe]
        DUs=array[i,indDUs]
        Dphase=array[i,indDphase]
        Df=array[i,indDfreq]
        DR=R*(5/100)
        log10f=np.log10(f)
        Dlog10f=Df/(f*np.log(10))
        q=Ue/Us
        Dq=q*((DUe/Ue)**2+(DUs/Us)**2)**(1/2)
        Req=q*cos
        DReq=((cos*Dq)**2+((np.pi/180)*q*sin*Dphase)**2)**1/2
        Imq=q*sin
        DImq=((sin*Dq)**2+((np.pi/180)*q*cos*Dphase)**2)**1/2
        Rplus=R+R0
        Rfois=R*R0
        omega=2*np.pi*f
        A=Rfois/(Rplus**2+Rfois*C*omega)
        E=Rplus*(Req-1)+Imq*Rfois*omega*C
        ReZ=A*E
        DRA=(R0*(Rplus**2+(Rfois*omega*C)**2)-2*Rfois*(Rplus+R*(R0*omega*C)**2))/((Rplus**2+(Rfois*omega*C)**2)**2)
        DCA=(-Rfois*((Rfois*omega)**2)*2*C)/((Rplus**2+(Rfois*omega*C)**2)**2)
        DRE=q*cos-1+q*sin*R0*omega*C
        DphiE=(np.pi/180)*(-q*sin*Rplus+q*cos*Rfois*omega*C)
        DqE=cos*Rplus+sin*Rfois*omega*C
        DCE=q*sin*Rfois*omega
        DRReZ=DRA*E+A*DRE
        DphiReZ=A*DphiE
        DqReZ=A*DqE
        DCReZ=DCA*E+A*DCE
        DReZ=((DRReZ*DR)**2+(DphiReZ*Dphase)**2+(DqReZ*Dq)**2+(DCReZ*DC)**2)**(1/2)
        F=Imq*Rplus+Rfois*C*omega*(1-Req)
        ImZ=A*F
        DRF=q*sin+R0*omega*C*(1-q*cos)
        DphiF=(np.pi/180)*(q*cos*Rplus-Rfois*omega*C*q*sin)
        DqF=sin*Rplus-Rfois*omega*C*cos
        DCF=Rfois*omega*(1-q*cos)
        DRImZ=DRA*F+A*DRF
        DphiImZ=A*DphiF
        DqImZ=A*DqF
        DCImZ=DCA*F+A*DCF
        DImZ=((DRImZ*DR)**2+(DRImZ*Dphase)**2+(DqImZ*Dq)**2+(DCImZ*DC)**2)**(1/2)
        argZ=np.arctan2(ImZ,ReZ)*(180/np.pi)
        B=ImZ/ReZ
        DRB=(DRImZ*ReZ-ImZ*DRReZ)/(ReZ**2)
        DphiB=(DphiImZ*ReZ-ImZ*DphiReZ)/(ReZ**2)
        DqB=(DqImZ*ReZ-ImZ*DqReZ)/(ReZ**2)
        DCB=(DCImZ*ReZ-ImZ*DCReZ)/(ReZ**2)
        DRargZ=(DRB*(180/np.pi))/(1+B**2)
        DphiargZ=(DphiB*(180/np.pi))/(1+B**2)
        DqargZ=(DqB*(180/np.pi))/(1+B**2)
        DCargZ=(DCB*(180/np.pi))/(1+B**2)
        DargZ=((DRargZ*DR)**2+(DphiargZ*Dphase)**2+(DqargZ*Dq)**2+(DCargZ*DC)**2)**(1/2)
        modZ=(ReZ**2+ImZ**2)**(1/2)
        log10modZ=np.log10(modZ)
        DRmodZ=(DRReZ*ReZ+DRImZ*ImZ)/(modZ)
        DphimodZ=(DphiReZ*ReZ+DphiImZ*ImZ)/(modZ)
        DqmodZ=(DqReZ*ReZ+DqImZ*ImZ)/(modZ)
        DCmodZ=(DCReZ*ReZ+DCImZ*ImZ)/(modZ)
        DmodZ=((DRmodZ*DR)**2+(DphimodZ*Dphase)**2+(DqmodZ*Dq)**2+(DCmodZ*DC)**2)**(1/2)
        Dlog10modZ=abs(DmodZ/(modZ*np.log(10)))
        epsx=-(L*ImZ)/(S*modZ**2*omega) 
        DRC=(DRImZ*modZ**2-ImZ*2*DRmodZ*modZ)/(modZ)**4 #C=ImZ/modZ
        DphiC=(DphiImZ*modZ**2-ImZ*2*DphimodZ*modZ)/(modZ)**4
        DqC=(DqImZ*modZ**2-ImZ*2*DqmodZ*modZ)/(modZ)**4
        DCC=(DCImZ*modZ**2-ImZ*2*DCmodZ*modZ)/(modZ)**4
        DRepsx=(-L/(S*omega))*DRC
        Dphiepsx=(-L/(S*omega))*DphiC
        Dqepsx=(-L/(S*omega))*DqC
        DCepsx=(-L/(S*omega))*DCC
        Depsx=(((epsx/L)*DL)**2+((epsx/S)*DS)**2+(DRepsx*DR)**2+(Dphiepsx*Dphase)**2+(Dqepsx*Dq)**2+(DCepsx*DC)**2)**(1/2)
        epsy=(L*ReZ)/(S*modZ**2*omega)
        DRD=(DRReZ*modZ**2-ReZ*2*DRmodZ*modZ)/(modZ)**4 #D=ReZ/modZ
        DphiD=(DphiReZ*modZ**2-ReZ*2*DphimodZ*modZ)/(modZ)**4
        DqD=(DqReZ*modZ**2-ReZ*2*DqmodZ*modZ)/(modZ)**4
        DCD=(DCReZ*modZ**2-ReZ*2*DCmodZ*modZ)/(modZ)**4
        DRepsy=(L/(S*omega))*DRD
        Dphiepsy=(L/(S*omega))*DphiD
        Dqepsy=(L/(S*omega))*DqD
        DCepsy=(L/(S*omega))*DCD
        Depsy=(((epsy/L)*DL)**2+((epsy/S)*DS)**2+(DRepsy*DR)**2+(Dphiepsy*Dphase)**2+(Dqepsy*Dq)**2+(DCepsy*DC)**2)**(1/2)
        log10epsx=np.log10(epsx)
        Dlog10epsx=abs(Depsx/(epsx*np.log(10)))
        log10epsy=np.log10(epsy)
        Dlog10epsy=abs(Depsy/(epsy*np.log(10)))
        angperte=epsy/epsx
        DRDangperte=(DRepsy*epsx-epsy*DRepsx)/(epsx)**2
        DphiDangperte=(Dphiepsy*epsx-epsy*Dphiepsx)/(epsx)**2
        DqDangperte=(Dqepsy*epsx-epsy*Dqepsx)/(epsx)**2
        DCDangperte=(DCepsy*epsx-epsy*DCepsx)/(epsx)**2
        Dangperte=((DRDangperte*DR)**2+(DphiDangperte*Dphase)**2+(DqDangperte*Dq)**2+(DCDangperte*DC)**2)**(1/2)
        log10angperte=np.log10(angperte)
        Dlog10angperte=abs(Dangperte/(angperte*np.log(10)))
    
        calculs[i,:]=[f,Df,log10f,Dlog10f,q,Dq,Req,DReq,Imq,DImq,ReZ,DReZ,ImZ,DImZ,argZ,DargZ,modZ,DmodZ,log10modZ,Dlog10modZ,epsx,Depsx,epsy,Depsy,log10epsx,Dlog10epsx,log10epsy,Dlog10epsy,log10angperte,Dlog10angperte]
    path2=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}_calculs.txt".format(filename,filename)
    np.savetxt(path2, calculs)
    
def calculmoy() :
    blocklen=[]
    filenameliste=[]
    G=[0,0.25,0.5,0.75,1,1.5,3,2.5,5,10]
    pourcentage=[0.125,0.25,0.5,1]
    for i in pourcentage:
        for j in G:
            for k in range(1,7):
                filename='{}%_{}g_{}'.format(i,j,k)
                path=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}.txt".format(filename,filename)
                if exists(path)==True:
                    filenameliste.append(filename)
                else:
                    blocklen.append(k-1)
                    break
    blocklen=[i for i in blocklen if i != 0]
           
    for i in range (1,5):
        filenameliste.append('air_{}'.format(i))
    blocklen.append(4)   
    s=0

    for i in blocklen:

        
        listeblock=[]
        
        for j in range(i):            
            path=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}_calculs.txt".format(filenameliste[s+j],filenameliste[s+j])
            with open(path) as file :
                l=[]
                liste=[line.strip().split('/n')[0] for line in file] 
                for b in range(len(liste)):
                    l2=liste[b].split(' ')
                    line=[]
                    line=[float(a) for a in l2]
                    l.append(line)

                    
                    
                
                listeblock.append(l)
             
        indfreq,indDfreq,indlog10freq,indDlog10freq,indq,indDq,\
        indReq,indDReq,indImq,indDImq,indReZ,indDReZ,indImZ,indDImZ,indargZ,\
        indDargZ,indmodZ,indDmodZ,indlog10modZ,indDlog10modZ,indepsx,indDepsx,indepsy,indDepsy,\
        indlog10epsx,indDlog10epsx,indlog10epsy,indDlog10epsy,\
        indlog10angperte,indDlog10angperte=0,1,2,3,4,5,6,7,8,9,10\
        ,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
         


        
        listeblock=np.array(listeblock)
        #print(listeblock.shape)
        calculsmoy=np.empty((len(l),30))  
               
        for k in range(len(l)):
            freqliste=listeblock[:,k,indfreq]
            freqliste = [x for x in freqliste if np.isnan(x) == False]
            Dfreqliste=listeblock[:,k,indDfreq]
            Dfreqliste = [x for x in Dfreqliste if np.isnan(x) == False]
            log10freqliste=listeblock[:,k,indlog10freq]
            log10freqliste = [x for x in log10freqliste if np.isnan(x) == False]
            Dlog10freqliste=listeblock[:,k,indDlog10freq]
            Dlog10freqliste = [x for x in Dlog10freqliste if np.isnan(x) == False]
            qliste=listeblock[:,k,indq]
            qliste = [x for x in qliste if np.isnan(x) == False]
            Dqliste=listeblock[:,k,indDq]
            Dqliste = [x for x in Dqliste if np.isnan(x) == False]
            Reqliste=listeblock[:,k,indReq]
            Reqliste = [x for x in Reqliste if np.isnan(x) == False]
            DReqliste=listeblock[:,k,indDReq]
            DReqliste = [x for x in DReqliste if np.isnan(x) == False]
            Imqliste=listeblock[:,k,indImq]
            Imqliste = [x for x in Imqliste if np.isnan(x) == False]
            DImqliste=listeblock[:,k,indDImq]
            DImqliste = [x for x in DImqliste if np.isnan(x) == False]
            ReZliste=listeblock[:,k,indReZ]
            ReZliste = [x for x in ReZliste if np.isnan(x) == False]
            DReZliste=listeblock[:,k,indDReZ]
            DReZliste = [x for x in DReZliste if np.isnan(x) == False]
            ImZliste=listeblock[:,k,indImZ]
            ImZliste = [x for x in ImZliste if np.isnan(x) == False]
            DImZliste=listeblock[:,k,indDImZ]
            DImZliste = [x for x in DImZliste if np.isnan(x) == False]
            argZliste=listeblock[:,k,indargZ]
            argZliste = [x for x in argZliste if np.isnan(x) == False]
            DargZliste=listeblock[:,k,indDargZ]
            DargZliste = [x for x in DargZliste if np.isnan(x) == False]
            modZliste=listeblock[:,k,indmodZ]
            modZliste = [x for x in modZliste if np.isnan(x) == False]
            DmodZliste=listeblock[:,k,indDmodZ]
            DmodZliste = [x for x in DmodZliste if np.isnan(x) == False]
            log10modZliste=listeblock[:,k,indlog10modZ]
            log10modZliste = [x for x in log10modZliste if np.isnan(x) == False]
            Dlog10modZliste=listeblock[:,k,indDlog10modZ]
            Dlog10modZliste = [x for x in Dlog10modZliste if np.isnan(x) == False]
            epsxliste=listeblock[:,k,indepsx]
            epsxliste = [x for x in epsxliste if np.isnan(x) == False]
            Depsxliste=listeblock[:,k,indDepsx]
            Depsxliste = [x for x in Depsxliste if np.isnan(x) == False]
            epsyliste=listeblock[:,k,indepsy]
            epsyliste = [x for x in epsyliste if np.isnan(x) == False]
            Depsyliste=listeblock[:,k,indDepsy]
            Depsyliste = [x for x in Depsyliste if np.isnan(x) == False]
            log10epsxliste=listeblock[:,k,indlog10epsx]
            log10epsxliste = [x for x in log10epsxliste if np.isnan(x) == False]
            Dlog10epsxliste=listeblock[:,k,indDlog10epsx]
            Dlog10epsxliste = [x for x in Dlog10epsxliste if np.isnan(x) == False]
            log10epsyliste=listeblock[:,k,indlog10epsy]
            log10epsyliste = [x for x in log10epsyliste if np.isnan(x) == False]
            Dlog10epsyliste=listeblock[:,k,indDlog10epsy]
            Dlog10epsyliste = [x for x in Dlog10epsyliste if np.isnan(x) == False]
            log10angperteliste=listeblock[:,k,indlog10angperte]
            log10angperteliste = [x for x in log10angperteliste if np.isnan(x) == False]
            Dlog10angperteliste=listeblock[:,k,indDlog10angperte]
            Dlog10angperteliste = [x for x in Dlog10angperteliste if np.isnan(x) == False]
            
            freqmoy=np.mean(freqliste)
            Dfreqmoynat=np.mean(Dfreqliste)
            Dfreqmoystat=np.std(Dfreqliste)
            Dfreqmoy=Dfreqmoynat+Dfreqmoystat

            
            
            log10freqmoy=np.mean(log10freqliste)
            Dlog10freqmoynat=np.mean(Dlog10freqliste)
            Dlog10freqmoystat=np.std(Dlog10freqliste)
            Dlog10freqmoy=Dlog10freqmoynat+Dlog10freqmoystat
            
            qmoy=np.mean(qliste)   
            Dqmoynat=np.mean(Dqliste)
            Dqmoystat=np.std(Dqliste)
            Dqmoy=Dqmoynat+Dqmoystat
            
            Reqmoy=np.mean(Reqliste)   
            DReqmoynat=np.mean(DReqliste)
            DReqmoystat=np.std(DReqliste)
            DReqmoy=DReqmoynat+DReqmoystat
            
            Imqmoy=np.mean(Imqliste)   
            DImqmoynat=np.mean(DImqliste)
            DImqmoystat=np.std(DImqliste)
            DImqmoy=DImqmoynat+DImqmoystat
            
            ReZmoy=np.mean(ReZliste)   
            DReZmoynat=np.mean(DReZliste)
            DReZmoystat=np.std(DReZliste)
            DReZmoy=DReZmoynat+DReZmoystat
            
            ImZmoy=np.mean(ImZliste)   
            DImZmoynat=np.mean(DImZliste)
            DImZmoystat=np.std(DImZliste)
            DImZmoy=DImZmoynat+DImZmoystat
            
            argZmoy=np.mean(argZliste)   
            DargZmoynat=np.mean(DargZliste)
            DargZmoystat=np.std(DargZliste)
            DargZmoy=DargZmoynat+DargZmoystat
            
            modZmoy=np.mean(modZliste)   
            DmodZmoynat=np.mean(DmodZliste)
            DmodZmoystat=np.std(DmodZliste)
            DmodZmoy=DmodZmoynat+DmodZmoystat
            
            log10modZmoy=np.mean(log10modZliste)   
            Dlog10modZmoynat=np.mean(Dlog10modZliste)
            Dlog10modZmoystat=np.std(Dlog10modZliste)
            Dlog10modZmoy=Dlog10modZmoynat+Dlog10modZmoystat
            
            epsxmoy=np.mean(epsxliste)   
            Depsxmoynat=np.mean(Depsxliste)
            Depsxmoystat=np.std(Depsxliste)
            Depsxmoy=Depsxmoynat+Depsxmoystat
            
            epsymoy=np.mean(epsyliste)   
            Depsymoynat=np.mean(Depsyliste)
            Depsymoystat=np.std(Depsyliste)
            Depsymoy=Depsymoynat+Depsymoystat
            
            log10epsxmoy=np.mean(log10epsxliste)   
            Dlog10epsxmoynat=np.mean(Dlog10epsxliste)
            Dlog10epsxmoystat=np.std(Dlog10epsxliste)
            Dlog10epsxmoy=Dlog10epsxmoynat+Dlog10epsxmoystat
            
            log10epsymoy=np.mean(log10epsyliste)   
            Dlog10epsymoynat=np.mean(Dlog10epsyliste)
            Dlog10epsymoystat=np.std(Dlog10epsyliste)
            Dlog10epsymoy=Dlog10epsymoynat+Dlog10epsymoystat
            
            log10angpertemoy=np.mean(log10angperteliste)   
            Dlog10angpertemoynat=np.mean(Dlog10angperteliste)
            Dlog10angpertemoystat=np.std(Dlog10angperteliste)
            Dlog10angpertemoy=Dlog10angpertemoynat+Dlog10angpertemoystat
            
            

            calculsmoy[k,:]=[freqmoy,Dfreqmoy,log10freqmoy,Dlog10freqmoy,qmoy,Dqmoy,Reqmoy,DReqmoy,Imqmoy,DImqmoy,ReZmoy,DReZmoy,ImZmoy,DImZmoy,argZmoy,DargZmoy,modZmoy,DmodZmoy,log10modZmoy,Dlog10modZmoy,epsxmoy,Depsxmoy,epsymoy,Depsymoy,log10epsxmoy,Dlog10epsxmoy,log10epsymoy,Dlog10epsymoy,log10angpertemoy,Dlog10angpertemoy]
        
        file=filenameliste[s][0:-2]
        path2=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\Calculs_moy\{}_calculs_moy.txt".format(file)
        np.savetxt(path2,calculsmoy)
        s=s+i    
        
def graphmoy():
    path=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation"
    pathcalc=os.path.join(path,'Calculs_moy')
    filenameliste=listdir(pathcalc)
    sli=5
    for i in filenameliste:
        filename=os.path.join(pathcalc,i)
        with open(filename) as file :
            l=[]
            liste=[line.strip().split('/n')[0] for line in file] 
            
            for j in range(len(liste)):
                l2=liste[j].split(' ')
                line=[]
                line=[float(a) for a in l2]
                l.append(line)
        l=np.array(l)
        l=l[0:-sli,:]
        indfreq,indDfreq,indlog10freq,indDlog10freq,indq,indDq,\
        indReq,indDReq,indImq,indDImq,indReZ,indDReZ,indImZ,indDImZ,indargZ,\
        indDargZ,indmodZ,indDmodZ,indlog10modZ,indDlog10modZ,indepsx,indDepsx,indepsy,indDepsy,\
        indlog10epsx,indDlog10epsx,indlog10epsy,indDlog10epsy,\
        indlog10angperte,indDlog10angperte=0,1,2,3,4,5,6,7,8,9,10\
        ,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29

        log10freq=l[:,indlog10freq]
        log10Dfreq=l[:,indDlog10freq]
        argZ=l[:,indargZ]
        DargZ=l[:,indDargZ]
        xlabel='log10freq'
        plt.xlabel(xlabel)
        ylabel='argZ'
        plt.ylabel(ylabel)
        cmassique=i.split('_')[0]
        accel=i.split('_')[1]
        if cmassique=='air':
            cmassique='none'
        if accel=='calculs':
            accel='none'
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}_et_accélération_de_{}'.format(cmassique, accel)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.scatter(log10freq,argZ,s=10)
        plt.errorbar(log10freq, argZ, xerr=log10Dfreq, yerr=DargZ,ls='none')
        plt.grid()
        filenamedest=os.path.join(path,'Graphs_moy')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        modZ=l[:,indmodZ]
        DmodZ=l[:,indDmodZ]
        plt.xlabel(xlabel)
        ylabel='modZ'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}_et_accélération_de_{}'.format(cmassique, accel)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.scatter(log10freq,modZ,s=10)
        plt.errorbar(log10freq, modZ, xerr=log10Dfreq, yerr=DmodZ,ls='none')
        plt.grid()
        filenamedest=os.path.join(path,'Graphs_moy')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        log10modZ=l[:,indlog10modZ]
        Dlog10modZ=l[:,indDlog10modZ]
        plt.xlabel(xlabel)
        ylabel='log10modZ'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}_et_accélération_de_{}'.format(cmassique, accel)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.scatter(log10freq,modZ,s=10)
        plt.errorbar(log10freq, log10modZ, xerr=log10Dfreq, yerr=Dlog10modZ,ls='none')
        plt.grid()
        filenamedest=os.path.join(path,'Graphs_moy')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        ReZ=l[:,indReZ]
        DReZ=l[:,indDReZ]
        plt.xlabel(xlabel)
        ylabel='ReZ'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}_et_accélération_de_{}'.format(cmassique, accel)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.scatter(log10freq,ReZ,s=10)
        plt.errorbar(log10freq, ReZ, xerr=log10Dfreq, yerr=DReZ,ls='none')
        plt.grid()
        filenamedest=os.path.join(path,'Graphs_moy')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        ImZ=l[:,indImZ]
        DImZ=l[:,indDImZ]
        plt.xlabel(xlabel)
        ylabel='ImZ'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}_et_accélération_de_{}'.format(cmassique, accel)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.scatter(log10freq,ImZ,s=10)
        plt.errorbar(log10freq, ImZ, xerr=log10Dfreq, yerr=DImZ,ls='none')
        plt.grid()
        filenamedest=os.path.join(path,'Graphs_moy')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        log10angperte=l[:,indlog10angperte]
        Dlog10angperte=l[:,indDlog10angperte]
        plt.xlabel(xlabel)
        ylabel='log10angperte'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}_et_accélération_de_{}'.format(cmassique, accel)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.scatter(log10freq,log10angperte,s=10)
        plt.errorbar(log10freq, log10angperte, xerr=log10Dfreq, yerr=Dlog10angperte,ls='none')
        plt.grid()
        filenamedest=os.path.join(path,'Graphs_moy')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        log10epsx=l[:,indlog10epsx]
        Dlog10epsx=l[:,indDlog10epsx]
        plt.xlabel(xlabel)
        ylabel='log10epsx'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}_et_accélération_de_{}'.format(cmassique, accel)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.scatter(log10freq,log10epsx,s=10)
        plt.errorbar(log10freq, log10epsx, xerr=log10Dfreq, yerr=Dlog10epsx,ls='none')
        plt.grid()
        filenamedest=os.path.join(path,'Graphs_moy')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        log10epsy=l[:,indlog10epsy]
        Dlog10epsy=l[:,indDlog10epsy]
        plt.xlabel(xlabel)
        ylabel='log10epsy'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}_et_accélération_de_{}'.format(cmassique, accel)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.scatter(log10freq,log10epsy,s=10)
        plt.errorbar(log10freq, log10epsy, xerr=log10Dfreq, yerr=Dlog10epsy,ls='none')
        plt.grid()
        filenamedest=os.path.join(path,'Graphs_moy')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        epsx=l[:,indepsx]
        Depsx=l[:,indDepsx]
        epsy=l[:,indepsy]
        Depsy=l[:,indDepsy]
        xlabel='epsilonx'
        plt.xlabel(xlabel)
        ylabel='epsilony'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}_et_accélération_de_{}'.format(cmassique, accel)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.scatter(epsx,epsy,s=10)
        plt.errorbar(epsx, epsy, xerr=Depsx, yerr=Depsy,ls='none')
        plt.grid()
        filenamedest=os.path.join(path,'Graphs_moy')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        n1=7
        n2=0
        n3=len(line)-n2
        epsx=l[:,indepsx]
        epsxs=epsx[n1:n3]
        Depsx=l[:,indDepsx]
        Depsxs=Depsx[n1:n3]
        epsy=l[:,indepsy]
        epsys=epsy[n1:n3]
        Depsy=l[:,indDepsy]
        Depsys=Depsy[n1:n3]
        xlabel='epsilonx'
        plt.xlabel(xlabel)
        ylabel='epsilony'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}_pour_r={}_et_{}'.format(ylabel, xlabel,cmassique,accel)
        subtitle='_sans_les_{}_premières_et_{}_dernières_valeures'.format(n1,n2)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.scatter(epsxs,epsys,s=10)
        plt.errorbar(epsxs, epsys, xerr=Depsxs, yerr=Depsys,ls='none')
        plt.grid()
        filenamedest=os.path.join(path,'Graphs_moy')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()

def graph(filename):
    sli=5 #affiches rsultats jusqu'à 100 000Hz
        
    path=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}_calculs.txt".format(filename,filename)


    with open(path) as file :
        l=[]
        liste=[line.strip().split('/n')[0] for line in file] 
        
        for j in range(len(liste)):
            l2=liste[j].split(' ')
            line=[]
            line=[float(a) for a in l2]
            l.append(line)
    array=np.array(l)
    array=array[0:-sli,:]
    
    indfreq,indDfreq,indlog10freq,indDlog10freq,indq,indDq,\
    indReq,indDReq,indImq,indDImq,indReZ,indDReZ,indImZ,indDImZ,indargZ,\
    indDargZ,indmodZ,indDmodZ,indlog10modZ,indDlog10modZ,indepsx,indDepsx,indepsy,indDepsy,\
    indlog10epsx,indDlog10epsx,indlog10epsy,indDlog10epsy,\
    indlog10angperte,indDlog10angperte=0,1,2,3,4,5,6,7,8,9,10\
    ,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29

    
    log10freq=array[:,indlog10freq]
    log10Dfreq=array[:,indDlog10freq]
    argZ=array[:,indargZ]
    DargZ=array[:,indDargZ]
    xlabel='log10freq'
    plt.xlabel(xlabel)
    ylabel='argZ'
    plt.ylabel(ylabel)
    title='{}_en fonction_de_{}'.format(ylabel, xlabel)
    plt.title(title)
    plt.scatter(log10freq,argZ,s=10)
    plt.errorbar(log10freq, argZ, xerr=log10Dfreq, yerr=DargZ,ls='none')
    plt.grid()
    path2=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}_".format(filename,filename)
    plt.savefig(path2+title+'.png')
    plt.show()
    plt.close()
    
    modZ=array[:,indmodZ]
    DmodZ=array[:,indDmodZ]
    plt.xlabel(xlabel)
    ylabel='modZ'
    plt.ylabel(ylabel)
    title='{}_en fonction_de_{}'.format(ylabel, xlabel)
    plt.title(title)
    plt.scatter(log10freq,modZ,s=10)
    plt.errorbar(log10freq, modZ, xerr=log10Dfreq, yerr=DmodZ,ls='none')
    plt.grid()
    path2=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}_".format(filename,filename)
    plt.savefig(path2+title+'.png')
    plt.show()
    plt.close()
    
    log10angperte=array[:,indlog10angperte]
    Dlog10angperte=array[:,indDlog10angperte]
    plt.xlabel(xlabel)
    ylabel='log10angperte'
    plt.ylabel(ylabel)
    title='{}_en fonction_de_{}'.format(ylabel, xlabel)
    plt.title(title)
    plt.scatter(log10freq,log10angperte,s=10)
    plt.errorbar(log10freq, log10angperte, xerr=log10Dfreq, yerr=Dlog10angperte,ls='none')
    plt.grid()
    path2=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}_".format(filename,filename)
    plt.savefig(path2+title+'.png')
    plt.show()
    plt.close()

    log10epsx=array[:,indlog10epsx]
    Dlog10epsx=array[:,indDlog10epsx]
    plt.xlabel(xlabel)
    ylabel='log10epsx'
    plt.ylabel(ylabel)
    title='{}_en fonction_de_{}'.format(ylabel, xlabel)
    plt.title(title)
    plt.scatter(log10freq,log10epsx,s=10)
    plt.errorbar(log10freq, log10epsx, xerr=log10Dfreq, yerr=Dlog10epsx,ls='none')
    plt.grid()
    path2=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}_".format(filename,filename)
    plt.savefig(path2+title+'.png')
    plt.show()
    plt.close()
    
    log10epsy=array[:,indlog10epsy]
    Dlog10epsy=array[:,indDlog10epsy]
    plt.xlabel(xlabel)
    ylabel='log10epsy'
    plt.ylabel(ylabel)
    title='{}_en fonction_de_{}'.format(ylabel, xlabel)
    plt.title(title)
    plt.scatter(log10freq,log10epsy,s=10)
    plt.errorbar(log10freq, log10epsy, xerr=log10Dfreq, yerr=Dlog10epsy,ls='none')
    plt.grid()
    path2=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}_".format(filename,filename)
    plt.savefig(path2+title+'.png')
    plt.show()
    plt.close()
    
    epsx=array[:,indepsx]
    Depsx=array[:,indDepsx]
    epsy=array[:,indepsy]
    Depsy=array[:,indDepsy]
    xlabel='epsilonx'
    plt.xlabel(xlabel)
    ylabel='epsilony'
    plt.ylabel(ylabel)
    title='{}_en fonction_de_{}'.format(ylabel, xlabel)
    plt.title(title)
    plt.scatter(epsx,epsy,s=10)
    plt.errorbar(epsx, epsy, xerr=Depsx, yerr=Depsy,ls='none')
    plt.grid()
    path2=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}_".format(filename,filename)
    plt.savefig(path2+title+'.png')
    plt.show()
    plt.close()
    
    n1=7
    n2=0
    n3=len(line)-n2
    epsx=array[:,indepsx]
    epsxs=epsx[n1:n3]
    Depsx=array[:,indDepsx]
    Depsxs=Depsx[n1:n3]
    epsy=array[:,indepsy]
    epsys=epsy[n1:n3]
    Depsy=array[:,indDepsy]
    Depsys=Depsy[n1:n3]
    xlabel='epsilonx'
    plt.xlabel(xlabel)
    ylabel='epsilony'
    plt.ylabel(ylabel)
    title='{}_en fonction_de_{}'.format(ylabel, xlabel)
    subtitle='_sans_les_{}_premières_et_{}_dernières_valeures'.format(n1,n2)
    plt.suptitle(title, fontsize=12)
    plt.title(subtitle, fontsize=12)
    plt.scatter(epsxs,epsys,s=10)
    plt.errorbar(epsxs, epsys, xerr=Depsxs, yerr=Depsys,ls='none')
    plt.grid()
    path2=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}_".format(filename,filename)
    plt.savefig(path2+title+subtitle+'.png')
    plt.show()
    plt.close()


# filenameliste=[]
# G=[0,0.25,0.5,0.75,1,1.5,3,2.5,5,10]
# pourcentage=[0.125,0.25,0.5,1]
# for i in pourcentage:
#     for j in G:
#         for k in range(1,7):
#             filename='{}%_{}g_{}'.format(i,j,k)
#             path=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation\{}_dir\{}.txt".format(filename,filename)
#             if exists(path)==True:
#                 filenameliste.append(filename)
# for i in range (1,5):
#     filenameliste.append('air_{}'.format(i))

# for i in filenameliste:
#     calculs(i)

#calculmoy()
#graphmoy()