from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Tech Price Glitch backend is running"}

@app.post("/scan-tech")
def scan_tech():
    # This will be upgraded later
    return {
        "message": "Scan started. You will be notified if a glitch is found."
    }
