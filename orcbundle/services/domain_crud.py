

import json
import os
from typing import Any, Dict, List, Optional

from orcbundle.utils.general import get_project_root
from orcbundle.models.domain import Domain

class DomainCRUD:
    def __init__(self):
        self.dir_path = get_project_root() / "resources/domains"
        self._ensure_directory_exists()

    def _ensure_directory_exists(self) -> None:
        """Create the directory if it doesn't exist"""
        os.makedirs(self.dir_path, exist_ok=True)

    def create(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Create a new item as a JSON file"""
        
        item_id = item['name']
        file_path = os.path.join(self.dir_path, f"{item_id}.json")
        
        if os.path.exists(file_path):
            return None  # Item already exists
        
        with open(file_path, 'w') as f:
            json.dump(item, f, indent=4)
        return item
    
   

    def read_all(self) -> List[Dict[str, Any]]:
        """Read all items from the directory"""
        items = []
        for filename in os.listdir(self.dir_path):
            if filename.endswith('.json'):
                file_path = os.path.join(self.dir_path, filename)
                with open(file_path, 'r') as f:
                    try:
                        items.append(json.load(f))
                    except json.JSONDecodeError:
                        continue
        return items

    def read_all(self) -> List[Dict[str, Any]]:
        """Read all items from the directory"""
        items = []
        for filename in os.listdir(self.dir_path):
            if filename.endswith('.json'):
                file_path = os.path.join(self.dir_path, filename)
                with open(file_path, 'r') as f:
                    try:
                        items.append(json.load(f))
                    except json.JSONDecodeError:
                        continue
        return items

    def read_one(self, file_name: Any) -> Optional[Dict[str, Any]]:
        """Read a single item by ID"""
        file_path = os.path.join(self.dir_path, f"{file_name}.json")
        if not os.path.exists(file_path):
            return None
        with open(file_path, 'r') as f:
            return json.load(f)

    # def update(self, item_id: Any, update_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    #     """Update an existing item"""
    #     file_path = os.path.join(self.dir_path, f"{item_id}.json")
    #     if not os.path.exists(file_path):
    #         return None
        
    #     # Handle potential ID change
    #     new_id = update_data.get('id', item_id)
    #     new_path = os.path.join(self.dir_path, f"{new_id}.json")
        
    #     with open(file_path, 'r') as f:
    #         current_data = json.load(f)
        
    #     # Prevent ID conflict
    #     if new_id != item_id and os.path.exists(new_path):
    #         return None
        
    #     # Update data
    #     current_data.update(update_data)
    #     current_data['id'] = new_id  # Maintain ID consistency
        
    #     # Write changes
    #     if new_id != item_id:
    #         os.remove(file_path)
    #         file_path = new_path
            
    #     with open(file_path, 'w') as f:
    #         json.dump(current_data, f, indent=4)
            
    #     return current_data

    # def delete(self, item_id: Any) -> bool:
    #     """Delete an item by ID"""
    #     file_path = os.path.join(self.dir_path, f"{item_id}.json")
    #     if os.path.exists(file_path):
    #         os.remove(file_path)
    #         return True
    #     return False


domain_crud = DomainCRUD()