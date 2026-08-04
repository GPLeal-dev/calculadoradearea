"""Interface gráfica da calculadora de áreas."""

import tkinter as tk
from tkinter import ttk

from calculos_area import area_circulo, area_quadrado, area_retangulo, area_triangulo


class CalculadoraAreaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Áreas")
        self.resizable(False, False)
        self.configure(padx=32, pady=28)

        self.forma = tk.StringVar(value="Quadrado")
        self.entradas = []
        self.area_texto = tk.StringVar(value="Área: -- m²")
        self.erro_texto = tk.StringVar()

        ttk.Label(self, text="Calculadora de Áreas", font=("Arial", 24, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(0, 20)
        )
        ttk.Label(self, text="Forma geométrica:", font=("Arial", 14)).grid(
            row=1, column=0, sticky="w"
        )
        seletor = ttk.Combobox(
            self,
            textvariable=self.forma,
            values=("Quadrado", "Retângulo", "Triângulo", "Círculo"),
            state="readonly",
            width=18,
            font=("Arial", 14),
        )
        seletor.grid(row=1, column=1, sticky="ew", pady=(0, 16))
        seletor.bind("<<ComboboxSelected>>", self.montar_campos)

        self.campos_frame = ttk.Frame(self)
        self.campos_frame.grid(row=2, column=0, columnspan=2)

        self.desenho = tk.Canvas(
            self, width=300, height=210, bg="white", highlightthickness=1,
            highlightbackground="#b0b0b0"
        )
        self.desenho.grid(row=3, column=0, columnspan=2, pady=(20, 10))

        ttk.Label(self, textvariable=self.area_texto, font=("Arial", 19, "bold")).grid(
            row=4, column=0, columnspan=2, pady=(12, 5)
        )
        ttk.Label(
            self, textvariable=self.erro_texto, foreground="firebrick", font=("Arial", 12)
        ).grid(row=5, column=0, columnspan=2)

        self.montar_campos()

    def montar_campos(self, evento=None):
        for widget in self.campos_frame.winfo_children():
            widget.destroy()

        nomes = {
            "Quadrado": ("Lado",),
            "Retângulo": ("Base", "Altura"),
            "Triângulo": ("Base", "Altura"),
            "Círculo": ("Raio",),
        }[self.forma.get()]

        self.entradas = []
        for linha, nome in enumerate(nomes):
            valor = tk.StringVar()
            valor.trace_add("write", self.calcular_area)
            self.entradas.append(valor)

            ttk.Label(self.campos_frame, text=f"{nome}:", font=("Arial", 14)).grid(
                row=linha, column=0, sticky="w", pady=3
            )
            ttk.Entry(self.campos_frame, textvariable=valor, width=18, font=("Arial", 14)).grid(
                row=linha, column=1, padx=(10, 5), pady=3
            )
            ttk.Label(self.campos_frame, text="m", font=("Arial", 14)).grid(
                row=linha, column=2, sticky="w"
            )

        self.area_texto.set("Área: -- m²")
        self.erro_texto.set("")
        self.desenhar_forma()

    def desenhar_forma(self):
        self.desenho.delete("all")
        cor = "#4f8fdd"
        forma = self.forma.get()

        if forma == "Quadrado":
            self.desenho.create_rectangle(90, 30, 210, 150, fill=cor, outline="#1d5fa7", width=3)
        elif forma == "Retângulo":
            self.desenho.create_rectangle(45, 55, 255, 140, fill=cor, outline="#1d5fa7", width=3)
        elif forma == "Triângulo":
            self.desenho.create_polygon(150, 25, 50, 160, 250, 160, fill=cor, outline="#1d5fa7", width=3)
        else:
            self.desenho.create_oval(80, 25, 220, 165, fill=cor, outline="#1d5fa7", width=3)

        self.desenho.create_text(150, 190, text=forma, font=("Arial", 14, "bold"), fill="#222")

    def calcular_area(self, *args):
        valores = [entrada.get().strip().replace(",", ".") for entrada in self.entradas]
        if not all(valores):
            self.area_texto.set("Área: -- m²")
            self.erro_texto.set("")
            return

        funcoes = {
            "Quadrado": area_quadrado,
            "Retângulo": area_retangulo,
            "Triângulo": area_triangulo,
            "Círculo": area_circulo,
        }
        try:
            area = funcoes[self.forma.get()](*valores)
        except ValueError as erro:
            self.area_texto.set("Área: -- m²")
            self.erro_texto.set(f"Erro: {erro}")
        else:
            self.area_texto.set(f"Área: {area:.2f} m²")
            self.erro_texto.set("")


if __name__ == "__main__":
    CalculadoraAreaApp().mainloop()
