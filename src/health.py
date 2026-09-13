from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home_page():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ans E-Commerce</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                text-align: center;
                padding-top: 100px;
            }
            .container {
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            h1 { color: #0078D4; }
            .btn {
                display: inline-block;
                margin: 15px 10px;
                padding: 12px 24px;
                text-decoration: none;
                background: #0078D4;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                transition: background 0.3s;
            }
            .btn:hover { background: #005A9E; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Ans E-Commerce</h1>
            <p>Your one-stop shop for premium activewear.</p>
            <div class="nav-links">
                <a href="/catalog" class="btn">Shop the Catalog</a>
                <a href="/auth" class="btn">Login / Register</a>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content