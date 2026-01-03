"""
HFC AI Assistant - Professional Styles & CSS
"""


class Styles:
    """Professional CSS Styles - ChatGPT/Claude Inspired"""
    
    @staticmethod
    def get_main_css():
        """Main application CSS"""
        return """
        <style>
            /* Import Google Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
            
            /* Root Variables - Professional Grey Theme */
            :root {
                --bg-primary: #212121;
                --bg-secondary: #2F2F2F;
                --bg-tertiary: #3A3A3A;
                --bg-chat: #1A1A1A;
                --text-primary: #ECECEC;
                --text-secondary: #B4B4B4;
                --text-muted: #8E8E8E;
                --border-color: #4A4A4A;
                --accent: #10A37F;
                --accent-hover: #1ABC94;
                --user-msg-bg: #2F2F2F;
                --assistant-msg-bg: #212121;
            }
            
            /* Global Styles */
            .stApp {
                background: var(--bg-primary);
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            }
            
            /* Hide Streamlit Defaults */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            /* Header background */
            header[data-testid="stHeader"] {
                background: var(--bg-primary) !important;
            }
            
            /* Sidebar Toggle */
            [data-testid="collapsedControl"] {
                visibility: visible !important;
                display: flex !important;
                background: var(--bg-secondary) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 8px !important;
                position: fixed !important;
                left: 10px !important;
                top: 10px !important;
                z-index: 999999 !important;
                width: 36px !important;
                height: 36px !important;
                align-items: center !important;
                justify-content: center !important;
            }

            [data-testid="collapsedControl"] svg {
                fill: var(--text-secondary) !important;
                width: 18px !important;
                height: 18px !important;
            }
            
            [data-testid="collapsedControl"]:hover {
                background: var(--bg-tertiary) !important;
            }
            
            [data-testid="collapsedControl"]:hover svg {
                fill: var(--text-primary) !important;
            }
            
            /* Chat Header */
            .chat-header {
                background: linear-gradient(180deg, var(--bg-secondary) 0%, var(--bg-primary) 100%);
                padding: 1rem 1.5rem;
                border-bottom: 1px solid var(--border-color);
                display: flex;
                align-items: center;
                justify-content: space-between;
                position: sticky;
                top: 0;
                z-index: 100;
            }
            
            .chat-header-title {
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }
            
            .chat-header h1 {
                color: var(--text-primary);
                font-size: 1.25rem;
                font-weight: 600;
                margin: 0;
            }
            
            .chat-header-badge {
                background: linear-gradient(135deg, #10A37F 0%, #0D8A6A 100%);
                color: white;
                padding: 0.25rem 0.75rem;
                border-radius: 12px;
                font-size: 0.75rem;
                font-weight: 500;
            }
            
            /* ============================================ */
            /* PROFESSIONAL INPUT FIELD STYLING */
            /* ============================================ */
            
            /* Form container */
            [data-testid="stForm"] {
                background: var(--bg-secondary) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 12px !important;
                padding: 0.5rem 0.75rem !important;
            }
            
            /* Remove form border on focus */
            [data-testid="stForm"]:focus-within {
                border-color: var(--accent) !important;
            }
            
            /* ============================================ */
            /* REMOVE INNER INPUT BOX & RED BORDER */
            /* ============================================ */
            
            /* Remove ALL inner styling */
            .stTextInput,
            .stTextInput > div,
            .stTextInput > div > div {
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
                outline: none !important;
                padding: 0 !important;
            }
            
            /* Remove baseweb inner box */
            div[data-baseweb="input"],
            div[data-baseweb="base-input"] {
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
                outline: none !important;
            }
            
            /* Input field itself */
            .stTextInput > div > div > input {
                background: transparent !important;
                border: none !important;
                box-shadow: none !important;
                outline: none !important;
                color: var(--text-primary) !important;
                font-size: 0.95rem !important;
                padding: 0.6rem 0.5rem !important;
                caret-color: var(--accent) !important;
            }
            
            .stTextInput > div > div > input::placeholder {
                color: var(--text-muted) !important;
            }
            
            /* Remove ALL focus states - NO RED BORDER */
            .stTextInput > div > div > input:focus,
            .stTextInput > div > div:focus,
            .stTextInput > div > div:focus-within,
            .stTextInput:focus-within,
            div[data-baseweb="input"]:focus,
            div[data-baseweb="input"]:focus-within,
            div[data-baseweb="base-input"]:focus,
            div[data-baseweb="base-input"]:focus-within {
                border: none !important;
                box-shadow: none !important;
                outline: none !important;
            }
            
            /* Remove label space */
            .stTextInput > label {
                display: none !important;
            }
            
            /* ============================================ */
            /* END INPUT FIX */
            /* ============================================ */
            
            /* Send Button */
            .stFormSubmitButton > button {
                background: var(--accent) !important;
                color: white !important;
                border: none !important;
                border-radius: 8px !important;
                padding: 0.6rem 1rem !important;
                font-weight: 500 !important;
                font-size: 1rem !important;
                transition: all 0.2s ease !important;
                min-height: 42px !important;
            }
            
            .stFormSubmitButton > button:hover {
                background: var(--accent-hover) !important;
            }
            
            .stFormSubmitButton > button:focus {
                box-shadow: none !important;
                outline: none !important;
            }
            
            /* Regular buttons */
            .stButton > button {
                background: var(--bg-secondary) !important;
                color: var(--text-primary) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 8px !important;
                padding: 0.5rem 1rem !important;
                font-weight: 500 !important;
                font-size: 0.85rem !important;
                transition: all 0.2s ease !important;
            }
            
            .stButton > button:hover {
                background: var(--bg-tertiary) !important;
                border-color: var(--accent) !important;
            }
            
            .stButton > button:focus {
                box-shadow: none !important;
                outline: none !important;
            }
            
            /* ============================================ */
            /* MESSAGE STYLES */
            /* ============================================ */
            
            .user-message {
                background: var(--user-msg-bg);
                color: var(--text-primary);
                padding: 1rem 1.25rem;
                border-radius: 12px;
                margin: 0.5rem 0;
                max-width: 85%;
                margin-left: auto;
                font-size: 0.95rem;
                line-height: 1.6;
                border: 1px solid var(--border-color);
            }
            
            .assistant-message {
                background: transparent;
                color: var(--text-primary);
                padding: 1rem 0;
                margin: 0.5rem 0;
                font-size: 0.95rem;
                line-height: 1.7;
            }
            
            /* Sidebar Styling */
            [data-testid="stSidebar"] {
                background: var(--bg-secondary) !important;
                border-right: 1px solid var(--border-color);
            }
            
            [data-testid="stSidebar"] > div {
                background: var(--bg-secondary) !important;
            }
            
            [data-testid="stSidebar"] .stMarkdown,
            [data-testid="stSidebar"] p,
            [data-testid="stSidebar"] span,
            [data-testid="stSidebar"] label {
                color: var(--text-secondary) !important;
            }
            
            [data-testid="stSidebar"] h1,
            [data-testid="stSidebar"] h2,
            [data-testid="stSidebar"] h3 {
                color: var(--text-primary) !important;
            }
            
            /* Status Indicator */
            .status-dot {
                width: 8px;
                height: 8px;
                background: var(--accent);
                border-radius: 50%;
                display: inline-block;
                margin-right: 0.5rem;
                animation: pulse 2s infinite;
            }
            
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.5; }
            }
            
            /* Scrollbar */
            ::-webkit-scrollbar {
                width: 6px;
            }
            
            ::-webkit-scrollbar-track {
                background: var(--bg-primary);
            }
            
            ::-webkit-scrollbar-thumb {
                background: var(--bg-tertiary);
                border-radius: 3px;
            }
            
            ::-webkit-scrollbar-thumb:hover {
                background: var(--border-color);
            }
            
            /* Footer Text */
            .footer-text {
                text-align: center;
                color: var(--text-muted);
                font-size: 0.75rem;
                padding: 0.5rem;
            }
            
            /* Divider/HR styling */
            hr {
                border: none !important;
                border-top: 1px solid var(--border-color) !important;
                margin: 1rem 0 !important;
            }
            
            /* Hide form submit button text if needed */
            .stFormSubmitButton > button > div {
                display: flex;
                align-items: center;
                justify-content: center;
            }
        </style>
        """
    
    @staticmethod
    def get_sidebar_css():
        """Sidebar specific CSS - merged into main"""
        return ""
    
    @staticmethod
    def thinking_indicator():
     """Thinking indicator - Professional"""
     return """
        <div style="display: flex; align-items: flex-start; gap: 0.6rem; margin: 0.5rem 0; padding: 0.5rem 0;">
            <div style="width: 28px; height: 28px; min-width: 28px; 
                        background: linear-gradient(135deg, #10A37F 0%, #0D8A6A 100%); 
                        border-radius: 6px; display: flex; align-items: center; 
                        justify-content: center; font-size: 0.85rem;">🍗</div>
            <div style="display: flex; align-items: center; gap: 0.5rem; padding-top: 0.3rem;">
                <div class="thinking-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
        <style>
            .thinking-dots {
                display: flex;
                gap: 4px;
            }
            .thinking-dots span {
                width: 8px;
                height: 8px;
                background: #8E8E8E;
                border-radius: 50%;
                animation: thinking 1.4s infinite ease-in-out;
            }
            .thinking-dots span:nth-child(1) { animation-delay: 0s; }
            .thinking-dots span:nth-child(2) { animation-delay: 0.2s; }
            .thinking-dots span:nth-child(3) { animation-delay: 0.4s; }
            @keyframes thinking {
                0%, 80%, 100% { 
                    transform: scale(0.6);
                    opacity: 0.4;
                }
                40% { 
                    transform: scale(1);
                    opacity: 1;
                }
            }
        </style>
    """