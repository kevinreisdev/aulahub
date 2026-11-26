# Backend Journey: Plataforma de Cursos Online

Uma plataforma de cursos online onde professores publicam cursos com aulas, alunos se matriculam e administradores gerenciam o sistema.

Este repositório registra minha jornada de estudos em backend. Em vez de seguir um tutorial pronto, estou construindo o sistema do zero, uma etapa por vez, primeiro modelar o domínio e escrever os testes, depois expor tudo em uma API, conectar um banco de dados e colocar em produção. Cada commit representa um passo dessa evolução.

Fase atual: **camada de domínio** (classes, validações e testes). A API ainda não foi implementada.

---

## Tecnologias utilizadas

- Python
- bcrypt (hash de senhas)
- pytest (testes automatizados)

---

## Funcionalidades

- Cadastro de usuários com validação de nome, sobrenome, e-mail e senha
- Senha armazenada como hash (bcrypt), nunca em texto puro
- Verificação de senha com `check_password`
- Perfis de usuário: aluno, professor e administrador
- Criação de cursos com validação do título
- Criação de aulas com validação de título, link do vídeo, posição e duração
- Matrícula de alunos em cursos com controle de status 
- Testes automatizados para todas as entidades

---

## Entidades

| Entidade   | Descrição                                              |
| ---------- | ------------------------------------------------------ |
| User       | Classe base com os dados e validações de todo usuário  |
| Student    | Aluno, herda de User                                   |
| Teacher    | Professor, herda de User e tem uma bio opcional        |
| Course     | Curso criado por um professor                          |
| Lesson     | Aula que pertence a um curso                           |
| Enrollment | Matrícula de um aluno em um curso                      |

Relacionamentos:

- Professor 1 ── N Cursos
- Curso 1 ── N Aulas
- Aluno N ── N Cursos (por meio da Matrícula)

A modelagem completa, com atributos, regras de validação e permissões, está em [data_model.md](data_model.md).

---

## Estrutura do projeto

```
backend_journey/
├── models/          # Entidades e regras de negócio
├── tests/           # Testes automatizados (pytest)
├── data_model.md    # Modelagem de dados
└── requirements.txt
```

---

## Como executar

```bash
# Criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt

# Rodar os testes
pytest
```

---

## Próximos passos

- API REST com FastAPI
- Banco de dados PostgreSQL
- Autenticação com JWT
- Docker
- CI com GitHub Actions
- Deploy
