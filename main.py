from fastapi import FastAPI
import uuid, sqlite3
app = FastAPI()

conn = sqlite3.connect("secrets.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS messages (key text, text text)")

@app.get("/")
async def root():
    return {"message": "OK"}

@app.post("/create/")
async def create(text):
    secret_key = str(uuid.uuid4())
    cursor.execute("INSERT INTO messages(key,text) VALUES (?,?)",(secret_key,text))
    conn.commit()
    return secret_key

@app.get("/read/{secret_key}")
async def read(secret_key):
    cursor.execute("SELECT text FROM messages WHERE key = ?", (secret_key,))
    result = cursor.fetchone()
    if result:
        cursor.execute("DELETE FROM messages WHERE key = ?", (secret_key,))
        conn.commit()
        return {"ok":result[0]}
    else:
        return{'error':"Сообщение не найдено..."}