import tkinter

font1 = ("Calibri", 14)
padx1 = 10
pady1 = 10

def main():
    window = tkinter.Tk()
    window.minsize(height=100, width=600)
    window.config(padx=padx1, pady=pady1)
    window.title("Mile to km converter")
    
    miles = tkinter.Label(text="Miles : ", font=font1)
    
    miles_in = tkinter.Entry(font=font1)
    
    
    def convert_to_km():
        try:
            output = round(float(miles_in.get()) * 1.609344, 2)
        except ValueError:
            output = "ValueError"
        km_out.config(text=output)
    
    
    def convert_to_mile():
        try:
            output = round(float(km_in.get()) * 0.621371, 2)
        except ValueError:
            output = "ValueError"
        mile_out.config(text=output)
        
        
    mile_to_km = tkinter.Button(text="Convert to KM",command=convert_to_km, font=font1)
    
    km_out = tkinter.Label(font=font1)
    
    kms = tkinter.Label(text="Kms : ", font=font1)
    km_in = tkinter.Entry(font=font1)
    km_to_mile = tkinter.Button(text="Convert to Miles", command=convert_to_mile, font=font1)
    mile_out = tkinter.Label(font=font1)
    
    miles.grid(column=0, row=0)
    miles.config(padx=padx1, pady=pady1)
    
    miles_in.grid(column=1, row=0)
    
    mile_to_km.grid(column=2, row=0)
    # mile_to_km.config(padx=padx1, pady=pady1)
    
    km_out.grid(column=3, row=0)
    km_out.config(padx=padx1, pady=pady1)
    
    kms.grid(column=0, row=1)
    kms.config(padx=padx1, pady=pady1)
    
    km_in.grid(column=1, row=1)
    
    km_to_mile.grid(column=2, row=1)
    # km_to_mile.config(padx=padx1, pady=pady1)
    
    mile_out.config(padx=padx1, pady=pady1)
    mile_out.grid(column=3, row=1)
    
    window.mainloop()
    

main()