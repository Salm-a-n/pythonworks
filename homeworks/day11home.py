import json
from datetime import datetime
from tracker import create_record
records = [
    create_record("Paris", "Loved the Eiffel Tower!", "05-06-2022"),
    create_record("Tokyo", "Cherry blossoms were stunning.", "12-04-2023"),
    create_record("New York", "Times Square was electric!", "20-09-2025")
]

for record in records:
    original_date = datetime.strptime(record["date"], "%d-%m-%Y")
    readable_date = original_date.strftime("%B %d, %Y")
    record["date"] = readable_date

json_data = json.dumps(records, indent=2)
print(" JSON Output:\n", json_data)

# Parse JSON back and display each record
parsed_records = json.loads(json_data)
print("\n Parsed Records:")
for record in parsed_records:
    print(record)
