import csv

def is_personal_account(username, fullname, category):
    # Enhanced heuristic to determine if an account is personal
    brand_keywords = [
        'official', 'tv', 'music', 'show', 'channel', 'studio', 'group', 'team',
        'company', 'inc', 'corp', 'llc', 'ltd', 'entertainment', 'magazine',
        'com', 'store', 'shop', 'brand', 'corporation', 'group'
    ]
    personal_keywords = ['mr', 'ms', 'mrs', 'dr', 'prof', 'sir', 'lady', 'lord']

    # Check if the username or fullname contains any brand keywords
    if any(keyword in username.lower() for keyword in brand_keywords) or any(keyword in fullname.lower() for keyword in brand_keywords):
        return False

    # Check if the fullname contains any personal keywords
    if any(keyword in fullname.lower() for keyword in personal_keywords):
        return True

    # Check if the category suggests a brand
    brand_categories = ['shopping & retail', 'clothing & outfits', 'luxury', 'cinema & actors/actresses']
    if category.lower() in brand_categories:
        return False

    # If the fullname looks like a real name (contains a space), assume it's personal
    if ' ' in fullname:
        return True

    # Default to not personal
    return False

# Read the original CSV and write to a new CSV with the additional column
with open('hypeauditor_youtube_united_states_all_results.csv', 'r', encoding='utf-8') as infile, open('hypeauditor_youtube_united_states_all_results_updated.csv', 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['isPersonal']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in reader:
        username = row['contributorContentUsername']
        fullname = row['contributorContentFullname']
        category = row['category']
        row['isPersonal'] = 'T' if is_personal_account(username, fullname, category) else ''
        writer.writerow(row)

print("CSV file updated with personal account information.")