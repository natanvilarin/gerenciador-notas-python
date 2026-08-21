# Gerenciador de Notas em Python


## Introdução

Este projeto consiste em um sistema simples de gerenciamento acadêmico desenvolvido em Python.

O programa calcula a média dos alunos, verifica se eles foram aprovados ou reprovados de acordo com uma média mínima e gera um relatório com os resultados.

O projeto foi desenvolvido como atividade acadêmica durante o curso de Análise e Desenvolvimento de Sistemas (ADS), com o objetivo de colocar em prática conceitos básicos de programação.


## Objetivo

O objetivo principal é desenvolver uma aplicação simples para organizar as notas de alunos e automatizar o cálculo da média e a verificação da situação acadêmica.

Além da funcionalidade, o projeto busca aplicar conceitos de organização e estruturação de código.


## Tecnologias utilizadas

- Python 3
- Listas e dicionários
- Funções
- Estruturas condicionais
- Docstrings
- Modularização
- Testes automatizados com unittest
- Git e GitHub


## Estrutura do projeto

```text
gerenciador-notas-python/
├── gerenciador_notas.py
├── test_notas.py
└── README.md
```
### `gerenciador_notas.py`

Arquivo principal da aplicação. Contém as funções responsáveis pelo cálculo das médias, verificação da aprovação, geração do relatório e execução do programa.

### `test_notas.py`

Arquivo responsável pelos testes automatizados das principais funções do sistema.

### `README.md`

Documentação do projeto, contendo informações sobre seu objetivo, tecnologias utilizadas, estrutura e execução.


## Como executar o sistema

É necessário ter o Python 3 instalado.

Abra o terminal na pasta do projeto e execute:

```bash
python gerenciador_notas.py
```

Em alguns sistemas, pode ser necessário utilizar:

```bash
python3 gerenciador_notas.py
```

## Como executar os testes

No terminal, execute:

```bash
python -m unittest test_notas.py
```

Ou:

```bash
python3 -m unittest test_notas.py
```

Se os testes forem executados corretamente, o terminal deverá indicar que os testes foram concluídos com sucesso.


## O que aprendi

Durante o desenvolvimento, pude aplicar na prática conceitos que estou aprendendo no curso de ADS, principalmente lógica de programação, funções, listas, dicionários e modularização.

Também tive contato com testes automatizados utilizando `unittest`, entendendo melhor a importância de verificar se as funções apresentam os resultados esperados.

Outro aprendizado foi perceber a importância de separar as responsabilidades do código e documentar o projeto, facilitando sua leitura e manutenção.


## Próximos passos

Pretendo continuar evoluindo o projeto conforme avanço na graduação, adicionando novas funcionalidades e aplicando outros conceitos de programação que forem sendo estudados.

---

Projeto desenvolvido para fins acadêmicos e de aprendizado.
