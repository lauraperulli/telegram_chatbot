"""
FILM&SERIES BOT - Main Entry Point

Questo è il file principale per l'avvio del bot Telegram.
Gestisce l'inizializzazione dei componenti RAG, la logica degli agenti 
e la connessione ai server Telegram.
"""

import sys
import GITHUB.config as config
from src.utils.logger import main_logger

# Validazione configurazione prima dell'avvio dei componenti core
if not config.validate_config():
    main_logger.error("Inizializzazione fallita: Controllare le variabili d'ambiente (.env)")
    sys.exit(1)

from bot_engine import LangChainEngine
from src.rag.vector_store import VectorStoreManager
from src.rag.document_processor import DocumentProcessor
from src.telegram.bot_setup import create_bot
from src.telegram.message_processor import MessageProcessor
from src.telegram.handlers import setup_handlers

def start_application():
    """Inizializza e avvia l'ecosistema Film&Series Bot."""
    main_logger.info("Inizializzazione componenti Core...")

    try:
        # Setup Vector DB (ChromaDB)
        vector_store = VectorStoreManager(
            persist_directory=config.paths_config.CHROMA_DIR,
            embedding_model=config.rag_config.EMBEDDING_MODEL
        )

        # Setup Document Processor per RAG
        doc_processor = DocumentProcessor(vector_store=vector_store)

        # Inizializzazione AI Engine (LangChain)
        langchain_engine = LangChainEngine(vector_store=vector_store)

        # Setup Message Processor (Logica di risposta)
        msg_processor = MessageProcessor(langchain_engine=langchain_engine)

        # Creazione istanza Bot Telegram
        app = create_bot(token=config.api_keys.TELEGRAM_BOT_TOKEN)

        # Configurazione degli Handler (Comandi e Messaggi)
        setup_handlers(
            app=app,
            langchain_engine=langchain_engine,
            vector_store=vector_store,
            document_processor=doc_processor,
            message_processor=msg_processor
        )

        main_logger.info("="*60)
        main_logger.info("FILM&SERIES BOT - SISTEMA ATTIVO")
        main_logger.info("="*60)
        
        # Avvio in modalità Polling
        app.run_polling(allowed_updates=['message', 'callback_query'])

    except Exception as e:
        main_logger.error(f"Errore critico durante l'esecuzione: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    start_application()