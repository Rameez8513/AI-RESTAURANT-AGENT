"""
HFC AI Assistant - Chat Page
"""

import streamlit as st
from ui.components import Components
from src.llm.chains import HFCAgent


class ChatPage:
    """Chat Page Handler"""
    
    @staticmethod
    @st.cache_resource
    def get_agent():
        """Get cached agent (loads once)"""
        return HFCAgent()
    
    @staticmethod
    def initialize_session():
        """Initialize Session"""
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "show_welcome" not in st.session_state:
            st.session_state.show_welcome = True
        if "waiting_response" not in st.session_state:
            st.session_state.waiting_response = False
    
    @staticmethod
    def add_message(role: str, content: str):
        """Add Message"""
        st.session_state.messages.append({"role": role, "content": content})
    
    @staticmethod
    def get_response(question: str) -> str:
        """Get AI Response"""
        try:
            agent = ChatPage.get_agent()
            return agent.process_query(question)
        except Exception as e:
            return "Sorry, something went wrong. Please try again."
    
    @staticmethod
    def render():
        """Render Chat Page"""
        ChatPage.initialize_session()
        
        # Header
        Components.chat_header()
        
        # Chat Area
        if st.session_state.show_welcome and not st.session_state.messages:
            # Welcome Screen
            st.markdown(Components.welcome_screen(), unsafe_allow_html=True)
            st.markdown(Components.suggestion_cards(), unsafe_allow_html=True)
            
            # Quick Buttons
            cols = st.columns(4)
            suggestions = [
                "What's on the menu?",
                "Are you open now?",
                "Where are you located?",
                "What's popular?"
            ]
            
            for i, text in enumerate(suggestions):
                with cols[i]:
                    if st.button(text, key=f"sug_{i}", use_container_width=True):
                        ChatPage.add_message("user", text)
                        st.session_state.show_welcome = False
                        st.session_state.waiting_response = True
                        st.rerun()
        else:
            # Display Messages
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    st.markdown(Components.user_message(msg["content"]), unsafe_allow_html=True)
                else:
                    st.markdown(Components.assistant_message(msg["content"]), unsafe_allow_html=True)
            
            # Show Thinking if waiting
            if st.session_state.waiting_response:
                st.markdown(Components.thinking_indicator(), unsafe_allow_html=True)
                
                # Get last user message
                last_msg = st.session_state.messages[-1]["content"] if st.session_state.messages else ""
                
                # Get response
                response = ChatPage.get_response(last_msg)
                ChatPage.add_message("assistant", response)
                st.session_state.waiting_response = False
                st.rerun()
        
        # Spacing
        st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
        
        # Input Area
        with st.form(key="chat_form", clear_on_submit=True, border=False):
            col1, col2 = st.columns([7, 1])
            
            with col1:
                user_input = st.text_input(
                    "Message",
                    placeholder="Message HFC Assistant...",
                    label_visibility="collapsed",
                    key="user_input"
                )
            
            with col2:
                submitted = st.form_submit_button("➤", use_container_width=True)
            
            if submitted and user_input and user_input.strip():
                ChatPage.add_message("user", user_input.strip())
                st.session_state.show_welcome = False
                st.session_state.waiting_response = True
                st.rerun()
        
        # Footer
        Components.footer()