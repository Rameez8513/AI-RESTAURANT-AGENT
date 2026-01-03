"""
HFC AI Assistant - Professional UI Components
"""

import streamlit as st
from datetime import datetime


class Components:
    """Professional UI Components - ChatGPT/Claude Inspired"""
    
    @staticmethod
    def chat_header():
        """Minimal Chat Header"""
        st.markdown("""
            <div class="chat-header">
                <div class="chat-header-title">
                    <h1>🍔 Fast Food Assistant</h1>
                    <span class="chat-header-badge">☪️ Halal Certified</span>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span class="status-dot"></span>
                    <span style="color: var(--text-secondary); font-size: 0.85rem;">Online</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def welcome_screen():
        """Welcome Screen - Compact"""
        return """
            <div style="text-align: center; padding: 1rem 0;">
                <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #10A37F 0%, #0D8A6A 100%); 
                            border-radius: 10px; display: inline-flex; align-items: center; justify-content: center; 
                            font-size: 1.5rem; margin-bottom: 0.75rem;">🍔</div>
                <h1 style="color: #ECECEC; font-size: 1.4rem; font-weight: 600; margin: 0 0 0.3rem;">Fast Food Assistant</h1>
                <p style="color: #B4B4B4; font-size: 0.9rem; margin: 0;">Ask about menu, hours, locations, and more.</p>
            </div>
        """
    
    @staticmethod
    def suggestion_cards():
        """Suggestion Cards - Inline Width"""
        return """
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; padding: 0.75rem 0;">
                <div class="suggestion-chip">📋 View Menu</div>
                <div class="suggestion-chip">🕐 Opening Hours</div>
                <div class="suggestion-chip">📍 Find Location</div>
                <div class="suggestion-chip">⭐ Top Picks</div>
            </div>
            <style>
                .suggestion-chip {
                    background: #2F2F2F;
                    border: 1px solid #4A4A4A;
                    border-radius: 20px;
                    padding: 0.5rem 1rem;
                    color: #B4B4B4;
                    font-size: 0.85rem;
                    cursor: pointer;
                    transition: all 0.2s;
                    display: inline-block;
                }
                .suggestion-chip:hover {
                    background: #3A3A3A;
                    border-color: #10A37F;
                    color: #ECECEC;
                }
            </style>
        """
    
    @staticmethod
    def user_message(message: str):
        """User Message - Fits Text Width"""
        return f'''
            <div style="display: flex; justify-content: flex-end; margin: 0.4rem 0;">
                <div style="background: #2F2F2F; border: 1px solid #4A4A4A; color: #ECECEC; 
                            padding: 0.6rem 1rem; border-radius: 18px 18px 4px 18px; 
                            font-size: 0.9rem; line-height: 1.5; display: inline-block; max-width: 80%;">{message}</div>
            </div>
        '''
    
    @staticmethod
    def assistant_message(message: str):
        """Assistant Message - Fits Text Width"""
        return f"""
            <div style="display: flex; align-items: flex-start; gap: 0.6rem; margin: 0.4rem 0;">
                <div style="width: 26px; height: 26px; min-width: 26px; background: linear-gradient(135deg, #10A37F 0%, #0D8A6A 100%); 
                            border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 0.8rem;">🍔</div>
                <div style="color: #ECECEC; font-size: 0.9rem; line-height: 1.6; display: inline-block;">{message}</div>
            </div>
        """
    
    @staticmethod
    def thinking_indicator():
        """Thinking Indicator - With Avatar"""
        return """
            <div style="display: flex; align-items: flex-start; gap: 0.6rem; margin: 0.4rem 0;">
                <div style="width: 26px; height: 26px; min-width: 26px; 
                            background: linear-gradient(135deg, #10A37F 0%, #0D8A6A 100%); 
                            border-radius: 6px; display: flex; align-items: center; 
                            justify-content: center; font-size: 0.8rem;">🍔</div>
                <div style="display: flex; align-items: center; gap: 0.4rem; padding-top: 0.2rem;">
                    <span style="color: #B4B4B4; font-size: 0.9rem;">Thinking</span>
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
                    align-items: center;
                    gap: 3px;
                    margin-left: 2px;
                }
                .thinking-dots span {
                    width: 6px;
                    height: 6px;
                    background: #B4B4B4;
                    border-radius: 50%;
                    animation: bounce 1.4s infinite ease-in-out;
                }
                .thinking-dots span:nth-child(1) { animation-delay: 0s; }
                .thinking-dots span:nth-child(2) { animation-delay: 0.2s; }
                .thinking-dots span:nth-child(3) { animation-delay: 0.4s; }
                @keyframes bounce {
                    0%, 80%, 100% { 
                        transform: translateY(0);
                        opacity: 0.4;
                    }
                    40% { 
                        transform: translateY(-5px);
                        opacity: 1;
                    }
                }
            </style>
        """
    
    @staticmethod
    def quick_actions():
        """Quick Action Buttons Data"""
        return [
            ("🕐", "Hours"),
            ("📍", "Location"),
            ("📋", "Menu"),
            ("⭐", "Popular"),
            ("📞", "Contact")
        ]
    
    @staticmethod
    def sidebar_content():
        """Sidebar Content - Professional"""
        st.markdown("""
            <div style="padding: 0.5rem;">
                <div style="display: flex; align-items: center; gap: 0.75rem; 
                            padding: 0.75rem; margin-bottom: 1rem;">
                    <div style="width: 32px; height: 32px; 
                                background: linear-gradient(135deg, #10A37F 0%, #0D8A6A 100%);
                                border-radius: 8px; display: flex; align-items: center; 
                                justify-content: center; font-size: 1rem;">🍔</div>
                    <span style="color: #ECECEC; font-weight: 600; font-size: 1rem;">Fast Food Assistant</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def sidebar_info():
        """Sidebar Info Section"""
        current_time = datetime.now().strftime("%I:%M %p")
        st.markdown(f"""
            <div style="background: #3A3A3A; border-radius: 8px; padding: 1rem; margin: 1rem 0;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.75rem;">
                    <span style="color: #8E8E8E; font-size: 0.8rem;">Status</span>
                    <span style="color: #10A37F; font-size: 0.8rem;">● Online</span>
                </div>
                <div style="display: flex; justify-content: space-between;">
                    <span style="color: #8E8E8E; font-size: 0.8rem;">Time</span>
                    <span style="color: #ECECEC; font-size: 0.8rem;">{current_time}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def footer():
        """Footer Text"""
        st.markdown("""
            <div style="text-align: center; color: #8E8E8E; font-size: 0.7rem; padding: 0.5rem; margin-top: 0.5rem;">
                HFC Assistant can make mistakes. Verify important information.
            </div>
        """, unsafe_allow_html=True)