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

## Iniciando projeto 

Apos `python manage.py startapp escola`  em *views* de escola mudar de `from django.shortcuts import render ` para `from django.http import JsonResponse` --> pois a API vai retornar um `JSON`


## Django rest download

```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```
 Apos download colocar como INSTALLED APP

## Criando models commit_id = 01 (cid 01)

## Configurando admin  cid 02

- Importar models para admin de escola
- Configurando classes do admin
  
## Serializers  cid 03

- Converte o model para algo que consegue virar json.
    - Estamos fazendo isso para configurar o view 
- Filtra os dados que vao para api

## View set em views dos apps cid 04

- Rotas criadas
- Json retornado

## PUT e PATCH cid 05

- PUT: Substitui todo o recurso 
- PATCH: Atualiza um conjunto selecionado dentro de um recurso

### testando por minha conta server local cors cid 06

## criando matriculas e relacionam alunos com cursos cid 07

## Listando com novas rotas cid 08

## autenticacao basica para views cid 09


## criacao de novo projeto implementando validacao de campos cid 10

## Criando filtro de celular com expressoes regulares cid 11

## Instalando e usando o doc-br-> pacote de verificacao de doc do brasil cid 12  

## Paginacao cid 13

## Ordenacao cid 14

## Busca e Filtro cid 15