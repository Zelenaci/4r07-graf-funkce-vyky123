#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:25:54 2019

@author: vyk35227
"""

import tkinter as tk
import pylab as pl
from tkinter import messagebox, filedialog


main = tk.Tk()
main.title("Grafy funkcí")


def fceGraf():
    try:
        od = float(fceMin.get())
        do = float(fceMax.get())
        x = pl.linspace(od, do, 500)
        if fceVar.get() == 0:
            y = pl.sin(x)
        elif fceVar.get() == 1:
            y = pl.log10(x)
        elif fceVar.get() == 2:
            y = pl.exp(x)
        
        pl.figure()
        pl.plot(x, y)
        pl.xlabel(osaxVar.get())
        pl.ylabel(osayVar.get())
        pl.show()
    except:
        messagebox.showerror(title="Chybné meze", message="Zadejte meze osy\n jako reálná čísla!")

def vyberSoubor():
    cesta = filedialog.askopenfilename(title="Vyberte soubor")
    if cesta != "":
        sbrVar.set(cesta)

def sbrGraf():
    try:
        cesta = sbrVar.get()
        f = open(cesta, "r")
        x = []
        y = []
        while True:
            radek=f.readline()
            if radek== "":
                break
            cisla = radek.split()
            x.append(float(cisla[0]))
            y.append(float(cisla[1]))
        f.close()
        pl.figure()
        pl.plot(x, y)
        pl.xlabel(osaxVar.get())
        pl.ylabel(osayVar.get())
        pl.show()
    except:
        messagebox.showerror(title="Chybný formát souboru", message="Graf se nepodařilo vytvořit,\nzkontrolujte formát souboru.")

def smazPole():
    fceMinEntry.delete(0, tk.END)
    fceMaxEntry.delete(0, tk.END)

def smazPoleSbr():
    sbrEntry.delete(0, tk.END)    


def klik(event):
    q1 = fceMin.get()
    q2 = fceMax.get()
    if q1 == "Od" or q2 == "Do":
        smazPole()

def klikSbr(event):
    q = sbrVar.get()
    if q == "/ceska/k/souboru":
        smazPoleSbr()
        


### funkce ###
fceVar = tk.IntVar()
fceMin = tk.StringVar()
fceMax = tk.StringVar()
fceFrame = tk.LabelFrame(main, text="Graf matematické funkce")
fceFrame.grid()


### výběr funkcí ###
tk.Radiobutton(fceFrame, text="sin", variable=fceVar, value=0).grid(sticky=tk.W)
tk.Radiobutton(fceFrame, text="log", variable=fceVar, value=1).grid(sticky=tk.W)
tk.Radiobutton(fceFrame, text="exp", variable=fceVar, value=2).grid(sticky=tk.W)


###od - do, vytvoř graf###
fceMin.set("Od")
fceMax.set("Do")
fceMinEntry = tk.Entry(fceFrame, textvariable=fceMin, width=6)
fceMinEntry.grid(column=2, row=0, sticky=tk.E)
fceMaxEntry = tk.Entry(fceFrame, textvariable=fceMax, width=6)
fceMaxEntry.grid(column=2, row=1, sticky=tk.E)
tk.Button(main, text="Vytvoř graf", height=5, command=fceGraf).grid(column=3, row=0)

fceMinEntry.bind("<Button-1>", klik)
fceMaxEntry.bind("<Button-1>", klik)


###graf ze souboru###
sbrFrame = tk.LabelFrame(main, text="Graf funkce ze souboru")
sbrFrame.grid()
sbrVar = tk.StringVar()
sbrVar.set("/ceska/k/souboru")
sbrEntry = tk.Entry(sbrFrame, textvariable=sbrVar)
sbrEntry.grid()
tk.Button(sbrFrame, text="Vyber soubor", width=8, command=vyberSoubor).grid(column=0, sticky=tk.E)
tk.Button(main, text="Vytvoř graf", height=5, command=sbrGraf).grid(column=3, row=1)
sbrEntry.bind("<Button-1>", klikSbr)

###popisky os###
osyFrame=tk.LabelFrame(main, text="Popisky os")
osyFrame.grid()
tk.Label(osyFrame, text="osa x").grid()
osaxVar = tk.StringVar()
osayVar = tk.StringVar()
tk.Entry(osyFrame, textvariable=osaxVar, width=15).grid(column=1, row=0)
tk.Label(osyFrame, text="osa y").grid(sticky=tk.W)
tk.Entry(osyFrame, textvariable=osayVar, width=15).grid(column=1, row=1)


main.mainloop()
