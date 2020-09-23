# Bot Instagram
- [Bot Instagram](#bot-instagram)
  - [1. Sobre o Bot](#1-sobre-o-bot)
  - [2. Ferramentas necessárias para execução](#2-ferramentas-necessárias-para-execução)
  - [3. Preenchendo os campos](#3-preenchendo-os-campos)
## 1. Sobre o Bot
 Este é um Bot para comentários automáticos em sorterios do Instagram, espero que goste, caso eu esteje certo deixe uma star!

## 2. Ferramentas necessárias para execução
 Atualmente tenho usado o navegador Firefox, logo escolhi ele para o bot executar suas ações, o editor de código que estou usando é o VS Code.
 * Primeiramente deve-se baixar o Python caso não o tenha ainda. [Dowload Python](https://www.python.org/downloads/)
 * Baixe o Mozilla Firefox. [Dowload Firefox](https://www.mozilla.org/pt-BR/firefox/new/)
 * Abra o terminal e execute os seguintes comandos para instalar as bibliotecas necessárias.
```
* pip install PySimpleGUI
* pip install selenium
```
 * Baixar o geckodriver de acordo com seu sistema operacional. Recomendo o dowload da versão mais recente! [Dowload geckodriver](https://github.com/mozilla/geckodriver/releases)
 * Extrair e colocar o arquivo em uma  pasta de fácil acesso, EX: C:, Desktop.
 * Verifique o caminho do `geeckodriver` na linha 17.
 * Abra o seu editor de código preferido e execute o arquivo `BotInstagram.py`.

## 3. Preenchendo os campos
 * Coloque o nome de usuário.
 * Coloque a senha.
 * Coloque a URL da foto.
 * Escreva os comentários que deseja comentar separados por `,` um após o outro, para marcar pessoas coloque `@usuario`.