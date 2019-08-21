import tkinter as tk
from tkinter import *
import math

mainWindow = tk.Tk()
mainWindow.configure(background='White')
mainWindow.title("Considerations in Fin Material Selection")
mainWindow.geometry("1790x790")
tkvar1 = StringVar(mainWindow)
tkvar2 = StringVar(mainWindow)
tkvar3 = StringVar(mainWindow)

label1 = tk.Label(mainWindow, text="Considerations in Fin Material Selection", fg="Red", font="algerian 18 bold", bg="white")
label1.pack()

label2 = tk.Label(mainWindow, text="We have here, a hot surface at Tb= 150 °C in a colder ambient temperature of 20 °C. We wish to cool down this hot surface\n by attaching an array of fins of some mateirial", font="8", bg="white")
label2.place(x=20,y=30)

label3 = tk.Label(mainWindow, text="For the purpose of comparison, let's experiment with long cylindrical fins of diameter 4mm, and assume\n that heat transfer coefficient(h) on all surface is 35 W/m²K .", font="8", bg="white")
label3.place(x=20,y=80)

label4 = tk.Label(mainWindow, text="Select any three materials to compare the Temperature Variation:",fg="teal", font="8", bg="white")
label4.place(x=20,y=140)

label5a = tk.Label(mainWindow, text="Select material 1:", font="10", bg="white")
label5a.place(x=420,y=180)

label5b = tk.Label(mainWindow, text="Select material 2:", font="10", bg="white")
label5b.place(x=420,y=390)

label5c = tk.Label(mainWindow, text="Select material 3:", font="10", bg="white")
label5c.place(x=420,y=590)

choice1 = {'Stainless Steel(Type 304) (K=14.4 W/mK)','Bronze (K=26 W/mK)', 'Carbon Steel(1 Y.C.) (K=43 W/mK)',
            'Copper-Phosphur Bronze (K=50 W/mK)','Cast Iron (K=52 W/mK)', 'Chrome Steel(1 Y.C.) (K=61 W/m.K)',
            'Brass (K=111 W/mK)','Al alloy 204 (K=125 W/mK)', 'Al alloy 6066 (K=167 W/mK)',
           'Aluminium (K=237 W/mk)', 'Copper (K=386 W/mK)'}
tkvar1.set('Stainless Steel(Type 304) (K=14.4 W/mK)')
popupMenu1 = OptionMenu(mainWindow, tkvar1, *choice1)
popupMenu1.place(x=400, y=210)

choice2 = {'Stainless Steel(Type 304) (K=14.4 W/mK)','Bronze (K=26 W/mK)', 'Carbon Steel(1 Y.C.) (K=43 W/mK)',
            'Copper-Phosphur Bronze (K=50 W/mK)','Cast Iron (K=52 W/mK)', 'Chrome Steel(1 Y.C.) (K=61 W/m.K)',
            'Brass (K=111 W/mK)','Al alloy 204 (K=125 W/mK)', 'Al alloy 6066 (K=167 W/mK)',
           'Aluminium (K=237 W/mk)', 'Copper (K=386 W/mK)'}
tkvar2.set('Stainless Steel(Type 304) (K=14.4 W/mK)')
popupMenu2 = OptionMenu(mainWindow, tkvar2, *choice2)
popupMenu2.place(x=400, y=420)

choice3 = {'Stainless Steel(Type 304) (K=14.4 W/mK)','Bronze (K=26 W/mK)', 'Carbon Steel(1 Y.C.) (K=43 W/mK)',
            'Copper-Phosphur Bronze (K=50 W/mK)','Cast Iron (K=52 W/mK)', 'Chrome Steel(1 Y.C.) (K=61 W/m.K)',
            'Brass (K=111 W/mK)','Al alloy 204 (K=125 W/mK)', 'Al alloy 6066 (K=167 W/mK)',
           'Aluminium (K=237 W/mk)', 'Copper (K=386 W/mK)'}
tkvar3.set('Stainless Steel(Type 304) (K=14.4 W/mK)')
popupMenu3 = OptionMenu(mainWindow, tkvar3, *choice3)
popupMenu3.place(x=400, y=620)


C1 = tk.Canvas(mainWindow, width=35, height=480,bg="red")
C1.place(x=40,y=260)
coord1 = 20, 230
C1.create_text(coord1, text="\t\tTb=150°C", angle=90, fill="black", font="times 15 bold")

C2 = tk.Canvas(mainWindow, width=945, height=35,bg="#FFB6C1")
C2.place(x=76,y=290)

