import pandas as pd
from pathlib import Path

BASE_DIR = Path("College_Scorecard_Most_Recent_Institutional_Data/22-23 Pell Grants")
FILES = [
    ("grants-ay22-23-q1.xls", "Q1"),
    ("grants-ay22-23-q2.xls", "Q2"),
    ("grants-ay22-23-q3.xls", "Q3"),
    ("grants-ay22-23-q4.xls", "Q4"),
]


def load_quarter(path: Path, quarter: str) -> pd.DataFrame:
    df = pd.read_excel(path, header=[5, 6])
    df.columns = [
        "OPEID"
        if (str(a).strip() == "" and b == "OPE ID")
        else "School"
        if (str(a).strip() == "" and b == "School")
        else "State"
        if (str(a).strip() == "" and b == "State")
        else "ZipCode"
        if (str(a).strip() == "" and b == "Zip Code")
        else "SchoolType"
        if (str(a).strip() == "" and b == "School Type")
        else f"{str(a).strip()}__{str(b).strip()}"
        for a, b in df.columns
    ]
    df = df[df["OPEID"].notna()]
    df = df[df["OPEID"] != "Grand Total"]
    df["Quarter"] = quarter
    return df


def main() -> None:
    frames = [load_quarter(BASE_DIR / fname, qtr) for fname, qtr in FILES]
    combined = pd.concat(frames, ignore_index=True)

    id_cols = ["OPEID", "School", "State", "ZipCode", "SchoolType"]
    numeric_cols = [c for c in combined.columns if c not in id_cols + ["Quarter"]]

    combined[numeric_cols] = combined[numeric_cols].replace("-", 0)
    combined[numeric_cols] = combined[numeric_cols].apply(pd.to_numeric, errors="coerce")
    combined["OPEID"] = combined["OPEID"].astype(str).str.zfill(8)

    agg = combined.groupby("OPEID", as_index=False)[numeric_cols].sum(min_count=1)
    ref = (
        combined.groupby("OPEID")[["School", "State", "ZipCode", "SchoolType"]]
        .first()
        .reset_index()
    )
    agg = agg.merge(ref, on="OPEID", how="left")
    agg["quarters_reporting"] = (
        combined.groupby("OPEID")["Quarter"].nunique().reset_index(drop=True)
    )

    out_path = BASE_DIR / "pell_grants_ay2022_2023_fullyear.csv"
    agg.to_csv(out_path, index=False)
    print(f"Aggregated {len(agg)} institutions -> {out_path}")


if __name__ == "__main__":
    main()

