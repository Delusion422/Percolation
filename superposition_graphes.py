# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:58:42 2022

@author: mathi
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from os import listdir
from os.path import exists

def superpositiongraphe():
    G=[0,0.25,0.5,0.75,1,1.5,3,2.5,5,10]
    pourcentage=[0.125,0.25,0.5,1]
    path=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation"
    pathcalc=os.path.join(path,'Calculs_moy')
    for i in pourcentage:
        if i==1:
            G=[0,2.5,5]
        else:
            G=[0,3,5,10]
        serieg=[]
        datag=[]
        for j in G:
            filename='{}%_{}g_calculs_moy.txt'.format(i,j)
            file=os.path.join(pathcalc,filename)
            if exists(file)==True:
                serieg.append(filename)
        for k in serieg:
            
            with open(os.path.join(pathcalc,k)) as file :
                sli=5
                l=[]
                liste=[line.strip().split('/n')[0] for line in file]
                for m in range(len(liste)-sli):
                    
                    l2=liste[m].split(' ')
                    line=[float(n) for n in l2]
                    l.append(line)
            datag.append(l)
        datag=np.array(datag)

        
        indfreq,indDfreq,indlog10freq,indDlog10freq,indq,indDq,\
        indReq,indDReq,indImq,indDImq,indReZ,indDReZ,indImZ,indDImZ,indargZ,\
        indDargZ,indmodZ,indDmodZ,indlog10modZ,indDlog10modZ,indepsx,indDepsx,indepsy,indDepsy,\
        indlog10epsx,indDlog10epsx,indlog10epsy,indDlog10epsy,\
        indlog10angperte,indDlog10angperte=0,1,2,3,4,5,6,7,8,9,10\
        ,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
        
        log10freqliste=datag[:,:,indlog10freq]
        Dlog10freqliste=datag[:,:,indDlog10freq]
        
        argZliste=datag[:,:,indargZ]
        DargZliste=datag[:,:,indDargZ]
        
        modZliste=datag[:,:,indmodZ]
        DmodZliste=datag[:,:,indDmodZ]
        
        log10modZliste=datag[:,:,indlog10modZ]
        Dlog10modZliste=datag[:,:,indDlog10modZ]
        
        ReZliste=datag[:,:,indReZ]
        DReZliste=datag[:,:,indDReZ]
        
        ImZliste=datag[:,:,indImZ]
        DImZliste=datag[:,:,indDImZ]
        
        log10angperteliste=datag[:,:,indlog10angperte]
        Dlog10angperteliste=datag[:,:,indDlog10angperte]
        
        epsxliste=datag[:,:,indepsx]
        Depsxliste=datag[:,:,indDepsx]
        
        epsyliste=datag[:,:,indepsy]
        Depsyliste=datag[:,:,indDepsy]
 
        
        
        f1=1
        f2=16
        
        for a in range(len(log10freqliste)):
            plt.scatter(log10freqliste[a][f1:f2],argZliste[a][f1:f2],s=10,label=serieg[a].split('_')[1])
            plt.errorbar(log10freqliste[a][f1:f2], argZliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=DargZliste[a][f1:f2],ls='none')
        
        
        plt.legend(loc="upper right")
        xlabel='log10freq'
        plt.xlabel(xlabel)
        ylabel='ArgZ'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}%'.format(i)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.grid()
        filenamedest=os.path.join(path,'Superposition_Graphes')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        f1=0
        f2=16
        
        if i!=1:
            if i==0.125:
                f2=9
            else:
                f2=13
       
            for a in range(len(log10freqliste)):
                g=serieg[a].split('_')[1]
                if g=='5g' or g=='10g':
                    f2=9
                    plt.scatter(log10freqliste[a][f1:f2],modZliste[a][f1:f2],s=10,label=g)
                    plt.errorbar(log10freqliste[a][f1:f2], modZliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=DmodZliste[a][f1:f2],ls='none')
                else:
                    plt.scatter(log10freqliste[a][f1:f2],modZliste[a][f1:f2],s=10,label=g)
                    plt.errorbar(log10freqliste[a][f1:f2], modZliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=DmodZliste[a][f1:f2],ls='none')
        else:
            for a in range(len(log10freqliste)):
                g=serieg[a].split('_')[1]
                plt.scatter(log10freqliste[a][f1:f2],modZliste[a][f1:f2],s=10,label=g)
                plt.errorbar(log10freqliste[a][f1:f2], modZliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=DmodZliste[a][f1:f2],ls='none')
            
            
        plt.legend(loc="upper right")
        xlabel='log10freq'
        plt.xlabel(xlabel)
        ylabel='ModZ'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}%'.format(i)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.grid()
        filenamedest=os.path.join(path,'Superposition_Graphes')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        f1=0
        f2=16
       
        for a in range(len(log10freqliste)):
            g=serieg[a].split('_')[1]
            if i==0.25 or i==0.5 :
                f2=13
                if g=='5g' or g=='10g':
                    f2=9
            elif i==0.125:
                f2=5
            else:
                f2=13

            plt.scatter(log10freqliste[a][f1:f2],log10modZliste[a][f1:f2],s=10,label=g)
            plt.errorbar(log10freqliste[a][f1:f2], log10modZliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=Dlog10modZliste[a][f1:f2],ls='none')
           
        
        
        plt.legend(loc="upper right")
        xlabel='log10freq'
        plt.xlabel(xlabel)
        ylabel='log10ModZ'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}%'.format(i)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.grid()
        filenamedest=os.path.join(path,'Superposition_Graphes')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        
        f1=0
        f2=16
        
        if i!=0.125 and i!=1:
            f2=12
        else:
            if i==0.125:
                f1=3
                f2=8
            if i==1:
                f2=13
        
        for a in range(len(log10freqliste)):
            g=serieg[a].split('_')[1]
            if (g=='5g' or g=='10g') and i==0.5:
                f2=10
            if (g=='5g' or g=='10g') and i==0.25:
                f2=9
            plt.scatter(log10freqliste[a][f1:f2],ReZliste[a][f1:f2],s=10,label=g)
            plt.errorbar(log10freqliste[a][f1:f2], ReZliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=DReZliste[a][f1:f2],ls='none')
            
        plt.legend(loc="upper right")
        xlabel='log10freq'
        plt.xlabel(xlabel)
        ylabel='ReZ'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}%'.format(i)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.grid()
        filenamedest=os.path.join(path,'Superposition_Graphes')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        f1=0
        f2=16

        for a in range(len(log10freqliste)):
            g=serieg[a].split('_')[1]
            if (g=='0g'or g=='3g') and i==0.25:
                f2=8
            else:
                if i!=1:
                    f2=10
                else:
                    f2=11
                    
                
            plt.scatter(log10freqliste[a][f1:f2],ImZliste[a][f1:f2],s=10,label=g)
            plt.errorbar(log10freqliste[a][f1:f2], ImZliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=DImZliste[a][f1:f2],ls='none')
            
        plt.legend(loc="upper right")
        xlabel='log10freq'
        plt.xlabel(xlabel)
        ylabel='ImZ'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}%'.format(i)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.grid()
        filenamedest=os.path.join(path,'Superposition_Graphes')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        f1=3
        f2=16
        
        
        
        for a in range(len(log10freqliste)):
            g=serieg[a].split('_')[1]
            if i==1 and (g=='0g' or g=='2.5g'):
                f1=8
                plt.scatter(log10freqliste[a][f1:f2],log10angperteliste[a][f1:f2],s=10,label=g)
                plt.errorbar(log10freqliste[a][f1:f2], log10angperteliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=Dlog10angperteliste[a][f1:f2],ls='none')
            elif i==0.125 and g=='0g':
                x=log10freqliste[a][:7]
                y=log10freqliste[a][8:]
                zlog10freqliste= np.concatenate((x,y),axis=None)
                x=Dlog10freqliste[a][:7]
                y=Dlog10freqliste[a][8:]
                zDlog10freqliste= np.concatenate((x,y),axis=None)
                x=log10angperteliste[a][:7]
                y=log10angperteliste[a][8:]
                zlog10angperteliste= np.concatenate((x,y),axis=None)
                x=Dlog10angperteliste[a][:7]
                y=Dlog10angperteliste[a][8:]
                zDlog10angperteliste= np.concatenate((x,y),axis=None)
                plt.scatter(zlog10freqliste,zlog10angperteliste,s=10,label=g)
                plt.errorbar(zlog10freqliste, zlog10angperteliste, xerr=zDlog10freqliste, yerr=zDlog10angperteliste,ls='none')
            elif i==0.25 and g=='10g':
                f1=4
                plt.scatter(log10freqliste[a][f1:f2],log10angperteliste[a][f1:f2],s=10,label=g)
                plt.errorbar(log10freqliste[a][f1:f2], log10angperteliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=Dlog10angperteliste[a][f1:f2],ls='none')
            elif i==0.5 and (g=='0g' or g=='10g'):
                f1=6
                plt.scatter(log10freqliste[a][f1:f2],log10angperteliste[a][f1:f2],s=10,label=g)
                plt.errorbar(log10freqliste[a][f1:f2], log10angperteliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=Dlog10angperteliste[a][f1:f2],ls='none')
               
            else:
                plt.scatter(log10freqliste[a][f1:f2],log10angperteliste[a][f1:f2],s=10,label=g)
                plt.errorbar(log10freqliste[a][f1:f2], log10angperteliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=Dlog10angperteliste[a][f1:f2],ls='none')
                
        plt.legend(loc="upper right")
        xlabel='log10freq'
        plt.xlabel(xlabel)
        ylabel='log10angperte'
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}%'.format(i)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.grid()
        filenamedest=os.path.join(path,'Superposition_Graphes')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
        f1=9
        f2=15
        
        for a in range(len(log10freqliste)):
            if i==0.125:
                f1=2
            g=serieg[a].split('_')[1]
            plt.scatter(epsxliste[a][f1:f2],epsyliste[a][f1:f2],s=10,label=g)
            plt.errorbar(epsxliste[a][f1:f2], epsyliste[a][f1:f2], xerr=Depsxliste[a][f1:f2], yerr=Depsyliste[a][f1:f2],ls='none')
            
        plt.legend(loc="upper right")
        xlabel="epsilon'"
        plt.xlabel(xlabel)
        ylabel="epsilon''"
        plt.ylabel(ylabel)
        title='{}_en fonction_de_{}'.format(ylabel, xlabel)
        subtitle='pour_r={}%'.format(i)
        plt.suptitle(title, fontsize=12)
        plt.title(subtitle, fontsize=12)
        plt.grid()
        filenamedest=os.path.join(path,'Superposition_Graphes')
        filenamef=os.path.join(filenamedest,title+subtitle+'.png')
        plt.savefig(filenamef)
        plt.close()
        
