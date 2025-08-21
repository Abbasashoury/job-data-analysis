import pandas as pd

data = pd.read_csv("jobs.csv")

skill = input("مهارت مورد نظر را وارد کنید: ").strip()

mask = data["مهارت‌ها"].str.contains(skill, case=False, na=False)
count = mask.sum()

print(f"تعداد مشاغل مرتبط با '{skill}': {count}")

with open("result.txt", "w", encoding="utf-8") as out:
    out.write(f"تعداد مشاغل مرتبط با '{skill}': {count}\n")
