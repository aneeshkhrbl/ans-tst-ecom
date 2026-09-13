from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Mock database of clothing products
PRODUCTS = [
    {"id": 1, "name": "Classic Workout T-Shirt", "category": "Activewear", "description": "Medium size, 40-inch chest, 26-inch max length.", "price": 25.00, "stock": 150},
    {"id": 2, "name": "Performance Joggers", "category": "Activewear", "description": "Breathable running joggers with zip pockets.", "price": 40.00, "stock": 85},
    {"id": 3, "name": "Heavyweight Hoodie", "category": "Outerwear", "description": "Fleece-lined winter hoodie.", "price": 55.00, "stock": 40}
]

@app.get("/catalog", response_class=HTMLResponse)
def get_catalog():
    # Dynamically generate HTML for each product card
    items_html = ""
    for item in PRODUCTS:
        items_html += f"""
        <div class="card">
            <h3>{item['name']}</h3>
            <span class="category">{item['category']}</span>
            <p>{item['description']}</p>
            <div class="price">€{item['price']:.2f}</div>
            <button onclick="alert('Added {item['name']} to cart!')">Add to Cart</button>
        </div>
        """
    
    # Wrap the cards in the main page structure
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Catalog - Ans E-Commerce</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                padding: 40px;
            }}
            h1 {{ color: #0078D4; text-align: center; }}
            .grid-container {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                max-width: 1000px;
                margin: 20px auto;
            }}
            .card {{
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                text-align: center;
            }}
            .category {{
                font-size: 0.8em;
                color: #666;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            .price {{
                font-size: 1.2em;
                color: #0078D4;
                font-weight: bold;
                margin: 15px 0;
            }}
            button {{
                background: #0078D4;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
                font-weight: bold;
            }}
            button:hover {{ background: #005A9E; }}
            .back-link {{
                display: block;
                text-align: center;
                margin-top: 30px;
                color: #0078D4;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <h1>Shop Our Collection</h1>
        <div class="grid-container">
            {items_html}
        </div>
        <a href="/" class="back-link">← Back to Home</a>
    </body>
    </html>
    """
    return html_content

@app.get("/catalog/{item_id}")
def get_item(item_id: int):
    for item in PRODUCTS:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}