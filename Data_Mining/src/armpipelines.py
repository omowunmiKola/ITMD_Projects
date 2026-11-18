import sys
sys.path.insert(0, "../src")
import codebookmap

import pandas as pd
import numpy as np

import warnings

warnings.filterwarnings("ignore")

from codebookmap import BRFSS_MAP


def make_arm_a(df):  # naive: sentinels left as numbers, mean/mode, no decoding
    df = df.copy()
    nominal_cols = [
        col
        for col, rules in BRFSS_MAP.items()
        if rules["type"] == "nominal" and not rules.get("is_target")
    ]
    ordinal_cols = [
        col
        for col, rules in BRFSS_MAP.items()
        if rules["type"] in ["ordinal"] and not rules.get("is_target")
    ]
    numeric_cols = [
        "_AGE80",
        "CHILDREN",
        "PHYSHLTH",
        "MENTHLTH",
        "_BMI5",
        "SLEPTIM1",
        "FRUIT2",
        "FRUITJU2",
        "FVGREEN1",
        "FRENCHF1",
        "POTATOE1",
        "VEGETAB2",
    ]
    # Separate X and y d
    X = df[nominal_cols + ordinal_cols + numeric_cols].copy()
    y = df["CLASS"].astype(int)
    return X, y


def make_arm_b(df):  # forensic: decode, sentinels, indicators, dtypes
    df = df.copy()
    df = df.replace(5.397605346934028e-79, 0)

    cols_to_process = [
        "FRUIT2",
        "FRUITJU2",
        "FVGREEN1",
        "FRENCHF1",
        "POTATOE1",
        "VEGETAB2",
    ]
    new_names = ["FRUTDA2_", "FTJUDA2_", "GRENDA1_", "FRNCHDA_", "POTADA1_", "VEGEDA2_"]

    df.drop(columns=new_names, inplace=True)

    def decode_brfss_frequency(val):
        # Handle missing, "Don't know" (777), and "Refused" (999)
        if pd.isna(val) or val >= 700:
            return np.nan
        # 555 = Never
        elif val == 555:
            return 0.0
        # 300 = Less than once a month
        elif val == 300:
            return 0.02
        # 101-199 = Times per day
        elif 100 <= val < 200:
            return val - 100.0
        # 201-299 = Times per week
        elif 200 < val < 300:
            return round((val - 200) / 7.0, 2)
        # 301-399 = Times per month
        elif 300 < val < 400:
            return round((val - 300) / 30.0, 2)
        else:
            return np.nan
            
    # Pair up the old and new column names and apply the function
    for old_col, new_col in zip(cols_to_process, new_names):
        df[new_col] = df[old_col].apply(decode_brfss_frequency)

    df.drop(columns=cols_to_process, inplace=True)

    for col, rules in BRFSS_MAP.items():
        # Base rule: If column not target or in df, skip.
        if col not in df.columns or rules.get("is_target"):
            continue

        # RULE 1: NOMINAL values (Recode to text, fill NA with 'Unknown', cast to category)
        if rules["type"] == "nominal":
            if rules["sentinels"]:
                if isinstance(rules["sentinels"], dict):
                    # Replace with dictionary mapping (e.g. {7: 'Not Sure'})
                    df[col] = df[col].replace(rules["sentinels"])
                else:
                    # replace all sentinel with unknown'
                    df[col] = df[col].replace(rules["sentinels"], "Unknown")

            # Fill nan with 'Unknown'
            df[col] = df[col].fillna("Unknown")

            df[col] = df[col].astype(str).astype("category")

            # RULE 2: NUMERIC values (Sentinels to NaN, implied decimals, cast to float32)
        elif rules["type"] in ["ordinal", "continuous"]:
            if rules["sentinels"]:
                if isinstance(rules["sentinels"], dict):
                    # replace sentinels with nan
                    df[col] = df[col].replace(rules["sentinels"])
                else:
                    # Replace list items with NaN
                    df[col] = df[col].replace(rules["sentinels"], np.nan)

            # Apply implied decimals
            if rules["decimals"] > 0:
                df[col] = df[col] / (10 ** rules["decimals"])
                
            df[col] = df[col].astype("float32")

    nominal_cols = [
        col
        for col, rules in BRFSS_MAP.items()
        if rules["type"] == "nominal" and not rules.get("is_target")
    ]
    numeric_cols = [
        col
        for col, rules in BRFSS_MAP.items()
        if rules["type"] in ["ordinal", "continuous"] and not rules.get("is_target")
    ]

    # Separate X and y
    X = df[nominal_cols + numeric_cols].copy()
    y = df["CLASS"].astype(int)
    return X, y
