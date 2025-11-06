# import pdfplumber
# import pandas as pd

# pdf_path = "asbabul_nuzul.pdf"
# data = []

# with pdfplumber.open(pdf_path) as pdf:
#     for i, page in enumerate(pdf.pages):
#         text = page.extract_text()
#         # Example simple parsing: split by line
#         lines = text.split('\n')
#         for line in lines:
#             if line.strip():  # ignore empty lines
#                 # Dummy parsing: real parsing will depend on PDF format
#                 # Suppose line format: "2:1 - Reason text here"
#                 if "-" in line:
#                     ayah_ref, reason = line.split("-", 1)
#                     data.append({
#                         "ayah_ref": ayah_ref.strip(),
#                         "reason": reason.strip(),
#                         "source": "Al-Wahidi, Asbabul Nuzul",
#                         "page": i + 1
#                     })

# # Convert to CSV
# df = pd.DataFrame(data)
# df.to_csv("asbabul_nuzul_dataset.csv", index=False)
# print("Dataset created:", df.head())



# # pdf to text csv

# # import pdfplumber
# # import pandas as pd

# # pdf_path = "asbabul_nuzul.pdf"
# # data = []

# # with pdfplumber.open(pdf_path) as pdf:
# #     for page_num, page in enumerate(pdf.pages, start=1):
# #         text = page.extract_text()
# #         if text:
# #             data.append({
# #                 "page_number": page_num,
# #                 "text": text.strip()
# #             })

# # df = pd.DataFrame(data)
# # df.to_csv("asbabul_nuzul_text.csv", index=False)
# # print("✅ CSV file created: asbabul_nuzul_text.csv")


# import csv

# # CSV file ka naam
# csv_file = "asbabul_nuzul_full_data.csv"

# # Columns define kar do
# columns = [
#     "Surah Number",
#     "Verse Number(s)",
#     "Wahidi Reference",
#     "Source Text",
#     "Asbab al-Nuzul Summary",
#     "Key Figures",
#     "Tribes/Groups Mentioned",
#     "Historical Events",
#     "Themes/Topics",
#     "Legal Rulings (Fiqh)",
#     "Contextual Keywords",
#     "Pre-Islamic Customs",
#     "Type of Occasion",
#     "Authenticity Assessment",
#     "Relevance to Verse Interpretation",
#     "Notes/Commentary",
#     "Combined Text"
# ]

# # CSV file create aur header add kar do
# with open(csv_file, mode="w", encoding="utf-8", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=columns)
#     writer.writeheader()

# print(f"CSV file '{csv_file}' created with columns successfully!")

import pdfplumber
import pandas as pd
import csv

# PDF path
pdf_path = "asbabul_nuzul.pdf"

# Extracted data (simple text for now)
data = []

with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()
        if text:
            # Store each page as raw text for now
            data.append({
                "page_number": page_num,
                "text": text.strip()
            })

# Create intermediate CSV with raw text
df = pd.DataFrame(data)
df.to_csv("asbabul_nuzul_text.csv", index=False)
print("✅ CSV file created: asbabul_nuzul_text.csv")

# Now create final CSV with all desired columns
csv_file = "asbabul_nuzul_full_data.csv"

columns = [
    "Surah Number",
    "Verse Number(s)",
    "Wahidi Reference",
    "Source Text",
    "Asbab al-Nuzul Summary",
    "Key Figures",
    "Tribes/Groups Mentioned",
    "Historical Events",
    "Themes/Topics",
    "Legal Rulings (Fiqh)",
    "Contextual Keywords",
    "Pre-Islamic Customs",
    "Type of Occasion",
    "Authenticity Assessment",
    "Relevance to Verse Interpretation",
    "Notes/Commentary",
    "Combined Text"
]

# Create CSV with headers
with open(csv_file, mode="w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()

print(f"✅ CSV file '{csv_file}' created with columns successfully!")
