# 🗂️ aula-git

> Repositório de estudos em Python — Web Scraping, Automação com Selenium e Programação Orientada a Objetos (POO).

---

## 📌 Sobre

Este repositório reúne scripts desenvolvidos durante a prática de Python, cobrindo três frentes principais:

- 🕷️ **Web Scraping** com `requests` + `BeautifulSoup` + `pandas`
- 🤖 **Automação Web** com `Selenium`
- 🧩 **Programação Orientada a Objetos (POO)**

## 📚 Índice

| # | Arquivo | Tema |
|---|---|---|
| 1 | [`POO.py`](#1--poopy) | POO — Sistema bancário com herança |
| 2 | [`Meu_scraper.py`](#2--meu_scraperpy) | Requests — Headers HTTP customizados |
| 3 | [`Exercicio_frases.py`](#3--exercicio_frasespy) | Scraping — Frases com paginação |
| 4 | [`Projeto scraper de livros.py`](#4--projeto-scraper-de-livrospy) | Scraping — Catálogo de livros tratado |
| 5 | [`primeiro_selenium.py`](#5--primeiro_seleniumpy) | Selenium — Primeiro contato |
| 6 | [`Espera inteligiente.py`](#6--espera-inteligientepy) | Selenium — Espera explícita |
| 7 | [`iframe.py`](#7--iframepy) | Selenium — Manipulação de iframes |

---

## 1. `POO.py`

Modela um **sistema bancário** aplicando herança e sobrescrita de métodos.

- Todas herdam `titular`, `saldo`, `depositar()`, `sacar()` e `mostrar()` de `ContaBancaria`.
- Cada subclasse **sobrescreve** o comportamento relevante ao seu tipo de conta.
- No final, instâncias de cada classe são guardadas numa lista e exibidas em loop — demonstrando **polimorfismo**.

**Conceitos:** herança, `super()`, sobrescrita de métodos, polimorfismo.

---

## 2. `Meu_scraper.py`

Teste simples de envio de **headers HTTP customizados** numa requisição.

- Define um `User-Agent` de navegador para simular uma requisição "humana".
- Faz `GET` em `https://httpbin.org/user-agent` (serviço de teste que ecoa o header recebido).
- Imprime a resposta para confirmar que o header foi enviado corretamente.

**Conceitos:** `requests`, headers HTTP, boas práticas anti-bloqueio em scraping.

---

## 3. `Exercicio_frases.py`

Scraper que percorre **todas as páginas** de [quotes.toscrape.com](http://quotes.toscrape.com), coletando frases e autores.

- `while` que segue o botão **"next"** até não existir mais próxima página.
- Extrai `div.quote` → `span.text` (frase) + `small.author` (autor) com `BeautifulSoup`.
- Salva tudo em `frases_famosas.csv` via `pandas`.

**Saída:** `frases_famosas.csv`

---

## 4. `Projeto scraper de livros.py`

Versão mais robusta de scraper, para o catálogo de [books.toscrape.com](http://books.toscrape.com).

- Percorre todas as páginas usando `urljoin` para montar a URL da próxima página corretamente.
- Extrai de cada livro: **título**, **preço**, **avaliação** (estrelas) e **estoque**.
- Só processa a página se `status_code == 200` (trata falha de requisição).
- Limpa os dados com `pandas`: preenche avaliações ausentes com `"Sem Avaliação"` e remove linhas sem preço.
- Salva o resultado tratado em `Livros_Tratados.csv`.

**Saída:** `Livros_Tratados.csv`
**Diferencial:** trata erros de requisição e limpa os dados antes de salvar — mais avançado que o `Exercicio_frases.py`.

---

## 5. `primeiro_selenium.py`

Primeiro contato com **Selenium**: abre o Chrome, acessa `quotes.toscrape.com`, espera 5s e fecha.

- Usa `webdriver_manager` para gerenciar o `chromedriver` automaticamente.
- Não interage com a página — serve só para validar que a automação abre/fecha o navegador.

> ⚠️ A URL no código está como `"https:quotes.toscrape.com/"` (faltam as barras `//`). O Chrome geralmente corrige, mas o correto é `https://quotes.toscrape.com/`.

**Conceitos:** inicialização do driver, `webdriver_manager`, espera fixa (`time.sleep`).

---

## 6. `Espera inteligiente.py`

Evolução do anterior: usa **espera explícita** em vez de espera fixa.

- Acessa `https://demoqa.com/dynamic-properties` (elementos que mudam de estado dinamicamente).
- `WebDriverWait` + `expected_conditions.element_to_be_clickable` aguarda até 10s o botão `id="colorChange"` ficar clicável.
- Clica no botão e confirma no console.

**Conceitos:** `WebDriverWait`, `expected_conditions`, espera explícita vs. fixa.

---

## 7. `iframe.py`

Demonstra como o Selenium lida com **iframes**.

- Acessa `https://demoqa.com/frames`.
- Localiza todos os `<iframe>` da página.
- Para cada um: entra no iframe (`switch_to.frame`), extrai o texto do `<h1>`, e retorna ao contexto principal (`switch_to.default_content()`).
- Imprime a lista de textos extraídos.

**Conceitos:** `switch_to.frame`, `switch_to.default_content`, múltiplos iframes.

---

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-HTML%20Parser-yellow)
![Pandas](https://img.shields.io/badge/Pandas-DataFrames-purple)

Requisitos adicionais:

Google Chrome instalado (para os scripts com Selenium)
Python 3.x
▶️ Como executar
Copy
python "nome_do_arquivo.py"
💡 Arquivos com espaço no nome (ex: Projeto scraper de livros.py) precisam estar entre aspas no terminal.

💡 Melhorias futuras
 Adicionar try/except/finally nos scripts de Selenium para garantir drive.quit() mesmo em erro.
 Corrigir a URL sem // em primeiro_selenium.py.
 Padronizar nomes de arquivos (evitar espaços/acentos).
 Criar requirements.txt para instalação com um único comando.
 Adicionar testes automatizados para os scrapers.

## 📦 Instalação

```bash
pip install selenium webdriver-manager requests beautifulsoup4 pandas
