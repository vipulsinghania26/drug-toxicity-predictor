import joblib
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem

# Load model once when server starts
import os

# Build absolute path — works no matter where you run uvicorn from
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'model', 'best_model.pkl')
model = joblib.load(model_path)
def smiles_to_fingerprint(smiles: str):
    """Convert SMILES string to Morgan Fingerprint array"""
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
        return np.array(fp).reshape(1, -1)  # reshape for single prediction
    except:
        return None

def predict_toxicity(smiles: str):
    """Take SMILES string, return prediction and confidence"""
    fingerprint = smiles_to_fingerprint(smiles)
    
    if fingerprint is None:
        return {"error": "Invalid SMILES string — could not parse molecule"}
    
    prediction = model.predict(fingerprint)[0]
    probability = model.predict_proba(fingerprint)[0][1]
    
    return {
        "smiles": smiles,
        "toxic": bool(prediction),
        "confidence": round(float(probability) * 100, 2),
        "verdict": "⚠️ TOXIC" if prediction == 1 else "✅ NON-TOXIC"
    }