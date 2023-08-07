import tkinter

font1 = ("Calibri", 14)

def main():
    window = tkinter.Tk()
    window.minsize(height=100, width=600)
    window.title("Mile to km converter")
    
    miles = tkinter.Label(text="Miles : ", font=font1)
    miles_in = tkinter.Entry(font=font1)
    mile_to_km = tkinter.Button(text="Convert to KM",
                                command=lambda: km_out.config(
                                    text= f"{float(miles_in.get()) * 1.609}"
                                    ), font=font1)
    km_out = tkinter.Label(font=font1)
    
    kms = tkinter.Label(text="Kms : ", font=font1)
    km_in = tkinter.Entry(font=font1)
    km_to_mile = tkinter.Button(text="Convert to Miles", 
                                command=lambda : mile_out.config(
                                    text= f"{float(km_in.get()) * 0.621}"
                                ), font=font1)
    mile_out = tkinter.Label(font=font1)
    
    miles.grid(column=0, row=0)
    miles_in.grid(column=1, row=0)
    mile_to_km.grid(column=2, row=0)
    km_out.grid(column=3, row=0)
    
    kms.grid(column=0, row=1)
    km_in.grid(column=1, row=1)
    km_to_mile.grid(column=2, row=1)
    mile_out.grid(column=3, row=1)
    window.mainloop()
    

main()