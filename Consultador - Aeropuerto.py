import tkinter as tk
from tkinter import Canvas


def main():

    def cerrar():
        marco.destroy()

    marco = tk.Tk()
    marco.title("Consultar Clientes")
    marco.geometry("500x500")
    marco.configure(bg="black")

    l1 = tk.Label(marco, text="Consultar tabla por origen", bg="black", fg="red").grid(row=0,
                                                                                       column=0)
    l2 = tk.Label(marco, text="Consultar tabla por destino", bg="black", fg="red").grid(row=1,
                                                                                        column=0)
    l3 = tk.Label(marco, text="Consultar tabla por aerolinea", bg="black", fg="red").grid(row=2,
                                                                                          column=0)
    l4 = tk.Label(marco, text="Consultar tabla por fecha", bg="black", fg="red").grid(row=3,
                                                                                      column=0)

    def Consulc():
        marcocc = tk.Entry(marco, width = 20, bg="red" , fg="black").grid(row=2,
                                                                           column=1,
                                                                           sticky=tk.W,
                                                                           pady=4)

    tk.Button(marco,
              text="Consultar", command=Consulc, bg="black", fg="red").grid(row=0,
                                                                           column=1,
                                                                           sticky=tk.W,
                                                                           pady=4)

    tk.Button(marco,
              text="Consultar", command=cerrar, bg="black", fg="red").grid(row=1,
                                                                           column=1,
                                                                           sticky=tk.W,
                                                                           pady=4)

    tk.Button(marco,
              text="Consultar", command=cerrar, bg="black", fg="red").grid(row=2,
                                                                           column=1,
                                                                           sticky=tk.W,
                                                                           pady=4)

    tk.Button(marco,
              text="Consultar", command=cerrar, bg="black", fg="red").grid(row=3,
                                                                           column=1,
                                                                           sticky=tk.W,
                                                                           pady=4)

    tk.Button(marco,
              text="Cerrar", command=cerrar, bg="black", fg="red").grid(row=4,
                                                                        column=0,
                                                                        sticky=tk.W,
                                                                        pady=4)

    
    
    marco.mainloop()


if __name__ == "__main__":
    main()