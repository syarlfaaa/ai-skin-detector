from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from routes import auth, pages
from config import GMAIL_USER, GRADIO_URL
import os

app = FastAPI()

# Create static directory if it doesn't exist
os.makedirs("static", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(pages.router)
app.include_router(auth.router)

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 AI SKIN DETECTOR - LOGIN SERVER")
    print("=" * 60)
    print(f"📧 Email: {GMAIL_USER}")
    print(f"🔗 Gradio: {GRADIO_URL}")
    print(f"📍 Server: http://localhost:8000")
    print("=" * 60)
    print("✅ Ready! Open your browser at: http://localhost:8000")
    print("=" * 60)
    uvicorn.run(app, host="0.0.0.0", port=8000)