# Secure Emergency Alert System

An ML-based secure emergency alert system for a restricted facility.

## Project Overview

The system uses sensor readings to detect possible fire conditions using
a Logistic Regression machine learning model.

When an emergency is detected, the system will generate an alert.
The alert will later be protected using cryptographic techniques.

## Machine Learning

The current ML model uses five sensor features:

- Temperature
- Humidity
- TVOC
- eCO2
- PM2.5

Model:

- Logistic Regression
- StandardScaler
- 80/20 stratified train-test split

## Dataset

Dataset source:

Kaggle Smoke Detection IoT Dataset

The dataset itself is not included in this repository.

See `data/README.md` for dataset information.

## Project Structure

```text
secure-emergency-alert/
├── data/
├── notebooks/
├── src/
├── results/
├── docs/
├── requirements.txt
├── .gitignore
└── README.md