C3 = tk.Canvas(mainWindow, width=945, height=35,bg="#FFFF00")
C3.place(x=76,y=490)

C4 = tk.Canvas(mainWindow, width=945, height=35,bg="#00FF00")
C4.place(x=76,y=690)

coord2a = 23,20
C2.create_text(coord2a, text="x=0.5", fill="black", font="times 15 ")

coord2b = 77,20
C2.create_text(coord2b, text="1", fill="black", font="times 15 ")

coord2c = 162,20
C2.create_text(coord2c, text="2", fill="black", font="times 15 ")

coord2d = 247,20
C2.create_text(coord2d, text="3", fill="black", font="times 15 ")

coord2e = 332,20
C2.create_text(coord2e, text="4", fill="black", font="times 15 ")

coord2f = 417,20
C2.create_text(coord2f, text="5", fill="black", font="times 15 ")

coord2g = 502,20
C2.create_text(coord2g, text="8", fill="black", font="times 15 ")

coord2h = 587,20
C2.create_text(coord2h, text="10", fill="black", font="times 15 ")

coord2i = 672,20
C2.create_text(coord2i, text="12", fill="black", font="times 15 ")

coord2j = 757,20
C2.create_text(coord2j, text="15", fill="black", font="times 15 ")

coord2k = 842,20
C2.create_text(coord2k, text="18", fill="black", font="times 15 ")

coord2l = 912,20
C2.create_text(coord2l, text="20", fill="black", font="times 15 ")



coord3a = 23,20
C3.create_text(coord3a, text="x=0.5", fill="black", font="times 15 ")

coord3b = 77,20
C3.create_text(coord3b, text="1", fill="black", font="times 15 ")

coord3c = 162,20
C3.create_text(coord3c, text="2", fill="black", font="times 15 ")

coord3d = 247,20
C3.create_text(coord3d, text="3", fill="black", font="times 15 ")

coord3e = 332,20
C3.create_text(coord3e, text="4", fill="black", font="times 15 ")

coord3f = 417,20
C3.create_text(coord3f, text="5", fill="black", font="times 15 ")

coord3g = 502,20
C3.create_text(coord3g, text="8", fill="black", font="times 15 ")

coord3h = 587,20
C3.create_text(coord3h, text="10", fill="black", font="times 15 ")

coord3i = 672,20
C3.create_text(coord3i, text="12", fill="black", font="times 15 ")

coord3j = 757,20
C3.create_text(coord3j, text="15", fill="black", font="times 15 ")

coord3k = 842,20
C3.create_text(coord3k, text="18", fill="black", font="times 15 ")

coord3l = 912,20
C3.create_text(coord3l, text="20", fill="black", font="times 15 ")


coord4a = 23,20
C4.create_text(coord4a, text="x=0.5", fill="black", font="times 15 ")

coord4b = 77,20
C4.create_text(coord4b, text="1", fill="black", font="times 15 ")

coord4c = 162,20
C4.create_text(coord4c, text="2", fill="black", font="times 15 ")

coord4d = 247,20
C4.create_text(coord4d, text="3", fill="black", font="times 15 ")

coord4e = 332,20
C4.create_text(coord4e, text="4", fill="black", font="times 15 ")

coord4f = 417,20
C4.create_text(coord4f, text="5", fill="black", font="times 15 ")

coord4g = 502,20
C4.create_text(coord4g, text="8", fill="black", font="times 15 ")

coord4h = 587,20
C4.create_text(coord4h, text="10", fill="black", font="times 15 ")

coord4i = 672,20
C4.create_text(coord4i, text="12", fill="black", font="times 15 ")

coord4j = 757,20
C4.create_text(coord4j, text="15", fill="black", font="times 15 ")

coord4k = 842,20
C4.create_text(coord4k, text="18", fill="black", font="times 15 ")

coord4l = 912,20
C4.create_text(coord4l, text="20", fill="black", font="times 15 ")

