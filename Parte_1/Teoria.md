# Parte 1

## Sumario

- Criando api's 
- Vinculando adm 
- Padrao Rest

## Primeiros passos

- Instalando Django numa versao
    - `pip install Django==3.0.7`
- Crie um Ambiente Virtual
    - `python3 -m venv ./venv`
    - `source venv/bin/activate` --> Ativando no unix
    - `venv\Scripts\activate.bat` --> Ativando no Windows
- Baixando no venv
    - `pip3 install django` 
- Criar um projeto *setup*
  - `django-admin startproject setup .`
- Mudando settings.py
  - `LENGUAGE = pt-br`
  - `TIMEZONE = America/Sao_Paulo`

## Oq é uma API?

- Tecnologia que recebe requisicoes, busca em alguma outra tecnologia e retorna a resposta para quem requisitou em um formato `JSON` ou `XML`.

