import os
import argparse
import pandas as pd


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    TODO: PASTE langkah preprocessing dari notebook lo ke sini.
    Pastikan step-nya sama persis dengan yang ada di Eksperimen_Alifya_Harsyarani.ipynb
    """
    df = df.drop_duplicates()

    df.columns = [c.strip() for c in df.columns]

    df = df.dropna()

    numeric_cols = [c for c in df.columns if "score" in c.lower()]
    for c in numeric_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df = df.dropna(subset=numeric_cols)

    return df


def main():
    parser = argparse.ArgumentParser(description="Automated preprocessing for MSML submission (Kriteria 1 - Skilled)")
    parser.add_argument(
        "--input",
        type=str,
        default="StudentsPerformance_raw.csv",
        help="Path file raw dataset (default: StudentsPerformance_raw.csv di root repo)",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default=os.path.join("preprocessing", "namadataset_preprocessing"),
        help="Folder output hasil preprocessing",
    )
    parser.add_argument(
        "--output_name",
        type=str,
        default="students_performance_preprocessing.csv",
        help="Nama file output",
    )
    args = parser.parse_args()

    input_path = args.input
    output_dir = args.output_dir
    output_path = os.path.join(output_dir, args.output_name)

    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(input_path):
        raise FileNotFoundError(
            f"File raw tidak ditemukan: {input_path}\n"
            f"Pastikan file StudentsPerformance_raw.csv ada di root repo, atau jalankan dengan --input <path>."
        )

    df = pd.read_csv(input_path)

    df_processed = preprocess_data(df)

    df_processed.to_csv(output_path, index=False)

    print("=== PREPROCESSING DONE ===")
    print(f"Input  : {input_path}")
    print(f"Output : {output_path}")
    print(f"Shape (raw)       : {df.shape}")
    print(f"Shape (processed) : {df_processed.shape}")
    print("==========================")


if __name__ == "__main__":
    main()