def solve():
        # Fetching k1 value
    if tkvar1.get() == 'Stainless Steel(Type 304) (K=14.4 W/mK)':
        k1 = float(14.4)
    elif tkvar1.get() == 'Bronze (K=26 W/mK)':
        k1 = float(26)
    elif tkvar1.get() == 'Carbon Steel(1 Y.C.) (K=43 W/mK)':
        k1 = float(43)
    elif tkvar1.get() == 'Copper-Phosphur Bronze (K=50 W/mK)':
        k1 = float(50)
    elif tkvar1.get() == 'Cast Iron (K=52 W/mK)':
        k1 = float(52)
    elif tkvar1.get() == 'Chrome Steel(1 Y.C.) (K=61 W/m.K)':
        k1 = float(61)
    elif tkvar1.get() == 'Brass (K=111 W/mK)':
        k1 = float(111)
    elif tkvar1.get() == 'Al alloy 204 (K=125 W/mK)':
        k1 = float(125)
    elif tkvar1.get() == 'Al alloy 6066 (K=167 W/mK)':
        k1 = float(167)
    elif tkvar1.get() == 'Aluminium (K=237 W/mk)':
        k1 = float(237)
    elif tkvar1.get() == 'Copper (K=386 W/mK)':
        k1 = float(386)

    # Fetching k2 value
    if tkvar2.get() == 'Stainless Steel(Type 304) (K=14.4 W/mK)':
        k2 = float(14.4)
    elif tkvar2.get() == 'Bronze (K=26 W/mK)':
        k2 = float(26)
    elif tkvar2.get() == 'Carbon Steel(1 Y.C.) (K=43 W/mK)':
        k2 = float(43)
    elif tkvar2.get() == 'Copper-Phosphur Bronze (K=50 W/mK)':
        k2 = float(50)
    elif tkvar2.get() == 'Cast Iron (K=52 W/mK)':
        k2 = float(52)
    elif tkvar2.get() == 'Chrome Steel(1 Y.C.) (K=61 W/m.K)':
        k2 = float(61)
    elif tkvar2.get() == 'Brass (K=111 W/mK)':
        k2 = float(111)
    elif tkvar2.get() == 'Al alloy 204 (K=125 W/mK)':
        k2 = float(125)
    elif tkvar2.get() == 'Al alloy 6066 (K=167 W/mK)':
        k2 = float(167)
    elif tkvar2.get() == 'Aluminium (K=237 W/mk)':
        k2 = float(237)
    elif tkvar2.get() == 'Copper (K=386 W/mK)':
        k2 = float(386)

    # Fetching k3 value
    if tkvar3.get() == 'Stainless Steel(Type 304) (K=14.4 W/mK)':
        k3 = float(14.4)
    elif tkvar3.get() == 'Bronze (K=26 W/mK)':
        k3 = float(26)
    elif tkvar3.get() == 'Carbon Steel(1 Y.C.) (K=43 W/mK)':
        k3 = float(43)
    elif tkvar3.get() == 'Copper-Phosphur Bronze (K=50 W/mK)':
        k3 = float(50)
    elif tkvar3.get() == 'Cast Iron (K=52 W/mK)':
        k3 = float(52)
    elif tkvar3.get() == 'Chrome Steel(1 Y.C.) (K=61 W/m.K)':
        k3 = float(61)
    elif tkvar3.get() == 'Brass (K=111 W/mK)':
        k3 = float(111)
    elif tkvar3.get() == 'Al alloy 204 (K=125 W/mK)':
        k3 = float(125)
    elif tkvar3.get() == 'Al alloy 6066 (K=167 W/mK)':
        k3 = float(167)
    elif tkvar3.get() == 'Aluminium (K=237 W/mk)':
        k3 = float(237)
    elif tkvar3.get() == 'Copper (K=386 W/mK)':
        k3 = float(386)

    T2a1=(math.exp(-math.sqrt(35/k1)*0.5)*130)+20
    T2a = round(T2a1,2)
    entry2a=tk.Entry(mainWindow,width=5)
    entry2a.place(x=60,y=270)
    entry2a.insert(0,T2a)

    T2b1=(math.exp(-math.sqrt(35/k1)*1)*130)+20
    T2b = round(T2b1,2)
    entry2b=tk.Entry(mainWindow,width=5)
    entry2b.place(x=145,y=270)
    entry2b.insert(0,T2b)

    T2c1=(math.exp(-math.sqrt(35/k1)*2)*130)+20
    T2c = round(T2c1,2)
    entry2c=tk.Entry(mainWindow,width=5)
    entry2c.place(x=230,y=270)
    entry2c.insert(0,T2c)

    T2d1=(math.exp(-math.sqrt(35/k1)*3)*130)+20
    T2d = round(T2d1,2)
    entry2d=tk.Entry(mainWindow,width=5)
    entry2d.place(x=315,y=270)
    entry2d.insert(0,T2d)

    T2e1=(math.exp(-math.sqrt(35/k1)*4)*130)+20
    T2e = round(T2e1,2)
    entry2e=tk.Entry(mainWindow,width=5)
    entry2e.place(x=400,y=270)
    entry2e.insert(0,T2e)

    T2f1=(math.exp(-math.sqrt(35/k1)*5)*130)+20
    T2f = round(T2f1,2)
    entry2f=tk.Entry(mainWindow,width=5)
    entry2f.place(x=485,y=270)
    entry2f.insert(0,T2f)

    T2g1=(math.exp(-math.sqrt(35/k1)*8)*130)+20
    T2g = round(T2g1,2)
    entry2g=tk.Entry(mainWindow,width=5)
    entry2g.place(x=570,y=270)
    entry2g.insert(0,T2g)

    T2h1=(math.exp(-math.sqrt(35/k1)*10)*130)+20
    T2h = round(T2h1,2)
    entry2h=tk.Entry(mainWindow,width=5)
    entry2h.place(x=655,y=270)
    entry2h.insert(0,T2h)

    T2i1=(math.exp(-math.sqrt(35/k1)*12)*130)+20
    T2i = round(T2i1,2)
    entry2i=tk.Entry(mainWindow,width=5)
    entry2i.place(x=740,y=270)
    entry2i.insert(0,T2i)

    T2j1=(math.exp(-math.sqrt(35/k1)*15)*130)+20
    T2j = round(T2j1,2)
    entry2j=tk.Entry(mainWindow,width=5)
    entry2j.place(x=825,y=270)
    entry2j.insert(0,T2j)

    T2k1=(math.exp(-math.sqrt(35/k1)*18)*130)+20
    T2k = round(T2k1,2)
    entry2k=tk.Entry(mainWindow,width=5)
    entry2k.place(x=910,y=270)
    entry2k.insert(0,T2k)

    T2l1=(math.exp(-math.sqrt(35/k1)*20)*130)+20
    T2l = round(T2l1,2)
    entry2l=tk.Entry(mainWindow,width=5)
    entry2l.place(x=995,y=270)
    entry2l.insert(0,T2l)


    T3a1=(math.exp(-math.sqrt(35/k2)*0.5)*130)+20
    T3a = round(T3a1,2)
    entry3a=tk.Entry(mainWindow,width=5)
    entry3a.place(x=60,y=470)
    entry3a.insert(0,T3a)

    T3b1=(math.exp(-math.sqrt(35/k2)*1)*130)+20
    T3b = round(T3b1,2)
    entry3b=tk.Entry(mainWindow,width=5)
    entry3b.place(x=145,y=470)
    entry3b.insert(0,T3b)

    T3c1=(math.exp(-math.sqrt(35/k2)*2)*130)+20
    T3c = round(T3c1,2)
    entry3c=tk.Entry(mainWindow,width=5)
    entry3c.place(x=230,y=470)
    entry3c.insert(0,T3c)

    T3d1=(math.exp(-math.sqrt(35/k2)*3)*130)+20
    T3d = round(T3d1,2)
    entry3d=tk.Entry(mainWindow,width=5)
    entry3d.place(x=315,y=470)
    entry3d.insert(0,T3d)

    T3e1=(math.exp(-math.sqrt(35/k2)*4)*130)+20
    T3e = round(T3e1,2)
    entry3e=tk.Entry(mainWindow,width=5)
    entry3e.place(x=400,y=470)
    entry3e.insert(0,T3e)

    T3f1=(math.exp(-math.sqrt(35/k2)*5)*130)+20
    T3f = round(T3f1,2)
    entry3f=tk.Entry(mainWindow,width=5)
    entry3f.place(x=485,y=470)
    entry3f.insert(0,T3f)

    T3g1=(math.exp(-math.sqrt(35/k2)*8)*130)+20
    T3g = round(T3g1,2)
    entry3g=tk.Entry(mainWindow,width=5)
    entry3g.place(x=570,y=470)
    entry3g.insert(0,T3g)

    T3h1=(math.exp(-math.sqrt(35/k2)*10)*130)+20
    T3h = round(T3h1,2)
    entry3h=tk.Entry(mainWindow,width=5)
    entry3h.place(x=655,y=470)
    entry3h.insert(0,T3h)

    T3i1=(math.exp(-math.sqrt(35/k2)*12)*130)+20
    T3i = round(T3i1,2)
    entry3i=tk.Entry(mainWindow,width=5)
    entry3i.place(x=740,y=470)
    entry3i.insert(0,T3i)

    T3j1=(math.exp(-math.sqrt(35/k2)*15)*130)+20
    T3j = round(T3j1,2)
    entry3j=tk.Entry(mainWindow,width=5)
    entry3j.place(x=825,y=470)
    entry3j.insert(0,T3j)

    T3k1=(math.exp(-math.sqrt(35/k2)*18)*130)+20
    T3k = round(T3k1,2)
    entry3k=tk.Entry(mainWindow,width=5)
    entry3k.place(x=910,y=470)
    entry3k.insert(0,T3k)

    T3l1=(math.exp(-math.sqrt(35/k2)*20)*130)+20
    T3l = round(T3l1,2)
    entry3l=tk.Entry(mainWindow,width=5)
    entry3l.place(x=995,y=470)
    entry3l.insert(0,T3l)


    T4a1=(math.exp(-math.sqrt(35/k3)*0.5)*130)+20
    T4a = round(T4a1,2)
    entry4a=tk.Entry(mainWindow,width=5)
    entry4a.place(x=60,y=670)
    entry4a.insert(0,T4a)

    T4b1=(math.exp(-math.sqrt(35/k3)*1)*130)+20
    T4b = round(T4b1,2)
    entry4b=tk.Entry(mainWindow,width=5)
    entry4b.place(x=145,y=670)
    entry4b.insert(0,T4b)

    T4c1=(math.exp(-math.sqrt(35/k3)*2)*130)+20
    T4c = round(T4c1,2)
    entry4c=tk.Entry(mainWindow,width=5)
    entry4c.place(x=230,y=670)
    entry4c.insert(0,T4c)

    T4d1=(math.exp(-math.sqrt(35/k3)*3)*130)+20
    T4d = round(T4d1,2)
    entry4d=tk.Entry(mainWindow,width=5)
    entry4d.place(x=315,y=670)
    entry4d.insert(0,T4d)

    T4e1=(math.exp(-math.sqrt(35/k3)*4)*130)+20
    T4e = round(T4e1,2)
    entry4e=tk.Entry(mainWindow,width=5)
    entry4e.place(x=400,y=670)
    entry4e.insert(0,T4e)

    T4f1=(math.exp(-math.sqrt(35/k3)*5)*130)+20
    T4f = round(T4f1,2)
    entry4f=tk.Entry(mainWindow,width=5)
    entry4f.place(x=485,y=670)
    entry4f.insert(0,T4f)

    T4g1=(math.exp(-math.sqrt(35/k3)*8)*130)+20
    T4g = round(T4g1,2)
    entry4g=tk.Entry(mainWindow,width=5)
    entry4g.place(x=570,y=670)
    entry4g.insert(0,T4g)

    T4h1=(math.exp(-math.sqrt(35/k3)*10)*130)+20
    T4h = round(T4h1,2)
    entry4h=tk.Entry(mainWindow,width=5)
    entry4h.place(x=655,y=670)
    entry4h.insert(0,T4h)

    T4i1=(math.exp(-math.sqrt(35/k3)*12)*130)+20
    T4i = round(T4i1,2)
    entry4i=tk.Entry(mainWindow,width=5)
    entry4i.place(x=740,y=670)
    entry4i.insert(0,T4i)

    T4j1=(math.exp(-math.sqrt(35/k3)*15)*130)+20
    T4j = round(T4j1,2)
    entry4j=tk.Entry(mainWindow,width=5)
    entry4j.place(x=825,y=670)
    entry4j.insert(0,T4j)

    T4k1=(math.exp(-math.sqrt(35/k3)*18)*130)+20
    T4k = round(T4k1,2)
    entry4k=tk.Entry(mainWindow,width=5)
    entry4k.place(x=910,y=670)
    entry4k.insert(0,T4k)

    T4l1=(math.exp(-math.sqrt(35/k3)*20)*130)+20
    T4l = round(T4l1,2)
    entry4l=tk.Entry(mainWindow,width=5)
    entry4l.place(x=995,y=670)
    entry4l.insert(0,T4l)


    Q21 = math.sqrt(5521.376*k1)*130
    Q2=round(Q21,2)
    entry2A=tk.Entry(mainWindow, width=8)
    entry2A.place(x=1055,y=295)
    entry2A.insert(0,Q2)
    entry2A.config(font="5")

    Q31 = math.sqrt(5521.376*k2)*130
    Q3=round(Q31,2)
    entry3A=tk.Entry(mainWindow, width=8)
    entry3A.place(x=1055,y=495)
    entry3A.insert(0,Q3)
    entry3A.config(font="5")

    Q41 = math.sqrt(5521.376*k3)*130
    Q4=round(Q41,2)
    entry4A=tk.Entry(mainWindow, width=8)
    entry4A.place(x=1055,y=695)
    entry4A.insert(0,Q4)
    entry4A.config(font="5")

    ε21 = Q2/(57148)
    ε2=round(ε21,2)
    entry2B=tk.Entry(mainWindow, width=5)
    entry2B.place(x=1175,y=295)
    entry2B.insert(0,ε2)
    entry2B.config(font="5")

    ε31 = Q3/(57148)
    ε3=round(ε31,2)
    entry3B=tk.Entry(mainWindow, width=5)
    entry3B.place(x=1175,y=495)
    entry3B.insert(0,ε3)
    entry3B.config(font="5")

    ε41 = Q4/(57148)
    ε4=round(ε41,2)
    entry4B=tk.Entry(mainWindow, width=5)
    entry4B.place(x=1175,y=695)
    entry4B.insert(0,ε4)
    entry4B.config(font="5")


