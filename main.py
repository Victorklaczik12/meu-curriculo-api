from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware

import models
import schemas
import services
from database import engine, get_db

# Cria as tabelas no banco de dados SQLite (caso ainda não existam)
models.Base.metadata.create_all(bind=engine)

# 1. Inicializa o FastAPI com o título e descrição
app = FastAPI(
    title="Interactive Resume & Analytics API",
    description="API para portfólio interativo com registro de métricas e notificações assíncronas.",
    version="1.0.0"
)

# 2. Configuração do CORS logo após criar o 'app'
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite que qualquer site faça chamadas para a API
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Mapeia a pasta estática (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")


# ----------------------------------------------------
# ROTAS DE PÁGINA (FRONT-END)
# ----------------------------------------------------
@app.get("/", response_class=FileResponse)
def ler_index():
    """
    Serve o arquivo principal index.html na raiz do site.
    """
    return FileResponse("static/index.html")


# ----------------------------------------------------
# ROTAS DA API REST (BACK-END)
# ----------------------------------------------------

@app.post("/api/visita", response_model=schemas.VisitaResponse, status_code=status.HTTP_201_CREATED)
def registrar_visita(db: Session = Depends(get_db)):
    """
    Registra um novo acesso/visualização na página.
    """
    nova_visita = models.Visita()
    db.add(nova_visita)
    db.commit()
    db.refresh(nova_visita)
    return nova_visita


@app.post("/api/contacto", response_model=schemas.MensagemResponse, status_code=status.HTTP_201_CREATED)
def enviar_mensagem(
    dados: schemas.MensagemCreate, 
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Recebe os dados do formulário de contato, salva no banco
    e dispara o webhook de notificação em segundo plano.
    """
    nova_mensagem = models.Mensagem(
        nome=dados.nome,
        email=dados.email,
        mensagem=dados.mensagem
    )
    db.add(nova_mensagem)
    db.commit()
    db.refresh(nova_mensagem)

    # Agenda o disparo da notificação assíncrona (Background Task)
    background_tasks.add_task(
        services.enviar_notificacao_mensagem,
        nome=dados.nome,
        email=dados.email,
        mensagem=dados.mensagem
    )

    return nova_mensagem


@app.get("/api/analytics", response_model=schemas.AnalyticsResponse)
def obter_metricas(db: Session = Depends(get_db)):
    """
    Retorna o total consolidado de visitas e mensagens recebidas.
    """
    total_visitas = db.query(models.Visita).count()
    total_mensagens = db.query(models.Mensagem).count()
    
    return {
        "total_visitas": total_visitas,
        "total_mensagens": total_mensagens
    }


@app.get("/api/mensagens", response_model=List[schemas.MensagemResponse])
def listar_mensagens(db: Session = Depends(get_db)):
    """
    Rota auxiliar para listar todas as mensagens cadastradas no banco.
    """
    return db.query(models.Mensagem).all()