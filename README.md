Drug Toxicity Predictor
An end-to-end machine learning web application that predicts the toxicity of drug compounds from molecular SMILES strings using Morgan Fingerprints and a Random Forest classifier — deployed live with FastAPI.
🔗 Live Demo: drug-toxicity-predictor.onrender.com

Overview
Drug toxicity screening is a critical and expensive step in pharmaceutical development. This project automates toxicity prediction for the NR-AR (Androgen Receptor) target from the NIH Tox21 dataset — the same benchmark used by researchers at the US National Institutes of Health.
Given a SMILES string (a text representation of a molecule), the app:

Parses the molecular structure using RDKit
Converts it into a 2048-bit Morgan Fingerprint
Predicts toxicity using a trained Random Forest model
Returns the verdict and confidence score via a clean web interface


Demo
InputPredictionCC(=O)Oc1ccccc1C(=O)O (Aspirin)Non-Toxicc1ccccc1 (Benzene) ToxicCCO (Ethanol) Non-Toxic

Project Architecture
drug-toxicity-predictor/
├── app/
│   ├── main.py              ← FastAPI backend (routes & endpoints)
│   ├── model_utils.py       ← SMILES → Fingerprint → Prediction pipeline
│   └── templates/
│       └── index.html       ← Frontend (TailwindCSS)
├── model/
│   └── best_model.pkl       ← Trained Random Forest model
├── notebooks/
│   └── drug_detector.ipynb  ← EDA, feature engineering & modeling
├── Procfile                 ← Render deployment config
├── requirements.txt
└── README.md

How It Works
1. Feature Engineering — Morgan Fingerprints
Raw SMILES strings (e.g. CCO) are converted into 2048-bit Morgan Fingerprints using RDKit. Each bit encodes whether a specific molecular substructure exists within a radius of 2 bonds from each atom. This is the industry-standard featurization method used in cheminformatics.
pythonfrom rdkit.Chem import AllChem
fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
2. Handling Class Imbalance
The Tox21 dataset is heavily imbalanced (~10:1 non-toxic to toxic ratio). This was addressed using class_weight='balanced' in the Random Forest, which automatically penalizes misclassification of the minority (toxic) class.
3. Model Selection
Three models were trained and compared:
ModelROC-AUCF1-ScoreLogistic Regression--Random ForestbestbestXGBoost--

ROC-AUC was chosen as the primary metric over accuracy because the dataset is imbalanced — a model predicting everything as non-toxic would score 90%+ accuracy but be completely useless.

4. Deployment
The app is served via FastAPI with a Jinja2 HTML frontend and deployed on Render (free tier). The /docs endpoint provides auto-generated interactive API documentation.

🛠️ Tech Stack
LayerTechnologyData & EDApandas, numpy, matplotlib, seabornFeature EngineeringRDKit (Morgan Fingerprints)Machine Learningscikit-learn (Random Forest)Imbalance Handlingclass_weight='balanced'Backend APIFastAPI + UvicornFrontendHTML + TailwindCSS + Jinja2DeploymentRenderVersion ControlGit + GitHub

 Dataset
Tox21 — NIH National Toxicology Program

7,831 chemical compounds
12 toxicity targets (NR-AR, SR-MMP, SR-p53, etc.)
Source: MoleculeNet

This project focuses on the NR-AR (Androgen Receptor) target for binary classification (toxic / non-toxic).

 Run Locally
Prerequisites

Python 3.10+
Anaconda or pip

Setup
bash# Clone the repo
git clone https://github.com/vipulsinghania26/drug-toxicity-predictor.git
cd drug-toxicity-predictor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload
Open → http://127.0.0.1:8000

📡 API Usage
The app exposes a REST API endpoint for developers:
bashGET /api/predict?smiles=CCO
Response:
json{
  "smiles": "CCO",
  "toxic": false,
  "confidence": 12.4,
  "verdict": " NON-TOXIC"
}
Interactive API docs available at → /docs

🔬 Key Learnings

Morgan Fingerprints are a powerful way to encode molecular structure for ML without deep learning
Class imbalance is the biggest challenge in toxicity prediction — ROC-AUC is far more meaningful than accuracy here
FastAPI's automatic /docs generation makes ML APIs significantly more professional
Deploying with environment-agnostic absolute paths (os.path.abspath) avoids common production bugs


Author
Vipul Singhania
GitHub: @vipulsinghania26
