import pandas as pd
df = extract_tsv(preprocess_image("page_1.png"))

df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)