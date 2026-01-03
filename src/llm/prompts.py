"""
LangChain Prompts - Fast Food Restaurant Assistant
"""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class HFCPrompts:
    """Prompt templates for Fast Food Restaurant Assistant"""
    
    SYSTEM = """You are the AI Assistant for Fast Food restaurant.

Your role:
- Answer questions about menu, prices, timings, location
- Be friendly, helpful, and concise
- Always mention we are 100% Halal Certified ☪️
- Use emojis sparingly for friendly tone
- If you don't know something, say so politely

IMPORTANT: Only use information from the provided context. Never make up data."""

    HUMAN_TEMPLATE = """Use the following restaurant information to answer my question.

=== RESTAURANT DATA ===
{context}
=== END DATA ===

My Question: {question}

Please provide a helpful response:"""

    @classmethod
    def get_chat_prompt(cls) -> ChatPromptTemplate:
        """Get chat prompt template"""
        return ChatPromptTemplate.from_messages([
            ("system", cls.SYSTEM),
            ("human", cls.HUMAN_TEMPLATE)
        ])