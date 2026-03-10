Drug Toxicity Predictor
An end-to-end machine learning web application that predicts the toxicity of drug compounds from molecular SMILES strings using Morgan Fingerprints and a Random Forest classifier — deployed live with FastAPI.
🔗 Live Demo: 
drug-toxicity-predictor.onrender.com

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



Author
Vipul Singhania
GitHub: @vipulsinghania26
