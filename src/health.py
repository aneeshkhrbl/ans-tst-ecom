from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ans Activewear</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap" rel="stylesheet">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Poppins', sans-serif;
            }
            body {
                background: #0f172a;
                color: #fff;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                /* Dark overlay with dynamic strength and conditioning background image */
                background-image: linear-gradient(rgba(15, 23, 42, 0.75), rgba(15, 23, 42, 0.95)), url('https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&w=1920&q=80');
                background-size: cover;
                background-position: center;
            }
            .glass-panel {
                background: rgba(255, 255, 255, 0.03);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 24px;
                padding: 60px 40px;
                text-align: center;
                max-width: 650px;
                width: 90%;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            }
            h1 {
                font-size: 3.5rem;
                font-weight: 800;
                margin-bottom: 10px;
                background: linear-gradient(to right, #38bdf8, #818cf8);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-transform: uppercase;
                letter-spacing: 2px;
            }
            p {
                font-size: 1.1rem;
                color: #cbd5e1;
                margin-bottom: 40px;
                font-weight: 400;
                line-height: 1.6;
            }
            .nav-links {
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
            }
            .btn {
                padding: 15px 35px;
                font-size: 1rem;
                font-weight: 600;
                text-decoration: none;
                border-radius: 50px;
                transition: all 0.3s ease;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            .btn-primary {
                background: #38bdf8;
                color: #0f172a;
                box-shadow: 0 10px 20px -10px #38bdf8;
            }
            .btn-primary:hover {
                background: #0ea5e9;
                transform: translateY(-3px);
                box-shadow: 0 15px 25px -10px #38bdf8;
            }
            .btn-secondary {
                background: transparent;
                color: #fff;
                border: 2px solid rgba(255,255,255,0.2);
            }
            .btn-secondary:hover {
                background: rgba(255,255,255,0.1);
                border-color: #fff;
                transform: translateY(-3px);
            }
        </style>
    </head>
    <body>
        <div class="glass-panel">
            <h1>Ans Activewear</h1>
            <p>Premium strength and conditioning gear designed to move with you.</p>
            <div class="nav-links">
                <a href="/catalog" class="btn btn-primary">Shop the Catalog</a>
                <a href="/auth" class="btn btn-secondary">Login / Register</a>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content