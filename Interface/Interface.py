import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
from Buscas.BuscaAestrela import BuscaAestrela
from Buscas.BuscaHorizontal import BuscaHorizontal
import time

class Interface:
    def __init__(self, root):
        self.root = root
        root.title("Puzzle 8")

        self.estado_inicial = [[0, 2, 3], [1, 4, 5], [6, 7, 8]]
        self.estado_final = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.solucao = None

        # Carrega as imagens para cada peça
        self.imagens = []
        for i in range(9):
            caminho_imagem = f"./img/imagem{i}.png"
            imagem = Image.open(caminho_imagem)
            imagem = imagem.resize((100, 100))
            self.imagens.append(ImageTk.PhotoImage(imagem))

        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.grid(row=0, column=0, rowspan=5, columnspan=3, padx=5, pady=5)

        self.puzzle_images = []
        for i in range(3):
            row_images = []
            for j in range(3):
                numero = self.estado_inicial[i][j]
                imagem = self.canvas.create_image(j * 100, i * 100, anchor=tk.NW, image=self.imagens[numero])
                row_images.append(imagem)
            self.puzzle_images.append(row_images)

        self.estado_inicial_label = ttk.Label(root, text=f"Estado Inicial: {self.estado_inicial}")
        self.estado_inicial_label.grid(row=5, column=0, columnspan=3, pady=(0, 5))

        self.estado_final_label = ttk.Label(root, text=f"Estado Final: {self.estado_final}")
        self.estado_final_label.grid(row=6, column=0, columnspan=3, pady=(0, 10))

        self.metodos = ["Busca Horizontal", "Busca A* (heurística g(x))", "Busca A* (heurística h(x))"]
        self.metodo_combobox = ttk.Combobox(root, values=self.metodos)
        self.metodo_combobox.set(self.metodos[0])
        self.metodo_combobox.grid(row=7, column=0, padx=5, pady=5, columnspan=3)

        self.embaralhar_button = ttk.Button(root, text="Embaralhar", command=self.embaralhar_e_atualizar_puzzle)
        self.embaralhar_button.grid(row=8, column=0, padx=5, pady=5)

        self.buscar_button = ttk.Button(root, text="Buscar Solução", command=self.buscar_solucao)
        self.buscar_button.grid(row=8, column=1, padx=5, pady=5)

        self.mostrar_solucao_button = ttk.Button(root, text="Mostrar Solução", command=self.mostrar_solucao, state=tk.DISABLED)
        self.mostrar_solucao_button.grid(row=8, column=2, padx=5, pady=5)

        self.mostrar_caminho_button = ttk.Button(root, text="Mostrar Caminho", command=self.mostrar_caminho, state=tk.DISABLED)
        self.mostrar_caminho_button.grid(row=9, column=0, columnspan=3, padx=5, pady=5)

        self.resultado_label = ttk.Label(root, text="Tempo de busca: N/A\nTamanho da árvore: N/A")
        self.resultado_label.grid(row=10, column=0, columnspan=3, pady=10)

    def embaralhar_e_atualizar_puzzle(self):
        numeros = list(range(9))
        random.shuffle(numeros)
        self.estado_inicial = [numeros[i:i+3] for i in range(0, 9, 3)]
        self.resetar_resultados()
        self.atualizar_puzzle()
        self.atualizar_estados_na_interface()
        self.solucao = None

    def atualizar_puzzle(self):
        for i in range(3):
            for j in range(3):
                numero = self.estado_inicial[i][j]
                self.canvas.itemconfig(self.puzzle_images[i][j], image=self.imagens[numero])

    def buscar_solucao(self):
        metodo = self.metodo_combobox.get()

        if metodo == "Busca Horizontal":
            busca = BuscaHorizontal(self.estado_inicial, self.estado_final)
        elif metodo == "Busca A* (heurística g(x))":
            busca = BuscaAestrela(self.estado_inicial, self.estado_final, 'G')
        elif metodo == "Busca A* (heurística h(x))":
            busca = BuscaAestrela(self.estado_inicial, self.estado_final, 'GH')
        else:
            return

        try:
            limite_tempo = 60
            inicio_tempo = time.time()

            self.resultado_label.config(text="Buscando solução...")
            self.root.update()

            self.solucao = None
            while time.time() - inicio_tempo < limite_tempo:
                self.solucao, tempo, tamanho_arvore = busca.buscar()
                if self.solucao:
                    break

            if self.solucao:
                self.mostrar_resultados(tempo, tamanho_arvore, True)
                self.root.update()
                self.mostrar_solucao_button.config(state=tk.NORMAL)
                self.mostrar_caminho_button.config(state=tk.NORMAL) 
            else:
                self.mostrar_resultados(0, 0, False)
                self.resultado_label.config(text="Solução não encontrada.")
                self.mostrar_solucao_button.config(state=tk.NORMAL)
                self.mostrar_caminho_button.config(state=tk.NORMAL)
                self.root.update()

        except Exception as e:
            self.resultado_label.config(text="")
            self.mostrar_solucao_button.config(state=tk.NORMAL)
            self.mostrar_caminho_button.config(state=tk.NORMAL)
            self.root.update()
            messagebox.showwarning("Importante", f"Não foi possível encontrar uma solução.")

    def mostrar_solucao(self):
        if self.solucao:
            self.animar_solucao(self.solucao)

    def mostrar_caminho(self):
        if self.solucao:
            caminho = "\n".join([f"Passo {i + 1}:\n{self.formatar_estado(estado)}" for i, estado in enumerate(self.solucao)])

            # Cria uma nova janela para exibir o caminho da solução
            caminho_window = tk.Toplevel(self.root)
            caminho_window.title("Caminho da Solução")

            # Cria um widget de texto para exibir o caminho da solução
            text_widget = tk.Text(caminho_window, wrap=tk.WORD, width=40, height=20)
            text_widget.insert(tk.END, caminho)
            text_widget.pack()

    def mostrar_resultados(self, tempo, tamanho_arvore, encontrou_solucao):
        if encontrou_solucao:
            self.resultado_label.config(text=f"Tempo de busca: {tempo} segundos\nTamanho da árvore: {tamanho_arvore} nós")
        else:
            self.resultado_label.config(text="Solução NÃO encontrada!")

    def resetar_resultados(self):
        self.resultado_label.config(text="Tempo de busca: N/A\nTamanho da árvore: N/A")

    def animar_solucao(self, solucao):
        for passo, estado in enumerate(solucao):
            for i in range(3):
                for j in range(3):
                    numero = estado[i][j]
                    self.canvas.itemconfig(self.puzzle_images[i][j], image=self.imagens[numero])
                    self.root.update()
                    self.root.after(90)

    def atualizar_estados_na_interface(self):
        self.estado_inicial_label.config(text=f"Estado Inicial: {self.estado_inicial}")
        self.estado_final_label.config(text=f"Estado Final: {self.estado_final}")

    def formatar_estado(self, estado):
        return "\n".join([" ".join(map(str, row)) for row in estado])

