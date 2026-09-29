# ROMPA

## Descrição do Projeto

Este repositório contém a plataforma ROMPA, desenvolvida em grupo para a disciplina de Engenharia de Software I, com a metodologia Scrum. O sistema busca conscientizar homens sobre a violência contra as mulheres e sobre como a omissão contribui para sua perpetuação, por meio de conteúdo educativo, um quiz, um simulador de situações e um manifesto de compromisso.

O trabalho cobriu o ciclo completo de desenvolvimento: levantamento de requisitos, análise, modelagem em UML, implementação e validação.

## Metodologia

O projeto foi desenvolvido por cinco integrantes, organizado em quatro sprints: levantamento de requisitos, análise do sistema, modelagem e desenvolvimento com validação. Os requisitos foram levantados com brainstorming e entrevistas informais e documentados em histórias de usuário e casos de uso.

A modelagem (casos de uso, classes, pacotes, atividades e sequência) estão na [documentação do projeto](docs/ROMPA.pdf).

## Funcionalidades do Sistema

* Cadastro, login e logout de usuários, com senha protegida por hash.
* Conteúdo educativo sobre os tipos de violência (física, psicológica, moral, patrimonial, sexual e digital), suas consequências e recursos para reflexão.
* Quiz sobre os tipos de violência, com correção das respostas e classificação do usuário por nível de conhecimento.
* Simulador de situações do cotidiano, com resultado personalizado de acordo com a postura do usuário.
* Manifesto de compromisso, com confirmação da assinatura e contador de assinaturas.
* Quiz, simulador e manifesto exigem usuário autenticado.

## Estrutura do Projeto

O código segue uma arquitetura em camadas:

* `app/controllers`: rotas da aplicação (Flask Blueprints).
* `app/services`: regras de negócio (autenticação, quiz, simulador e manifesto).
* `app/repositories`: acesso ao banco de dados.
* `app/models`: tabelas do banco (SQLAlchemy).
* `app/strategies`: padrão Strategy, usado na classificação dos níveis do quiz.
* `app/states` e `app/context`: padrão State, usado nas posturas do simulador (ativa, reflexiva e omissa).
* `app/decorators`: controle de acesso com `login_required`.
* `app/templates` e `app/static`: páginas HTML e estilos.
* `migrations`: migrações do banco de dados.
* `run.py`: ponto de entrada da aplicação.

## Requisitos

* Python 3.10 ou superior
* Banco de dados PostgreSQL
* Bibliotecas listadas em `requirements.txt` (Flask, Flask-SQLAlchemy, Flask-Migrate, psycopg2, entre outras)

## Como Rodar

1. Clone o repositório:

```
git clone <URL_DO_REPOSITORIO>
cd projeto-rompa
```

2. Crie e ative um ambiente virtual:

```
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto:

```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
SECRET_KEY=uma-chave-secreta-qualquer
```

5. Crie as tabelas com as migrações:

```
flask --app run db upgrade
```

6. Inicie a aplicação e acesse `http://localhost:5000`:

```
python run.py
```

## Solução de Problemas Comuns

* **A aplicação não inicia e reclama da URI do banco:** a variável `DATABASE_URL` não foi encontrada. Confira se o `.env` está na raiz do projeto, ao lado do `run.py`.
* **Erro de sessão dizendo que não há chave secreta:** falta a variável `SECRET_KEY` no `.env`. Adicione-a e reinicie a aplicação.
* **Erro dizendo que uma tabela (por exemplo, `usuarios`) não existe:** as migrações não foram aplicadas. Rode `flask --app run db upgrade`.
* **Quiz ou simulador sem perguntas ou cenários:** as migrações criam só a estrutura das tabelas. As perguntas (`perguntas_quiz`) e os cenários e opções do simulador (`cenarios_simulador` e `opcoes_simulador`) ficam no banco e precisam estar cadastrados.
* **Tela de login ao abrir quiz, simulador ou manifesto:** é o comportamento esperado, pois essas funcionalidades exigem login. Entre na conta e acesse novamente.
* **Mensagem "Usuário já existe" no cadastro:** já há uma conta com esse nome de usuário. Escolha outro ou faça login.

## Observações

* Projeto desenvolvido para a disciplina de Engenharia de Software I.
* Equipe: Thais Carvalho, Matheus Neri, Gustavo Poncell, Vicente Cordeiro e Luiz Felipe Evangelista.
