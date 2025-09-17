# 🍲 Projeto Django - Site de Receitas  

Este é um projeto desenvolvido com **Django** para prática de desenvolvimento web.  
O sistema é um **site de receitas**, onde usuários podem se cadastrar, enviar receitas e interagir com a comunidade.  
Há também uma área administrativa para aprovar e gerenciar as receitas.  

---

## 🚀 Funcionalidades  

- Cadastro e login de usuários  
- Cadastro de novas receitas (apenas para usuários autenticados)  
- Listagem de receitas disponíveis  
- Área administrativa para aprovação e gerenciamento de receitas  
- Banco de dados inicial em **SQLite**  

---

## 🛠️ Tecnologias utilizadas  

- [Python](https://www.python.org/)  
- [Django](https://www.djangoproject.com/)  
- Banco de dados: **SQLite**  
- HTML, CSS e Django Templates  

---

## 📂 Estrutura do projeto  

```bash
meu_projeto_receitas/
│
├── app/              # App de autenticação
│   ├── settings.py
│   ├── urls.py
│
│
├── recipes/              
│   ├── models.py         
│   ├── views.py          
│   ├── urls.py           
│   └── templates/        
│
├── manage.py
├── db.sqlite3            
└── requirements.txt      
└── README.md             
