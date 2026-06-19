from __future__ import annotations

import os
from typing import Any

import joblib
import numpy as np
import pandas as pd

from sklearn.base import clone
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
     accuracy_score,
     classification_report,
     confusion_matrix,
     f1_score,
     precision_score,
     recall_score,
     roc_auc_score
)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

## Creation of Synthetic dataset
def create_loan_dataset(
    n_samples: int = 1200,
    random_state: int = 42,
) -> pd.DataFrame:
    rng = np.random.default_rng(random_state)

    applicant_income = rng.integers(
        25_000,
        200_000,
        n_samples,
    )

    loan_amount = rng.integers(
        10_000,
        160_000,
        n_samples,
    )

    credit_score = np.clip(
        rng.normal(650, 85, n_samples),
        300,
        850,
    ).round().astype(int)

    existing_debt = rng.integers(
        0,
        120_000,
        n_samples,
    )

    employment_years = np.clip(
        rng.normal(6, 4, n_samples),
        0,
        35,
    ).round(1)

    loan_term = rng.choice(
        [12, 24, 36, 48, 60],
        n_samples,
        p=[0.10, 0.20, 0.35, 0.20, 0.15],
    )

    employment_type = rng.choice(
        ["Salaried", "Self-employed", "Contract"],
        n_samples,
        p=[0.60, 0.25, 0.15],
    )

    education = rng.choice(
        ["High School", "Graduate", "Postgraduate"],
        n_samples,
        p=[0.25, 0.55, 0.20],
    )

    property_area = rng.choice(
        ["Urban", "Semiurban", "Rural"],
        n_samples,
        p=[0.45, 0.35, 0.20],
    )

    self_employed = np.where(
        employment_type == "Self-employed",
        "Yes",
        rng.choice(
            ["No", "Yes"],
            n_samples,
            p=[0.95, 0.05],
        ),
    )

    debt_to_income = (
        existing_debt
        / np.maximum(applicant_income, 1)
    )

    score = (
        0.012 * (credit_score - 650)
        + 0.000012 * (applicant_income - 80_000)
        - 0.000014 * (loan_amount - 60_000)
        - 1.8 * debt_to_income
        + 0.09 * employment_years
        + np.where(
            employment_type == "Salaried",
            0.35,
            np.where(
                employment_type == "Self-employed",
                0.10,
                -0.25,
            ),
        )
        + np.where(
            education == "Postgraduate",
            0.20,
            np.where(
                education == "Graduate",
                0.10,
                -0.10,
            ),
        )
        + np.where(
            property_area == "Urban",
            0.08,
            0.0,
        )
        + rng.normal(0, 0.9, n_samples)
        - 0.80
    )

    approval_probability = 1 / (
        1 + np.exp(-score)
    )

    loan_approved = (
        rng.random(n_samples)
        < approval_probability
    ).astype(int)

    df = pd.DataFrame({
        "applicant_income": applicant_income,
        "loan_amount": loan_amount,
        "credit_score": credit_score,
        "existing_debt": existing_debt,
        "employment_years": employment_years,
        "loan_term": loan_term,
        "employment_type": employment_type,
        "education": education,
        "property_area": property_area,
        "self_employed": self_employed,
        "loan_approved": loan_approved,
    })

    # Add a few missing values to simulate raw data.
    missing_columns = [
        "credit_score",
        "employment_years",
        "employment_type",
        "education",
    ]

    for column in missing_columns:
        missing_indices = rng.choice(
            n_samples,
            size=int(0.03 * n_samples),
            replace=False,
        )
        df.loc[missing_indices, column] = np.nan

    return df

## create and Inspect Data
df = create_loan_dataset()

print("First five rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nTarget distribution:")
print(df["loan_approved"].value_counts())

print("\nTarget percentage:")
print(
    df["loan_approved"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)
