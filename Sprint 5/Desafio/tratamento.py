import pandas as pd

# Carrega o arquivo CSV
file_path = "C:\\Users\\mggir\\OneDrive\\Área de Trabalho\\sprint_5\\repasse-s.csv"
df = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Remove os pontos usados como separadores de milhares e substitui a vírgula por ponto para a separação decimal
df["Total Repassado"] = (
    df["Total Repassado"].replace({r"\.": "", ",": "."}, regex=True).astype(float)
)

# Salva o arquivo CSV processado
processed_file_path = (
    "C:\\Users\\mggir\\OneDrive\\Área de Trabalho\\sprint_5\\repasse-s-processado.csv"
)
df.to_csv(processed_file_path, sep=";", index=False)
