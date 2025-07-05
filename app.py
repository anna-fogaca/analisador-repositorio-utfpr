import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout, QListWidget, QLabel, QTableWidget, QTableWidgetItem
import analisador 
from collections import defaultdict, Counter
import re

# Importa as funções do analisador
from analisador import ( 
    raspar_dados,
    limpar_e_filtrar_palavras,
    traduzir_palavras,
    normalizar_palavras,
    contar_palavras,
    contar_por_tema,
    orientadores_por_tema,
)

# Roda as funções para obter os dados
resultados = analisador.raspar_dados(analisador.TOTAL_PAGINAS)
titulos = [titulo for titulo, _, _ in resultados]
palavras_filtradas = analisador.limpar_e_filtrar_palavras(titulos)
palavras_traduzidas = analisador.traduzir_palavras(palavras_filtradas)
palavras_normalizadas = analisador.normalizar_palavras(palavras_traduzidas)
mais_comuns = analisador.contar_palavras(palavras_normalizadas)
contagem_tematica = analisador.contar_por_tema(titulos)

class MainWindow(QTabWidget):
    def __init__(self, resultados, mais_comuns, contagem_tematica):
        super().__init__()
        self.setWindowTitle("Analisador de Títulos de Teses")
        self.resize(1200, 800)
        self.resultados = resultados
        self.mais_comuns = mais_comuns
        self.contagem_tematica = contagem_tematica
        self.criar_aba_lista()
        self.criar_aba_palavras()
    
    def criar_aba_lista(self):
        aba = QWidget()
        layout = QVBoxLayout()

        tabela = QTableWidget()
        tabela.setColumnCount(3)
        tabela.setHorizontalHeaderLabels(["Título", "Autor(a)", "Orientador"])

        tabela.setRowCount(len(self.resultados))

        for linha, (titulo, autor, orientador) in enumerate(self.resultados):
            tabela.setItem(linha, 0, QTableWidgetItem(titulo))
            tabela.setItem(linha, 1, QTableWidgetItem(autor))
            tabela.setItem(linha, 2, QTableWidgetItem(orientador))

        tabela.resizeColumnsToContents()
        layout.addWidget(tabela)
        aba.setLayout(layout)
        self.addTab(aba, "Títulos")


    def criar_aba_palavras(self):
        aba = QWidget()
        layout = QVBoxLayout()

        titulo = QLabel("Palavras mais frequentes nos títulos")
        lista = QListWidget()

        n = 1

        for palavra, freq in self.mais_comuns:
            lista.addItem(f"{n}): {palavra}: {freq}")
            n += 1
        
        layout.addWidget(titulo)
        layout.addWidget(lista)
        aba.setLayout(layout)
        self.addTab(aba, "Palavras Frequentes")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    total_paginas = 20
    resultados = raspar_dados(total_paginas)
    titulos = [titulo for titulo, _, _ in resultados]
    palavras_filtradas = limpar_e_filtrar_palavras(titulos)
    palavras_traduzidas = traduzir_palavras(palavras_filtradas)
    palavras_normalizadas = normalizar_palavras(palavras_traduzidas)
    mais_comuns = contar_palavras(palavras_normalizadas)
    contagem_tematica = contar_por_tema(titulos)
    
    janela = MainWindow(resultados, mais_comuns, contagem_tematica)
    janela.setWindowTitle("Analisador de Repositório - Mestrado UTFPR")
    janela.resize(1200, 800)
    janela.show()
    
    sys.exit(app.exec_())

