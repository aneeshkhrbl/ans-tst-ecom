from fastapi import FastAPI

app = FastAPI()

# Mock database of clothing products
PRODUCTS = [
    {"id": 1, "name": "Classic Workout T-Shirt", "category": "Activewear", "description": "Medium size, 40-inch chest, 26-inch max length.", "price": 25.00, "stock": 150},
    {"id": 2, "name": "Performance Joggers", "category": "Activewear", "description": "Breathable running joggers with zip pockets.", "price": 40.00, "stock": 85},
    {"id": 3, "name": "Heavyweight Hoodie", "category": "Outerwear", "description": "Fleece-lined winter hoodie.", "price": 55.00, "stock": 40}
]

@app.get("/catalog")
def get_catalog():
    return {"items": PRODUCTS, "total_count": len(PRODUCTS)}

@app.get("/catalog/{item_id}")
def get_item(item_id: int):
    for item in PRODUCTS:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}