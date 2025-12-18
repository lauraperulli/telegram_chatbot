"""
Film&Series Bot - Configuration Module

Questo modulo centralizza tutte le impostazioni del bot.
Include i parametri per LLM, RAG, gestione della memoria e i workaround 
necessari per la compatibilità degli ambienti cloud (es. Railway).
"""

import sys
import os
from typing import List
from dotenv import load_dotenv

# ============================================
# CRITICAL: SQLite Workaround
# Necessario per sistemi con versioni datate di SQLite (es. Debian/Railway)
# ============================================
try:
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
    sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None
    print("[OK] SQLite workaround attivato (pysqlite3)")
except ImportError:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    print("[WARN] pysqlite3 non trovato, utilizzo sqlite3 di sistema")

# Carica variabili d'ambiente da file .env
load_dotenv()

class APIKeys:
    """Gestione centralizzata delle chiavi API e validazione delle credenziali."""
    def __init__(self):
        self.TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    def validate(self) -> bool:
        """Verifica la presenza delle chiavi obbligatorie."""
        missing = []
        if not self.TELEGRAM_BOT_TOKEN: missing.append("TELEGRAM_BOT_TOKEN")
        if not self.OPENAI_API_KEY: missing.append("OPENAI_API_KEY")
        
        if missing:
            print(f"[ERROR] Chiavi mancanti nel file .env: {', '.join(missing)}")
            return False
        return True

class AdminConfig:
    """Configurazione degli accessi amministrativi."""
    def __init__(self):
        ids_str = os.getenv("ADMIN_USER_IDS", "")
        self.ADMIN_USER_IDS = [int(i.strip()) for i in ids_str.split(",") if i.strip()]

class LLMConfig:
    """Parametri del modello di linguaggio (GPT)."""
    def __init__(self):
        self.MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
        self.TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))

class RAGConfig:
    """Configurazione del sistema di Retrieval-Augmented Generation."""
    def __init__(self):
        self.EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
        self.CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "800"))
        self.CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "100"))
        self.TOP_K = int(os.getenv("RAG_TOP_K", "8"))

class PathsConfig:
    """Gestione dei percorsi file per database e documenti."""
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.DATA_DIR = os.path.join(self.BASE_DIR, "data")
        self.DOCUMENTS_DIR = os.path.join(self.BASE_DIR, "documents")
        self.CHROMA_DIR = os.path.join(self.BASE_DIR, "chroma_db")
        self.MEMORY_DIR = os.path.join(self.BASE_DIR, "user_memories")

# Istanza globale delle configurazioni
api_keys = APIKeys()
admin_config = AdminConfig()
llm_config = LLMConfig()
rag_config = RAGConfig()
paths_config = PathsConfig()

def validate_config() -> bool:
    """Esegue il controllo di integrità del sistema all'avvio."""
    print("\n" + "="*50)
    print("[SYSTEM] VALIDAZIONE CONFIGURAZIONE FILM&SERIES BOT")
    print("="*50)

    if not api_keys.validate():
        return False

    if not admin_config.ADMIN_USER_IDS:
        print("[WARN] Nessun amministratore configurato.")

    # Creazione automatica directory necessarie
    for path in [paths_config.DATA_DIR, paths_config.DOCUMENTS_DIR, 
                 paths_config.CHROMA_DIR, paths_config.MEMORY_DIR]:
        os.makedirs(path, exist_ok=True)

    print(f"[OK] LLM Model: {llm_config.MODEL}")
    print(f"[OK] Environment: Ready\n")
    return True