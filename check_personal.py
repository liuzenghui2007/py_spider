import csv

def is_personal_account(nickname, full_name, category):
    # Simple heuristic to determine if an account is personal
    # This can be improved with more sophisticated logic
    brand_indicators = ['official', 'studios', 'entertainment', 'magazine', 'com', 'store', 'shop', 'brand', 'corporation', 'inc', 'ltd', 'group', 'company']
    if any(indicator in nickname.lower() for indicator in brand_indicators):
        return ''
    if any(indicator in full_name.lower() for indicator in brand_indicators):
        return ''
    if category.lower() in ['shopping & retail', 'clothing & outfits', 'luxury', 'cinema & actors/actresses']:
        return ''
    return 'T'

# Read the CSV file with a different encoding
with open('result.csv', 'r', encoding='latin1') as infile:
    reader = csv.reader(infile)
    rows = list(reader)

# Add the new column header
rows[0].append('Is Personal Account')

# Process each row and determine if it's a personal account
for row in rows[1:]:
    nickname = row[1]
    full_name = row[2]
    category = row[3]
    personal_account = is_personal_account(nickname, full_name, category)
    row.append(personal_account)

# Write the updated data back to a new CSV file
with open('result_with_personal_account.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print("Processing complete. The updated file is saved as 'result_with_personal_account.csv'.")