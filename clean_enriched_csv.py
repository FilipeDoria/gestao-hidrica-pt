import csv

def clean_csv():
    input_file = 'AH_Web_Enriched.csv'
    output_file = 'AH_Web_Clean.csv'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
        
    print(f"Total rows read: {len(rows)}")
    
    cleaned_rows = []
    seen_ids = set()
    
    # Priority: items with Name > items with valid Type > items with Coordinates
    # Actually, simpler: Drop items with no Name.
    # If duplicates exist (e.g. Node and Way both have same ID and Name?), keep the one with more fields.
    
    # First, filter out rows with empty names
    valid_rows = [r for r in rows if r['Name'].strip()]
    
    # Group by ID to handle duplicates (if any)
    by_id = {}
    for r in valid_rows:
        oid = r['OSM_ID']
        if oid not in by_id:
            by_id[oid] = []
        by_id[oid].append(r)
        
    final_rows = []
    for oid, group in by_id.items():
        # If multiple, pick the one with most filled fields
        if len(group) > 1:
            best_row = max(group, key=lambda x: sum(1 for v in x.values() if v.strip()))
            final_rows.append(best_row)
        else:
            final_rows.append(group[0])
            
    print(f"Rows after cleaning: {len(final_rows)}")
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(final_rows)
        
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_csv()
