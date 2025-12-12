import csv
import unicodedata
import re
from difflib import SequenceMatcher

def normalize(text):
    if not text:
        return ""
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    text = text.lower()
    
    remove_b = [
        "aproveitamento hidroeletrico ", "aproveitamento hidraulico ",
        "central hidroeletrica ", "central hidrica ", "mini-hidrica ",
        "minihidrica ", "barragem ", "acude ", "mini central hidroeletrica "
    ]
    for prefix in remove_b:
        text = text.replace(prefix, "")
        
    words = text.split()
    filtered_words = [w for w in words if w not in ["de", "da", "do", "das", "dos", "e", "-", "–"]]
    return " ".join(filtered_words)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def read_csv_data(filepath):
    data = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            data = list(reader)
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            reader = csv.DictReader(f, delimiter=';')
            data = list(reader)
    return data

def read_web_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def main():
    apa_file = 'AH_Lista.csv'
    web_file = 'AH_Web_Clean.csv'
    output_file = 'AH_Master_Merged.csv'

    apa_data = read_csv_data(apa_file)
    web_data = read_web_data(web_file)

    print(f"Loaded {len(apa_data)} APA rows and {len(web_data)} Web rows.")

    # Prepare for matching
    matched_web_indices = set()
    
    # Enrich APA data
    enriched_data = []
    
    for row in apa_data:
        # Find key column
        name_key = 'Aproveitamento Hidráulico'
        if name_key not in row:
             for k in row.keys():
                 if k and 'Aproveitamento' in k:
                     name_key = k
                     break
        
        original_name = row.get(name_key, '')
        norm_name = normalize(original_name)
        
        best_match_idx = -1
        best_score = 0.0
        match_type = ""

        # Strategy 1: Exact Normalized Match
        for idx, w_row in enumerate(web_data):
            if idx in matched_web_indices: continue
            
            w_norm = normalize(w_row['Name'])
            
            if w_norm == norm_name:
                best_match_idx = idx
                match_type = "Exact"
                break
        
        # Strategy 2: Substring / Fuzzy
        if best_match_idx == -1:
            for idx, w_row in enumerate(web_data):
                if idx in matched_web_indices: continue
                
                w_norm = normalize(w_row['Name'])
                
                # Substring
                if (len(w_norm)>3 and w_norm in norm_name) or (len(norm_name)>3 and norm_name in w_norm):
                    best_match_idx = idx
                    match_type = "Substring"
                    break
                
                # Roman Numeral check (simplified)
                w_base = re.sub(r' (i|ii|iii|1|2)$', '', w_norm)
                c_base = re.sub(r' (i|ii|iii|1|2)$', '', norm_name)
                if len(w_base)>3 and w_base == c_base:
                     best_match_idx = idx
                     match_type = "Variant"
                     break
                     
        # If matched, merge
        new_row = row.copy()
        if best_match_idx != -1:
            w_row = web_data[best_match_idx]
            matched_web_indices.add(best_match_idx)
            
            new_row['Source'] = 'Both'
            new_row['Match_Method'] = match_type
            new_row['Lat'] = w_row.get('Lat', '')
            new_row['Lon'] = w_row.get('Lon', '')
            new_row['Capacity_Web'] = w_row.get('Capacity', '')
            new_row['Operator_Web'] = w_row.get('Operator', '')
            new_row['Web_Name'] = w_row.get('Name', '')
            new_row['OSM_ID'] = w_row.get('OSM_ID', '')
        else:
            new_row['Source'] = 'APA'
            new_row['Match_Method'] = ''
            new_row['Lat'] = ''
            new_row['Lon'] = ''
            new_row['Capacity_Web'] = ''
            new_row['Operator_Web'] = ''
            new_row['Web_Name'] = ''
            new_row['OSM_ID'] = ''
            
        enriched_data.append(new_row)

    # Add remaining Web Data as new rows
    count_new_web = 0
    for idx, w_row in enumerate(web_data):
        if idx not in matched_web_indices:
            # Check if likely already exists but failed fuzzy? 
            # For now append
            new_row = {k: '' for k in enriched_data[0].keys()} # Empty schema
            # Map standard fields
            new_row['Aproveitamento Hidráulico'] = w_row['Name'] # Use Web Name as primary
            new_row['Source'] = 'OpenInfraMap'
            new_row['Lat'] = w_row.get('Lat', '')
            new_row['Lon'] = w_row.get('Lon', '')
            new_row['Capacity_Web'] = w_row.get('Capacity', '')
            new_row['Operator_Web'] = w_row.get('Operator', '')
            new_row['Web_Name'] = w_row.get('Name', '')
            new_row['OSM_ID'] = w_row.get('OSM_ID', '')
            # Default "Finalidade" to Energia if from this source?
            new_row['Finalidade'] = 'Energia (Assumed)'
            
            enriched_data.append(new_row)
            count_new_web += 1

    # Save
    # Collect all unique keys from all rows
    all_keys = set()
    for row in enriched_data:
        all_keys.update(row.keys())
        
    fieldnames = list(all_keys)
    
    # Ensure important cols are first and Sorted for consistency
    priority = ['Aproveitamento Hidráulico', 'Source', 'Lat', 'Lon', 'Capacity_Web', 'Finalidade', 'Bacia']
    remaining = sorted([f for f in fieldnames if f not in priority])
    fieldnames = priority + remaining
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', extrasaction='ignore') 
        writer.writeheader()
        writer.writerows(enriched_data)
        
    print(f"Merge Complete.")
    print(f"- Matches Found: {len(matched_web_indices)}")
    print(f"- New Web-Only Entries: {count_new_web}")
    print(f"- Total Rows: {len(enriched_data)}")
    print(f"- Saved to {output_file}")

if __name__ == "__main__":
    main()
