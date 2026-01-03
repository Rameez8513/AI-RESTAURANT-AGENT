"""
Data Models - Format data for LLM context
"""

from datetime import datetime
from typing import Dict, List


class RestaurantData:
    """Restaurant data processor"""
    
    def __init__(self, data: Dict):
        self.raw = data
        self.info = data.get("restaurant_info", {})
        self.timings = data.get("timings", {})
        self.menu = data.get("menu", [])
        self.extras = data.get("extras", [])
    
    def is_open_now(self) -> Dict:
        """Check if currently open"""
        now = datetime.now()
        day = now.strftime("%A")
        time = now.strftime("%I:%M %p")
        
        for t in self.timings.get("weekly", []):
            if t.get("day") == day:
                return {
                    "is_open": t.get("status", "").lower() == "open",
                    "day": day,
                    "time": time,
                    "opens": t.get("opens", ""),
                    "closes": t.get("closes", "")
                }
        
        return {"is_open": False, "day": day, "time": time}
    
    def get_categories(self) -> List[str]:
        """Get menu categories"""
        cats = set()
        for item in self.menu:
            cat = item.get("Category", "")
            if cat:
                cats.add(cat)
        return sorted(list(cats))
    
    def get_menu_by_category(self, category: str) -> List[Dict]:
        """Filter menu by category"""
        return [
            item for item in self.menu
            if item.get("Category", "").lower() == category.lower()
        ]
    
    def get_bestsellers(self) -> List[Dict]:
        """Get bestseller items"""
        return [
            item for item in self.menu
            if item.get("Is_Bestseller", "").lower() == "yes"
        ]
    
    def search_menu(self, query: str) -> List[Dict]:
        """Search menu"""
        query = query.lower()
        return [
            item for item in self.menu
            if query in item.get("Item_Name", "").lower()
            or query in item.get("Description", "").lower()
        ]
    
    def to_context(self) -> str:
        """Format as LLM context"""
        status = self.is_open_now()
        
        ctx = f"""
=== HFC - HALAL FRIED CHICKEN ===

📍 RESTAURANT INFO:
Name: {self.info.get('Name', 'HFC')}
Address: {self.info.get('Address', 'N/A')}
Phone: {self.info.get('Phone', 'N/A')}
Rating: {self.info.get('Rating', 'N/A')} ⭐
Halal Certified: Yes ☪️

🕐 CURRENT STATUS:
Day: {status['day']}
Time: {status['time']}
Status: {'🟢 OPEN' if status['is_open'] else '🔴 CLOSED'}
Hours: {status.get('opens', '')} - {status.get('closes', '')}

📅 WEEKLY HOURS:
"""
        for t in self.timings.get("weekly", []):
            icon = "🟢" if t.get("status", "").lower() == "open" else "🔴"
            ctx += f"  {t['day']}: {t['opens']} - {t['closes']} {icon}\n"
        
        ctx += "\n🍽️ MEAL TIMES:\n"
        for m in self.timings.get("meals", []):
            ctx += f"  {m['meal_type']}: {m['start_time']} - {m['end_time']}\n"
        
        ctx += "\n📋 MENU:\n"
        
        # Group by category
        categories = {}
        for item in self.menu:
            cat = item.get("Category", "Other")
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(item)
        
        for cat, items in categories.items():
            ctx += f"\n【{cat.upper()}】\n"
            for item in items:
                name = item.get("Item_Name", "")
                price = item.get("Regular_Price", item.get("Price", ""))
                avail = "✅" if item.get("Available", "").lower() == "yes" else "❌"
                best = "⭐" if item.get("Is_Bestseller", "").lower() == "yes" else ""
                spicy = "🌶️" if item.get("Is_Spicy", "").lower() == "yes" else ""
                ctx += f"  • {name} - ${price} {best}{spicy} {avail}\n"
        
        ctx += "\n🏪 FACILITIES:\n"
        for e in self.extras:
            if e.get("Available", "").lower() == "yes":
                ctx += f"  ✓ {e.get('Feature', '')}\n"
        
        return ctx