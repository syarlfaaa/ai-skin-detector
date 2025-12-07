from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from templates.html_templates import get_home_page
from templates.knowledge_page import get_knowledge_page
from config import GRADIO_URL

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home():
    """Halaman utama dengan Login & Sign Up"""
    return get_home_page()

@router.get("/knowledge", response_class=HTMLResponse)
async def knowledge():
    """Halaman knowledge about skincare"""
    return get_knowledge_page(GRADIO_URL)