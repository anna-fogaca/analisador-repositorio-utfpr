import requests
import re
from collections import Counter, defaultdict
from bs4 import BeautifulSoup

#! AQUI É O URL DO REPOSITÓRIO DO CPGEI, PORÉM, DÁ PRA ATUALIZAR ONDE O USUÁRIO ESCOLHE QUAL MESTRADO SERÁ ANALISADO!
BASE_URL = "https://repositorio.utfpr.edu.br/jspui/handle/1/2101?offset={offset}"
HEADERS = {"User-Agent": "Mozilla/5.0"}
TOTAL_PAGINAS = 20 #! Número de páginas do repositório do mestrado

stopwords = set([
    "de", "do", "da", "e", "a", "o", "em", "para", "com", "no", "na", "dos", "das", "por",
    "um", "uma", "sobre", "ao", "à", "se", "são", "as", "os", "que", "pelos", "pelo", "and", 
    "for", "usando", "using", "utilizando", "análise", "sistema", "desenvolvimento", "avaliação",
    "caracterização", "baseado", "aplicação", "implementação", "meio", "classficação", "caracterização",
    "sistemas", "modelo", "baseada", "sem", "técnica", "técnicas", "aplicado", "baseados", "proposta", "orientado"
])

traducao = {
    "networks": "redes",
    "learning": "aprendizagem",
    "machine": "máquina",
    "urban": "urbano",
    "analysis": "análise",
}

agrupamento_manual = {
    "redes": "rede",
    "sensores": "sensor",
    "fibras": "fibra",
    "óticas": "ótica",
    "baseados": "baseado",
    "aprendizagem": "aprendizado",
}

temas = {
    "IA / Machine Learning": ["aprendizagem", "aprendizado", "neurais"],
    "IoT / Sensoriamento": ["sensor", "monitoramento", "ultrassom", "medição", "rede"],
    "Telecom / Fibras Ópticas": ["fibra", "ótica", "bragg", "comunicação", "fio"],
    "Energia e Eletricidade": ["energia", "elétrica", "potência"],
    "Transporte e Veículos": ["transporte", "veículos"],
    "Visão Computacional": ["imagens", "detecção"],
    "Engenharia e Controle": ["controle", "simulação", "método", "desempenho", "modelagem", "otimização"],
    "Computação / Dados": ["programação", "dados", "tecnologia", "rede", "mapeamento"],
    "Sustentabilidade / Ambiente": ["ambiente", "sustentabilidade", "água"],
    "Educação e Matemática": ["matemática", "estudo", "proposta"],
    "Redes Neurais": ["neurais"]
}

def formatar_nome(nome_raw):
    if "," in nome_raw:
        sobrenome, nome = nome_raw.split(",", 1)
        sobrenome = sobrenome.strip().upper()
        nome = nome.strip()
        return f"{nome} {sobrenome}"
    return nome_raw

def raspar_dados(total_paginas):
    resultados = []
    for i in range(total_paginas):
        offset = i * 20
        url = BASE_URL.format(offset=offset)
        resposta = requests.get(url, headers=HEADERS)
        if resposta.status_code != 200:
            print(f"Erro ao acessar a página {url}")
            continue
        sopa = BeautifulSoup(resposta.content, 'html.parser')
        linhas = sopa.select("table tr")[1:]  # Ignora cabeçalho
        for linha in linhas:
            colunas = linha.find_all("td")
            if len(colunas) >= 5:
                titulo = colunas[2].get_text(strip=True)
                autor = colunas[3].get_text(strip=True)
                orientador_raw = colunas[4].get_text(strip=True)
                orientador = formatar_nome(orientador_raw)
                resultados.append((titulo, autor, orientador))
    return resultados

def limpar_e_filtrar_palavras(titulos):
    texto_titulos = " ".join(titulos).lower()
    texto_limpo = re.sub(r'[^a-zà-ú\s]', '', texto_titulos)
    palavras = texto_limpo.split()
    palavras_filtradas = [p for p in palavras if p not in stopwords and len(p) > 2]
    return palavras_filtradas

def traduzir_palavras(palavras):
    palavras_traduzidas = []
    for palavra in palavras:
        if palavra in traducao:
            palavras_traduzidas.append(traducao[palavra])
        else:
            palavras_traduzidas.append(palavra)
    return palavras_traduzidas

def normalizar_palavras(palavras):
    palavras_normalizadas = []
    for palavra in palavras:
        if palavra in agrupamento_manual:
            palavras_normalizadas.append(agrupamento_manual[palavra])
        else:
            palavras_normalizadas.append(palavra)
    return palavras_normalizadas

def contar_palavras(palavras):
    contagem = Counter(palavras)
    return contagem.most_common(40)

def contar_por_tema(titulos):
    contagem_tematica = {tema: 0 for tema in temas}
    for titulo in titulos:
        palavras_titulo = re.sub(r'[^a-zà-ú\s]', '', titulo.lower()).split()
        palavras_filtradas = [p for p in palavras_titulo if p not in stopwords and len(p) > 2]
        for tema, palavras_chave in temas.items():
            if any(p in palavras_filtradas for p in palavras_chave):
                contagem_tematica[tema] += 1
    return contagem_tematica


def orientadores_por_tema(resultados, stopwords, temas):
    orientadores_por_tema = defaultdict(list)
    for titulo, _, orientador in resultados:
        palavras_titulo = re.sub(r'[^a-zà-ú\s]', '', titulo.lower()).split()
        palavras_filtradas = [p for p in palavras_titulo if p not in stopwords and len(p) > 2]

        for tema, palavras_chave in temas.items():
            if any(p in palavras_filtradas for p in palavras_chave):
                orientadores_por_tema[tema].append(orientador)

    resultado = {}  # Dicionário para armazenar o orientador mais comum de cada tema
    for tema, orientadores in orientadores_por_tema.items():
        if orientadores:
            mais_comum = Counter(orientadores).most_common(1)[0][0]
            resultado[tema] = mais_comum
        else:
            resultado[tema] = "Nenhum"  # Caso não haja orientador para o tema

    return resultado

def main():
    resultados = raspar_dados(TOTAL_PAGINAS)
    for titulo, autor, orientador in resultados:
        print(f"Título: {titulo}")
        print(f"Autor(a): {autor}")
        print(f"Orientador: {orientador}")
        print("-" * 60)
    
    titulos = [titulo for titulo, _, _ in resultados]
    palavras_filtradas = limpar_e_filtrar_palavras(titulos)
    palavras_traduzidas = traduzir_palavras(palavras_filtradas)
    palavras_normalizadas = normalizar_palavras(palavras_traduzidas)
    mais_comuns = contar_palavras(palavras_normalizadas)
    orientadores_mais_comum = orientadores_por_tema(resultados, stopwords, temas)

    print("\nPalavras mais comuns nos títulos:")
    n = 1
    for palavra, freq in mais_comuns:
        print(f"{n}) {palavra}: {freq}")
        n += 1

    contagem_tematica = contar_por_tema(titulos)
    print("\nDistribuição por área temática:")
    for tema, qtd in contagem_tematica.items():
        print(f"- {tema}: {qtd} títulos")

    print("\nOrientadores mais comuns por tema:")
    for tema, orientador in orientadores_mais_comum.items():
        print(f"- {tema}: {orientador}")

if __name__ == "__main__":
    main()
