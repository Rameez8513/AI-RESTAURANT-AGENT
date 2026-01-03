"""
HFC AI Assistant - Configuration
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Central Configuration"""
    
    # Project
    PROJECT_NAME = "HFC AI Assistant"
    VERSION = "1.0.0"
    
    # Paths
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / "data"
    CACHE_DIR = DATA_DIR / "cache"
    
    # Google Sheets IDs
    SHEET_IDS = {
        "restaurant_info": os.getenv("SHEET_ID_RESTAURANT_INFO"),
        "timings": os.getenv("SHEET_ID_TIMINGS"),
        "menu": os.getenv("SHEET_ID_MENU"),
        "extras": os.getenv("SHEET_ID_EXTRAS")
    }
    
    # LLM API Keys (from .env)
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
    
    # LLM Settings - Using OpenRouter
    LLM_MODEL = "tngtech/deepseek-r1t2-chimera:free"
    LLM_TEMPERATURE = 0.7
    LLM_MAX_TOKENS = 512
    
    # Cache
    CACHE_ENABLED = True
    CACHE_TTL = 300  # 5 minutes


class Colors:
    """Professional Grey Theme"""
    
    BG_PRIMARY = "#212121"
    BG_SECONDARY = "#2F2F2F"
    BG_TERTIARY = "#3A3A3A"
    BG_CHAT = "#1A1A1A"
    TEXT_PRIMARY = "#ECECEC"
    TEXT_SECONDARY = "#B4B4B4"
    TEXT_MUTED = "#8E8E8E"
    ACCENT = "#10A37F"
    ACCENT_HOVER = "#1ABC94"
    BORDER = "#4A4A4A"