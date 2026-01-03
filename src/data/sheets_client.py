"""
Google Sheets Client - Fetch HFC Restaurant Data
"""

import pandas as pd
from typing import Dict, List, Optional
from configure import Config


class GoogleSheetsClient:
    """Fetch data from public Google Sheets"""
    
    def __init__(self):
        self.sheet_ids = Config.SHEET_IDS
        self.base_url = "https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"
    
    def _fetch_sheet(self, sheet_name: str) -> Optional[pd.DataFrame]:
        """Fetch single sheet as DataFrame"""
        sheet_id = self.sheet_ids.get(sheet_name)
        
        
        if not sheet_id:
            print(f" Sheet ID not found: {sheet_name}")
            return None
        
        try:
            url = self.base_url.format(sheet_id=sheet_id)
            df = pd.read_csv(url)
            return df
        except Exception as e:
            print(f" Error fetching {sheet_name}: {e}")
            return None
    
    def get_restaurant_info(self) -> Dict:
        """Get restaurant basic info"""
        df = self._fetch_sheet("restaurant_info")
        
        if df is None or df.empty:
            return {}
        
        info = {}
        for _, row in df.iterrows():
            field = str(row.iloc[0]).strip()
            value = str(row.iloc[1]).strip() if len(row) > 1 else ""
            
            if field and field.lower() != "field" and value != "nan":
                info[field] = value
        
        return info
    
    def get_timings(self) -> Dict:
        """Get opening/closing timings"""
        df = self._fetch_sheet("timings")
        
        if df is None or df.empty:
            return {"weekly": [], "meals": []}
        
        result = {"weekly": [], "meals": []}
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Dinner"]
        
        for _, row in df.iterrows():
            row_data = [str(cell).strip() for cell in row.tolist()]
            
            if not row_data[0] or row_data[0].lower() in ["day", "meal_type", "nan"]:
                continue
            
            if row_data[0] in days:
                result["weekly"].append({
                    "day": row_data[0],
                    "opens": row_data[1] if len(row_data) > 1 else "",
                    "closes": row_data[2] if len(row_data) > 2 else "",
                    "status": row_data[3] if len(row_data) > 3 else "Open"
                })
            elif row_data[0] in meals:
                result["meals"].append({
                    "meal_type": row_data[0],
                    "start_time": row_data[1] if len(row_data) > 1 else "",
                    "end_time": row_data[2] if len(row_data) > 2 else ""
                })
        
        return result
    
    def get_menu(self) -> List[Dict]:
        """Get full menu"""
        df = self._fetch_sheet("menu")
        
        if df is None or df.empty:
            return []
        
        menu = []
        columns = df.columns.tolist()
        
        for _, row in df.iterrows():
            item = {}
            for col in columns:
                value = row[col]
                value = "" if pd.isna(value) else str(value).strip()
                clean_col = col.strip().replace(" ", "_")
                item[clean_col] = value
            
            if item.get("Item_Name") or item.get("Item"):
                menu.append(item)
        
        return menu
    
    def get_extras(self) -> List[Dict]:
        """Get extras/facilities"""
        df = self._fetch_sheet("extras")
        
        if df is None or df.empty:
            return []
        
        extras = []
        columns = df.columns.tolist()
        
        for _, row in df.iterrows():
            item = {}
            for col in columns:
                value = row[col]
                value = "" if pd.isna(value) else str(value).strip()
                clean_col = col.strip().replace(" ", "_")
                item[clean_col] = value
            
            if item.get("Feature") or item.get("Category"):
                extras.append(item)
        
        return extras
    
    def get_all_data(self) -> Dict:
        """Fetch all data"""
        print("📡 Fetching data from Google Sheets...")
        
        data = {
            "restaurant_info": self.get_restaurant_info(),
            "timings": self.get_timings(),
            "menu": self.get_menu(),
            "extras": self.get_extras()
        }
        
        print(" Data fetched successfully!")
        # print(data)
        return data


# Test
if __name__ == "__main__":
    client = GoogleSheetsClient()
    data = client.get_all_data()
    print(f"Restaurant: {data['restaurant_info'].get('Name', 'N/A')}")
    print(f"Menu items: {len(data['menu'])}")