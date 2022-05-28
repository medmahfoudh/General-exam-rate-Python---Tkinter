from tkinter import *

window = Tk()
window.config(padx=40 , pady=40)
window.title('Calculatrice Moyenne DS')

c_math,c_pc,c_fr,c_si,c_info,c_ang=14,12,10,5,5,3
total_c=c_math+c_pc+c_fr+c_ang+c_info+c_si


n_math_ds1=Label(text='Note DS1 math:',font=('Courrier',12,'bold'))
n_math_ds1.grid(column=0, row=0)
n_math_ds1.config(padx=1,pady=1)
input_n_math_ds1 = Entry()
input_n_math_ds1.grid(column=0 , row=1)


n_math_ds2=Label(text='Note DS2 math:',font=('Courrier',12,'bold'))
n_math_ds2.grid(column=1, row=0)
n_math_ds2.config(padx=1,pady=1)
input_n_math_ds2 = Entry()
input_n_math_ds2.grid(column=1 , row=1)

n_pc_ds1=Label(text='Note DS1 pc:',font=('Courrier',12,'bold'))
n_pc_ds1.grid(column=0, row=2)
n_pc_ds1.config(padx=2,pady=1)
input_n_pc_ds1 = Entry()
input_n_pc_ds1.grid(column=0 , row=3)

n_pc_ds2=Label(text='Note DS2 pc:',font=('Courrier',12,'bold'))
n_pc_ds2.grid(column=1, row=2)
n_pc_ds2.config(padx=2,pady=1)
input_n_pc_ds2 = Entry()
input_n_pc_ds2.grid(column=1 , row=3)

n_info_ds=Label(text='Note DS info:',font=('Courrier',12,'bold'))
n_info_ds.grid(column=0, row=4)
n_info_ds.config(padx=2,pady=1)
input_n_info_ds = Entry()
input_n_info_ds.grid(column=0 , row=5)

n_si_ds=Label(text='Note DS SII:',font=('Courrier',12,'bold'))
n_si_ds.grid(column=1, row=4)
n_si_ds.config(padx=2,pady=1)
input_n_si_ds = Entry()
input_n_si_ds.grid(column=1 , row=5)

n_ang_ds=Label(text='Note DS Anglais:',font=('Courrier',12,'bold'))
n_ang_ds.grid(column=0, row=6)
n_ang_ds.config(padx=2,pady=1)
input_n_ang_ds = Entry()
input_n_ang_ds.grid(column=0 , row=7)

n_fr_ds=Label(text='Note DS Français:',font=('Courrier',12,'bold'))
n_fr_ds.grid(column=1, row=6)
n_fr_ds.config(padx=2,pady=1)
input_n_fr_ds = Entry()
input_n_fr_ds.grid(column=1 , row=7)

moyenne_ds_math=Label(text=' ', font=('courrier' , 10 , 'bold') )
moyenne_ds_math.grid(column=0 , row = 8)

def moyenne_tous_les_matieres():
    n_math_ds1=float(input_n_math_ds1.get())
    n_math_ds2=float(input_n_math_ds2.get())
    imoyenne_ds_math=(n_math_ds1+n_math_ds2)/2
   
    n_pc_ds1=float(input_n_pc_ds1.get())
    n_pc_ds2=float(input_n_pc_ds2.get())
    imoyenne_ds_pc=(n_pc_ds1+n_pc_ds2)/2
    
    moyenne_info_ds=float(input_n_info_ds.get())
    moyenne_si_ds=float(input_n_si_ds.get())
    moyenne_fr_ds=float(input_n_fr_ds.get())
    moyenne_ang_ds=float(input_n_ang_ds.get())
    
    moyenne_generale_de_la_ds=((imoyenne_ds_math*c_math)+(imoyenne_ds_pc*c_pc)+(moyenne_fr_ds*c_fr)+(moyenne_ang_ds*c_ang)+(moyenne_si_ds*c_si)+(moyenne_info_ds*c_info))/total_c
    moyenne_ds_math['text']= 'Moyenne Generale de la DS: ' + str(moyenne_generale_de_la_ds)

    
button_moyenne_ds_math=Button(text='Cliquer pour decouvrir Le Moyenne Generale de la DS' , command=moyenne_tous_les_matieres)
button_moyenne_ds_math.grid(column=1 , row= 9 )

window.mainloop()