def explanation():
    secondWindow = tk.Tk()
    secondWindow.configure()
    secondWindow.title("Explanation")
    secondWindow.geometry("650x650")

    label11 = tk.Label(secondWindow, text="Explanation", fg="red", font="times 18 bold")
    label11.pack()

    label12 = tk.Label(secondWindow, text="For an Infinite Fin", fg="black", font="times 15 bold")
    label12.place(x=210,y=30)

    C6 = tk.Canvas(secondWindow, height=450 ,width=450)
    C6.place(x=40,y=80)
    C6.create_text(60,40, text="θ", font="bold")
    C6.create_line(50,50,70,50, fill="black")
    C6.create_text(60,60, text="θb", font="bold")
    C6.create_text(80,40, text="=", font="bold")
    C6.create_text(110,40, text="e⁻ᵐˣ", font="bold")
    C6.create_text(250,40, text="where m =", font="bold")
    C6.create_line(320,20,320,80, fill="black")
    C6.create_line(320,20,410,20, fill="black")
    C6.create_line(300,70,320,80, fill="black")
    C6.create_line(320,48,410,48, fill="black")
    C6.create_text(360,35, text="h P", font="bold")
    C6.create_text(360,60, text="k Ac", font="bold")
    C6.create_text(60,300, text="Qfin =", font="bold")
    C6.create_line(110,280,110,320, fill="black")
    C6.create_line(110,280,200,280, fill="black")
    C6.create_line(95,310,110,320, fill="black")
    C6.create_text(160,295, text="h P k Ac", font="bold")
    C6.create_text(220,295, text="θb", font="bold")




