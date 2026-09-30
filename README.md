# 🚀 Interactive Resume & Analytics API

Uma aplicação completa que combina um portfólio interativo no frontend com um backend em FastAPI para registo de métricas de acesso em tempo real e processamento de contactos.

---

## 🛠️ Tecnologias Utilizadas

### **Backend**
* **[FastAPI](https://fastapi.tiangolo.com/):** Framework moderno e de alta performance para construção da API.
* **[SQLAlchemy](https://www.sqlalchemy.org/):** ORM para gestão do banco de dados relacional.
* **[SQLite](https://www.sqlite.org/):** Banco de dados leve para persistência das visitas e mensagens.
* **[Pydantic](https://docs.pydantic.dev/):** Validação de dados e esquemas de entrada/saída.
* **Background Tasks:** Execução de tarefas em segundo plano para envio assíncrono de notificações.

### **Frontend & Infraestrutura**
* **Frontend:** HTML5, CSS3 e JavaScript assíncrono (`Fetch API`).
* **Deploy:** [Render](https://render.com/) (Web Service com integração contínua via GitHub).
* **Documentação:** Swagger UI integrada e gerada automaticamente pelo FastAPI.

---

## 🎯 Funcionalidades

1. **Rastreio de Métricas:** Registo automático de visitas e contagem de mensagens recebidas.
2. **Formulário de Contacto:** Envio de dados assíncrono com persistência no banco de dados.
3. **Analytics API:** Rota dedicada (`/api/analytics`) para disponibilizar dados estatísticos ao frontend.
4. **Documentação Interativa:** Interface Swagger disponível para teste de todos os endpoints.

---

## 📌 Rotas da API

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/` | Serve a página principal do currículo (`index.html`). |
| `POST` | `/api/visita` | Regista uma nova visualização na página. |
| `POST` | `/api/contacto` | Recebe e salva uma mensagem do formulário de contacto. |
| `GET` | `/api/analytics` | Retorna o total consolidado de visitas e mensagens. |
| `GET` | `/api/mensagens` | Lista todas as mensagens recebidas no banco de dados. |
| `GET` | `/docs` | Documentação interativa em Swagger UI. |

---

## 💻 Como Executar o Projeto Localmente

### **Pré-requisitos**
* Python 3.10+ instalado
* Git instalado

### **Passo a Passo**

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/Victorklaczik12/meu-curriculo-api.git](https://github.com/Victorklaczik12/meu-curriculo-api.git)
   cd meu-curriculo-api