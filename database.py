from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define que usaremos um banco SQLite local salvo no arquivo "curriculo.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///./curriculo.db"

# Cria o mecanismo de conexão com o banco
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria a fábrica de sessões para executar operações no banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base que os nossos modelos SQL irão herdar
Base = declarative_base()

# Função auxiliar para abrir e fechar a conexão com o banco de forma segura
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()