button1 = tk.Button(mainWindow, text="SOLVE", font="times 15 bold", command=lambda:solve())
button1.place(x=1360,y=390)

button2 = tk.Button(mainWindow, text="EXPLANATION", font="times 15 bold", command=lambda:explanation())
button2.place(x=1360,y=590)

C5 = tk.Canvas(mainWindow, height=500 ,width=3, background="white")
C5.place(x=1035,y=240)
C5.create_line(2,2,1,980, fill="black")

label7 = tk.Label(mainWindow, text="Q(watt)", font="3", bg="white", background="white")
label7.place(x=1055,y=240)

C6 = tk.Canvas(mainWindow, height=500 ,width=3, background="white")
C6.place(x=1155,y=240)
C6.create_line(2,2,1,980, fill="black")

label8 = tk.Label(mainWindow, text="Effectiveness(ε)", font="3", bg="white")
label8.place(x=1175,y=240)

C7 = tk.Canvas(mainWindow, height=100, width=400, background="white")
C7.place(x=1070,y=120)
path="""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"""
gif1 = PhotoImage(data=path)
image = C7.create_image(1, 0, image=gif1, anchor=NW)

label9 = tk.Label(mainWindow, text="(x distances are in cm)", bg="white")
label9.place(x=900,y=335)

label10 = tk.Label(mainWindow, text="(x distances are in cm)", bg="white")
label10.place(x=900,y=535)

label11 = tk.Label(mainWindow, text="(x distances are in cm)", bg="white")
label11.place(x=900,y=735)

label12 = tk.Label(mainWindow, text="ambient temperature=20 °C", bg="white")
label12.place(x=80,y=390)

label13 = tk.Label(mainWindow, text="ambient temperature=20 °C", bg="white")
label13.place(x=80,y=590)


mainWindow.mainloop()