from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.model_utils import predict_toxicity

# Create FastAPI app instance
app = FastAPI(title="Drug Toxicity Predictor")

# Tell FastAPI where your HTML templates live
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the home page"""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": None
    })

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, smiles: str = Form(...)):
    """Receive SMILES from form, return prediction"""
    result = predict_toxicity(smiles)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result
    })

@app.get("/api/predict")
async def api_predict(smiles: str):
    """JSON API endpoint for developers"""
    return predict_toxicity(smiles)