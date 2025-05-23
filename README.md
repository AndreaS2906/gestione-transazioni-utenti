# gestione-transazioni-utenti

API backend fatta con FastAPI per gestire le transazioni degli utenti.  
Usa MySQL come database, con SQLAlchemy e Alembic per la gestione del database e migrazioni.  
L’autenticazione è fatta con JWT e la sicurezza con passlib, bcrypt e pyjwt.

---

## requirements

fastapi  
uvicorn[standard]  
sqlalchemy  
alembic  
pydantic  
pymysql  
cryptography  
python-multipart  
passlib  
pyjwt  
bcrypt==3.2.2  
mysql-connector-python  

---

## API principali

### User

POST  
`/user/create/`  
Crea un utente nuovo  

GET  
`/user/get_all/`  
Prendi tutti gli utenti  

### Auth

POST  
`/user/login`  
Login utente  

### Transactions

POST  
`/transactions/add`  
Aggiungi transazione  

GET  
`/transactions/get`  
Prendi tutte le transazioni  

POST  
`/transactions/update`  
Aggiorna transazione  

DELETE  
`/transactions/delete`  
Elimina transazione  

---

## Come installare

1. Clona il repo  
`git clone https://github.com/andreasposito/gestione-transazioni-utenti.git`  

2. Vai nella cartella  
`cd gestione-transazioni-utenti`  

3. Crea un ambiente virtuale (consigliato)  
`python -m venv venv`  

4. Attiva l’ambiente virtuale  
- Windows: `venv\Scripts\activate`  
- macOS/Linux: `source venv/bin/activate`  

5. Installa le dipendenze  
`pip install -r requirements.txt`  

---

## Come far partire il progetto

Devi far partire sia il server FastAPI che il database MySQL.

### Avvia il database MySQL

- Se l’hai installato sul pc, assicurati che sia acceso  
- Se vuoi usare Docker, puoi creare un file `docker-compose.yml` con MySQL e lanciarlo con `docker-compose up -d`  

### Avvia il server FastAPI

`uvicorn main:app --reload`

(Se il file principale non si chiama `main.py` cambia `main` con il nome giusto)

---

## Note

- Assicurati di configurare le credenziali per il database nel progetto (user, password, host, nome db)  
- Se vuoi posso aiutarti a scrivere il `docker-compose.yml` o a configurare tutto meglio  

---

Se vuoi chiedimi pure, sono qui per aiutarti!
