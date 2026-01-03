"""
LangChain Chains - HFC Agent (OpenRouter)
"""

from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from configure import Config
from src.data.sheets_client import GoogleSheetsClient
from src.data.models import RestaurantData
from src.llm.prompts import HFCPrompts


class HFCAgent:
    """Main HFC AI Agent using LangChain + OpenRouter"""
    
    def __init__(self):
        self.data: Optional[RestaurantData] = None
        self.chain = None
        self.llm = None
        
        # Load data first
        self._load_data()
        
        # Setup LLM
        self._setup_llm()
    
    def _load_data(self):
        """Load restaurant data from Google Sheets"""
        try:
            client = GoogleSheetsClient()
            raw_data = client.get_all_data()
            self.data = RestaurantData(raw_data)
            print("Restaurant data loaded")
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            self.data = None
    
    def _setup_llm(self):
        """Setup LangChain with OpenRouter"""
        try:
            api_key = Config.OPENROUTER_API_KEY
            
            if not api_key or api_key == "your_key_here" or api_key == "":
                print("No OpenRouter API key - using fallback mode")
                self.llm = None
                self.chain = None
                return
            
            # OpenRouter LLM using ChatOpenAI
            self.llm = ChatOpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key,
                model=Config.LLM_MODEL,
                temperature=Config.LLM_TEMPERATURE,
                max_tokens=Config.LLM_MAX_TOKENS
            )
            
            # Create chain: Prompt -> LLM -> Output Parser
            prompt = HFCPrompts.get_chat_prompt()
            self.chain = prompt | self.llm | StrOutputParser()
            
            print(" LangChain + OpenRouter initialized")
            
        except Exception as e:
            print(f"LLM setup error: {e}")
            self.llm = None
            self.chain = None
    
    def refresh_data(self):
        """Refresh data from Google Sheets"""
        self._load_data()
        return self.data is not None
    
    def process_query(self, question: str) -> str:
        """Process user query and return response"""
        
        if not self.data:
            return "Sorry, I couldn't load restaurant data. Please try again."
        
        # Get context from data
        context = self.data.to_context()
        
        # Try LLM chain first
        if self.chain:
            try:
                response = self.chain.invoke({
                    "context": context,
                    "question": question
                })
                return response.strip()
            except Exception as e:
                print(f" LLM error: {e}")
                return self._fallback_response(question)
        else:
            # No LLM, use fallback
            return self._fallback_response(question)
    
    def _fallback_response(self, question: str) -> str:
        """Smart fallback when LLM not available"""
        q = question.lower()
        
        # Timing questions
        if any(w in q for w in ["open", "close", "time", "hour", "when"]):
            status = self.data.is_open_now()
            if status["is_open"]:
                return f" Yes! We're currently OPEN.\n\n📍 Today ({status['day']}): {status['opens']} - {status['closes']}\n\nWelcome to Fast Food Restaurant! 🍔"
            else:
                return f" Sorry, we're currently CLOSED.\n\n📍 Today ({status['day']}): {status['opens']} - {status['closes']}\n\nSee you soon! 🍔"
        
        # Location questions
        if any(w in q for w in ["where", "location", "address", "phone", "contact"]):
            info = self.data.info
            return f"📍 **{info.get('Name', 'HFC')}**\n\nAddress: {info.get('Address', 'N/A')}\nPhone: {info.get('Phone', 'N/A')}\n\n100% Halal Certified ☪️"
        
        # Menu questions
        if any(w in q for w in ["menu", "food", "eat", "price", "chicken", "burger"]):
            cats = self.data.get_categories()
            if cats:
                return f"🍔 **Our Menu Categories:**\n\n" + "\n".join([f"• {c}" for c in cats]) + "\n\nAsk about any category!"
            return "We have delicious fried chicken, burgers, sides and drinks! 🍔"
        
        # Recommendations
        if any(w in q for w in ["recommend", "suggest", "best", "popular", "favorite"]):
            best = self.data.get_bestsellers()
            if best:
                res = "⭐ **Our Bestsellers:**\n\n"
                for item in best[:5]:
                    res += f"• {item.get('Item_Name', '')} - ${item.get('Regular_Price', '')}\n"
                return res + "\nCustomer favorites! 🍔"
            return "Try our signature fried chicken - it's amazing! 🍔"
        
        # Default welcome
        info = self.data.info
        return f"Welcome to **{info.get('Name', 'HFC')}**! 🍔\n\n100% Halal Certified ☪️\nRating: {info.get('Rating', 'N/A')} ⭐\n\nAsk me about menu, hours, or location!"
    
    def get_status(self) -> dict:
        """Get quick status for UI"""
        if not self.data:
            return {"is_open": False, "name": "HFC"}
        
        status = self.data.is_open_now()
        return {
            "name": self.data.info.get("Name", "HFC"),
            "is_open": status["is_open"],
            "time": status["time"],
            "rating": self.data.info.get("Rating", "N/A")
        }