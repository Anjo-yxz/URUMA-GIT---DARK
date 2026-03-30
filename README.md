# 🔴⚫ URUMA GIT 🔴⚫

<p align="center">
<img width="250" height="300" alt="image" src="https://github.com/user-attachments/assets/cbb1a428-0893-4127-b420-9d2a21d5c4b7" />
</p>


# ⚠️ Aviso

Este projeto foi desenvolvido apenas para fins educacionais, com o objetivo de demonstrar o uso da ferramenta Playwright.

O autor não se responsabiliza por qualquer uso indevido do código. Utilize com consciência e responsabilidade.

# 🤖 URUMA BOT

O URUMA BOT é um buscador automatizado de variáveis públicas no GitHub.

Ele funciona da seguinte forma:

Você informa uma variável (ex: EMAIL_PASS, TOKEN, etc.)
O bot faz uma busca por essa variável em repositórios públicos
Os resultados encontrados são salvos automaticamente em:
/Database/UrumaGITHUB.txt
📁 Estrutura do Projeto
```
src/
│
├── Bot/
│   └── UrumaBot.py
│
├── Database/
│   └── UrumaGITHUB.txt
│
├── Full/
│   └── Logo.py
│
├── Token/
│   └── UserGit.txt
│
└── main.py
```

# ⚙️ Como Usar

<img width="1434" height="335" alt="image" src="https://github.com/user-attachments/assets/4d3b77d9-37e9-48fe-90c9-a6c3373546ee" />


Configure seu cookie do GitHub

Vá até o arquivo:

Token/UserGit.txt
Cole seu cookie bruto do GitHub

Execute o projeto

python main.py
Escolha o modo de busca

O sistema vai perguntar:

# Usar variáveis padrão?
Sim → usa variáveis já definidas no projeto
Não → você digita sua própria variável
Resultado
O bot irá buscar no GitHub

E salvar tudo em:

 Database/UrumaGITHUB.txt
 
# 💡 Objetivo

Este projeto foi criado para:

Aprender automação com Playwright
Entender como funcionam buscas automatizadas
Demonstrar riscos de exposição de variáveis públicas
🚀 Melhorias Futuras (ideias)
Filtro por tipo de arquivo (.env, .txt, etc)
Interface gráfica
Exportação em JSON/CSV
Sistema de proxy para evitar bloqueios
🧠 Observação

Se uma variável está pública no GitHub, isso é um problema de segurança do dono do repositório, não do projeto.
