# 🎬 Film & Series Bot: chatbot telegram con RAG & LangChain

# 🤝 Presentazione
Ciao, sono LAURA PERULLI | **BSc in "Statistics e Big Data"**.

Benvenuto nel repository di uno dei miei progetti: un assistente AI avanzato per Telegram, progettato per agire come un esperto critico del mondo cinematografico e delle serie TV.

---

# 🚀 Di cosa si tratta?

🤖 **Film & Series Bot** non è un semplice chatbot, ma è un ecosistema basato su **Large Language Models (LLM)** che integra diverse tecnologie all'avanguardia per offrire un'esperienza utente completa:

- 🧠 **RAG (Retrieval-Augmented Generation)**: Il bot consulta documenti locali (PDF/TXT) per fornire risposte precise basate su database proprietari, riducendo le allucinazioni del modello.
- 👁️ **Vision AI**: Grazie ai modelli multimodali, il bot è in grado di analizzare locandine, screenshot di scene o poster inviati dagli utenti.
- 🎙️ **Voice Processing**: Integrazione con OpenAI Whisper per la trascrizione automatica delle note vocali.
- 🔍 **Web Search**: Capacità di navigare in tempo reale (via Tavily) per recuperare news, date di uscita e recensioni aggiornate.
  
---

# 🎯 Obiettivi del progetto
1. **Analisi del Linguaggio Naturale**: Implementare un sistema di conversazione fluido che mantenga la memoria storica del dialogo.
2. **Data Indexing & Retrieval**: Creare una pipeline efficiente per trasformare documenti non strutturati in un database vettoriale (**ChromaDB**).
3. **Multimodalità**: Gestire input eterogenei (testo, audio, immagini) in un unico flusso logico.
4. **Professional Coding**: Strutturare un codice pronto per l'ambiente di produzione, con gestione sicura delle chiavi API e gestione degli errori.

---

# 📁 Struttura del Repository

L'architettura del progetto è organizzata in modo modulare per separare la logica di business dalla gestione dei dati:

* **File di Configurazione e Avvio:**
    * `main.py`: Entry point dell'applicazione che coordina i diversi moduli.
    * `config.py`: Gestione centralizzata di variabili d'ambiente, costanti e setup tecnico.
    * `prompts.py`: Ingegneria dei prompt e definizione della personalità del bot.
    * `requirements.txt`: Elenco delle dipendenze Python (LangChain, OpenAI, ecc.).
    * `.env.example`: Template per la configurazione sicura delle chiavi API.
    * `.gitignore`: Esclusione di file sensibili, cache e database locali.

* **Cartella `src/` (Core Logic):**
    * 📂 **`llm/`**: Moduli per le capacità multimodali (Trascrizione audio e Visione).
    * 📂 **`rag/`**: Motore di ricerca semantica (Processing documenti, Vector Store e Retrieval).
    * 📂 **`telegram/`**: Gestione dell'interfaccia utente (Handler dei messaggi, Setup e Sicurezza).
    * 📂 **`utils/`**: Utility di supporto (Logging, Memoria intelligente e Client API condivisi).


---

# 🛠️ Stack Tecnologico
- **Linguaggio**: Python 3.10+
- **Orchestrazione AI**: LangChain
- **Modelli**: OpenAI GPT-4o (Chat & Vision), Whisper (Audio)
- **Vector Database**: ChromaDB
- **Tools**: Tavily Search API, Python-Telegram-Bot

---

# ⚙️ Installazione
1. Clona il repository.
2. Crea un file `.env` basandoti su `.env.example`.
3. Installa le librerie:
   ```bash
   pip install -r requirements.txt
4. Avvia il bot
   ```bash
   python main.py