def superpositiongraphe2():
    pourcentage=[0.125,0.25,0.5,1]
    path=r"C:\Users\mathi\OneDrive\Documents\Cours\M1\S2\Physique_experimentale_2_Projet\Donnees\Automatisation"
    pathcalc=os.path.join(path,'Calculs_moy')
    seriec=[]
    datac=[]
    for i in pourcentage:
        filename='{}%_0g_calculs_moy.txt'.format(i)
        seriec.append(filename)
    seriec.append('air_calculs_moy.txt')
    for j in seriec:
        with open(os.path.join(pathcalc,j)) as file :
            sli=5
            l=[]
            liste=[line.strip().split('/n')[0] for line in file]
            for m in range(len(liste)-sli):  
                l2=liste[m].split(' ')
                line=[float(n) for n in l2] 
                l.append(line)
            
        datac.append(l)
    datac=np.array(datac)
   
    indfreq,indDfreq,indlog10freq,indDlog10freq,indq,indDq,\
    indReq,indDReq,indImq,indDImq,indReZ,indDReZ,indImZ,indDImZ,indargZ,\
    indDargZ,indmodZ,indDmodZ,indlog10modZ,indDlog10modZ,indepsx,indDepsx,indepsy,indDepsy,\
    indlog10epsx,indDlog10epsx,indlog10epsy,indDlog10epsy,\
    indlog10angperte,indDlog10angperte=0,1,2,3,4,5,6,7,8,9,10\
    ,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29
    
    log10freqliste=datac[:,:,indlog10freq]
    Dlog10freqliste=datac[:,:,indDlog10freq]
    
    argZliste=datac[:,:,indargZ]
    DargZliste=datac[:,:,indDargZ]
    
    modZliste=datac[:,:,indmodZ]
    DmodZliste=datac[:,:,indDmodZ]
    
    log10modZliste=datac[:,:,indlog10modZ]
    Dlog10modZliste=datac[:,:,indDlog10modZ]
    
    ReZliste=datac[:,:,indReZ]
    DReZliste=datac[:,:,indDReZ]
    
    ImZliste=datac[:,:,indImZ]
    DImZliste=datac[:,:,indDImZ]
    
    log10angperteliste=datac[:,:,indlog10angperte]
    Dlog10angperteliste=datac[:,:,indDlog10angperte]
    
    epsxliste=datac[:,:,indepsx]
    Depsxliste=datac[:,:,indDepsx]
    
    epsyliste=datac[:,:,indepsy]
    Depsyliste=datac[:,:,indDepsy]

    
    
    f1=0
    f2=16
    
    for a in range(len(log10freqliste)):
        c=seriec[a].split('_')[0]
        plt.scatter(log10freqliste[a][f1:f2],argZliste[a][f1:f2],s=10,label=c)
        plt.errorbar(log10freqliste[a][f1:f2], argZliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=DargZliste[a][f1:f2],ls='none')
    
    
    plt.legend(loc="upper right")
    xlabel='log10freq'
    plt.xlabel(xlabel)
    ylabel='ArgZ'
    plt.ylabel(ylabel)
    title='{}_en fonction_de_{}'.format(ylabel, xlabel)
    subtitle='pour_0g'
    plt.suptitle(title, fontsize=12)
    plt.title(subtitle, fontsize=12)
    plt.grid()
    filenamedest=os.path.join(path,'Superposition_Graphes2')
    filenamef=os.path.join(filenamedest,title+subtitle+'.png')
    plt.savefig(filenamef)
    plt.close()
    
    f1=0
    f2=13
    
    for a in range(len(log10freqliste)):
        c=seriec[a].split('_')[0]
        plt.scatter(log10freqliste[a][f1:f2],log10modZliste[a][f1:f2],s=10,label=c)
        plt.errorbar(log10freqliste[a][f1:f2], log10modZliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=Dlog10modZliste[a][f1:f2],ls='none')
           
               
    plt.legend(loc="upper left")
    xlabel='log10freq'
    plt.xlabel(xlabel)
    ylabel='log10ModZ'
    plt.ylabel(ylabel)
    title='{}_en fonction_de_{}'.format(ylabel, xlabel)
    subtitle='pour_0g'
    plt.suptitle(title, fontsize=12)
    plt.title(subtitle, fontsize=12)
    plt.grid()
    filenamedest=os.path.join(path,'Superposition_Graphes2')
    filenamef=os.path.join(filenamedest,title+subtitle+'.png')
    plt.savefig(filenamef)
    plt.close()
    
    f1=3
    f2=12
    
    for a in range(len(log10freqliste)):
        c=seriec[a].split('_')[0]
        if c=='1%':
            f1=6
            plt.scatter(log10freqliste[a][f1:f2],log10angperteliste[a][f1:f2],s=10,label=c)
            plt.errorbar(log10freqliste[a][f1:f2], log10angperteliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=Dlog10angperteliste[a][f1:f2],ls='none')
        elif c=='0.5%':
            x=log10freqliste[a][f1:3]
            y=log10freqliste[a][4:f2]
            zlog10freqliste= np.concatenate((x,y),axis=None)
            x=Dlog10freqliste[a][f1:3]
            y=Dlog10freqliste[a][4:f2]
            zDlog10freqliste= np.concatenate((x,y),axis=None)
            x=log10angperteliste[a][f1:3]
            y=log10angperteliste[a][4:f2]
            zlog10angperteliste= np.concatenate((x,y),axis=None)
            x=Dlog10angperteliste[a][f1:3]
            y=Dlog10angperteliste[a][4:f2]
            zDlog10angperteliste= np.concatenate((x,y),axis=None)
            plt.scatter(zlog10freqliste,zlog10angperteliste,s=10,label=c)
            plt.errorbar(zlog10freqliste, zlog10angperteliste, xerr=zDlog10freqliste, yerr=zDlog10angperteliste,ls='none')
        elif c=='0.25%':
            x=log10freqliste[a][:2]
            y=log10freqliste[a][3:f2]
            zlog10freqliste= np.concatenate((x,y),axis=None)
            x=Dlog10freqliste[a][:2]
            y=Dlog10freqliste[a][3:f2]
            zDlog10freqliste= np.concatenate((x,y),axis=None)
            x=log10angperteliste[a][:2]
            y=log10angperteliste[a][3:f2]
            zlog10angperteliste= np.concatenate((x,y),axis=None)
            x=Dlog10angperteliste[a][:2]
            y=Dlog10angperteliste[a][3:f2]
            zDlog10angperteliste= np.concatenate((x,y),axis=None)
            plt.scatter(zlog10freqliste,zlog10angperteliste,s=10,label=c)
            plt.errorbar(zlog10freqliste, zlog10angperteliste, xerr=zDlog10freqliste, yerr=zDlog10angperteliste,ls='none')
        elif c=='0.125%':   
            f1=7
            plt.scatter(log10freqliste[a][f1:f2],log10angperteliste[a][f1:f2],s=10,label=c)
            plt.errorbar(log10freqliste[a][f1:f2], log10angperteliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=Dlog10angperteliste[a][f1:f2],ls='none')
        else:
            plt.scatter(log10freqliste[a][f1:f2],log10angperteliste[a][f1:f2],s=10,label=c)
            plt.errorbar(log10freqliste[a][f1:f2], log10angperteliste[a][f1:f2], xerr=Dlog10freqliste[a][f1:f2], yerr=Dlog10angperteliste[a][f1:f2],ls='none')
        
               
    plt.legend(loc="upper right")
    xlabel='log10freq'
    plt.xlabel(xlabel)
    ylabel='log10angperte'
    plt.ylabel(ylabel)
    title='{}_en fonction_de_{}'.format(ylabel, xlabel)
    subtitle='pour_0g'
    plt.suptitle(title, fontsize=12)
    plt.title(subtitle, fontsize=12)
    plt.grid()
    filenamedest=os.path.join(path,'Superposition_Graphes2')
    filenamef=os.path.join(filenamedest,title+subtitle+'.png')
    plt.savefig(filenamef)
    plt.close()

    f1=9
    f2=16
    
    for a in range(len(log10freqliste)):
        c=seriec[a].split('_')[0]
        plt.scatter(epsxliste[a][f1:f2],epsyliste[a][f1:f2],s=10,label=c)
        plt.errorbar(epsxliste[a][f1:f2], epsyliste[a][f1:f2], xerr=Depsxliste[a][f1:f2], yerr=Depsyliste[a][f1:f2],ls='none')
           
               
    plt.legend(loc="upper right")
    xlabel="epsilon'"
    plt.xlabel(xlabel)
    ylabel="epsilon''"
    plt.ylabel(ylabel)
    title='{}_en fonction_de_{}'.format(ylabel, xlabel)
    subtitle='pour_0g'
    plt.suptitle(title, fontsize=12)
    plt.title(subtitle, fontsize=12)
    plt.grid()
    filenamedest=os.path.join(path,'Superposition_Graphes2')
    filenamef=os.path.join(filenamedest,title+subtitle+'.png')
    plt.savefig(filenamef)
    plt.close()

    
superpositiongraphe2()



