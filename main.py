"""
HFC AI Assistant - Main Entry Point
Professional Chat Interface
"""

import streamlit as st
from configure import Config
from ui.styles import Styles
from ui.components import Components
from ui.pages.chat import ChatPage


# Page Configuration
st.set_page_config(
    page_title="Restaurant AI Assistant",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="collapsed"
)


def apply_styles():
    """Apply all custom CSS"""
    st.markdown(Styles.get_main_css(), unsafe_allow_html=True)


def render_sidebar():
    """Render Professional Sidebar"""
    with st.sidebar:
        Components.sidebar_content()
        
        # New Chat Button
        if st.button("☪️ Halal Certified", key="new_chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.show_welcome = True
            st.rerun()
        
        st.markdown("---")
        
        # Info Section
        Components.sidebar_info()
        
        st.markdown("---")
        
        # About Section
        st.markdown("""
            <div style="padding: 0.5rem;">
                <p style="color: #8E8E8E; font-size: 0.75rem; margin-bottom: 0.5rem;">ABOUT</p>
                <p style="color: #B4B4B4; font-size: 0.8rem; line-height: 1.5;">
                    HFC AI Assistant helps you explore our halal menu.
                    </p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        

def main():
    """Main Application - Chat Only"""
    
    # Apply Styles
    apply_styles()
    
    # Render Sidebar
    render_sidebar()
    
    # Render Chat Page
    ChatPage.render()


if __name__ == "__main__":
    main()