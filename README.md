<h1 align="center" style="font-weight: 900; font-size: 3rem; margin-bottom: 0.2em;">📚 Projeto de Análise de Teses - UTFPR</h1>

<p align="center" style="margin-bottom: 1em;">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python" style="margin:0 8px; height:28px;" />
  <img src="https://img.shields.io/badge/Qt-41CD52?style=flat&logo=qt&logoColor=white" alt="Qt" style="margin:0 8px; height:28px;" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg" alt="Python version" style="margin:0 6px; height:22px;" />
  <img src="https://img.shields.io/badge/Library-Requests-orange.svg" alt="Requests library" style="margin:0 6px; height:22px;" />
  <img src="https://img.shields.io/badge/Library-BeautifulSoup-green.svg" alt="BeautifulSoup library" style="margin:0 6px; height:22px;" />
  <img src="https://img.shields.io/badge/status-em--desenvolvimento-yellow.svg" alt="Em Desenvolvimento" style="margin:0 6px; height:22px;" />
  <img src="https://img.shields.io/badge/versão-0.1-red.svg" alt="versão 0.1" style="margin:0 6px; height:22px;" />
  <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License GPLv3" style="margin:0 6px; height:22px;" />
</p>

---

## 🚀 Sobre o Projeto

Este projeto realiza a raspagem, processamento e análise de dados acadêmicos do repositório de teses do Programa de Pós Graduação CPGEI da UTFPR. Coleta títulos, autores e orientadores, filtra e traduz palavras-chave, categoriza as teses por áreas temáticas e apresenta estatísticas importantes para facilitar a análise e pesquisa.

O projeto nasceu para me apoiar pessoalmente na análise dos temas mais frequentes em teses desse repositório da UTFPR. A ideia é entender:

1. Quais temas são mais abordados nas pesquisas acadêmicas do CPGEI;
2. Quais temas estão menos explorados, revelando lacunas e demandas para futuras pesquisas.

<p align="center">
  <img src="https://github.com/user-attachments/assets/10504a3c-d13b-48e1-b8f7-fd9becf2edc7" alt="Captura de tela 2025-07-05 014745" />
</p>

O foco inicial é me ajudar na preparação para tentar entrar no mestrado CPGEI — assim eu posso mapear as áreas com maior ou menor volume de produção científica, para direcionar melhor meus estudos e escolhas.

No futuro, quero expandir o sistema para que ele permita escolher outros programas de mestrado, abrindo espaço para uma análise mais ampla e útil para outros pesquisadores.

Esse projeto é meu aliado para tomar decisões mais informadas sobre a minha trajetória acadêmica e de pesquisa.

---

## ✨ Funcionalidades

- 🕸️ **Raspagem automática** dos dados das teses em até 20 páginas do repositório.
- 🧹 **Limpeza e filtragem** de palavras irrelevantes nos títulos.
- 🌍 **Tradução e normalização** de termos técnicos.
- 📊 **Contagem das palavras** mais frequentes nos títulos.
- 🎯 **Distribuição das teses por áreas temáticas** definidas.
- 👩‍🏫 **Identificação dos orientadores mais frequentes** em cada tema (implementada no back-end, sendo implementada no PyQT).

---

## Como rodar no seu computador

1) Baixe todos os arquivos do projeto e coloque-os na mesma pasta.
2) Tenha o Python instalado (versão 3.6 ou superior é recomendada).
3) Instale as dependências necessárias, caso ainda não tenha: ```requests, beautifulsoup4 e PyQt5. ```
4) Abra o terminal (cmd, PowerShell ou terminal do seu sistema).
5) Navegue até a pasta onde estão os arquivos baixados.
6) Execute o programa com o comando: python app.py
7) Pronto! A interface deve abrir e você pode explorar os dados.

O passo 4, 5 e 6 podem ser realizados de uma vez só pela sua IDE de preferência (como VS Code). 

## 📄 Licença

Este projeto está licenciado sob a Licença Pública Geral GNU versão 3 (GPLv3).  
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
