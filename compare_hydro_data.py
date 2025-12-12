import csv
import re
import unicodedata

def normalize(text):
    if not text:
        return ""
    # Normalize unicode characters
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    text = text.lower()
    
    # Remove common prefixes/words
    remove_b = [
        "aproveitamento hidroeletrico ",
        "aproveitamento hidraulico ",
        "central hidroeletrica ",
        "central hidrica ",
        "mini-hidrica ",
        "minihidrica ",
        "barragem ",
        "acude ",
        "mini central hidroeletrica "
    ]
    
    for prefix in remove_b:
        text = text.replace(prefix, "")
        
    # Remove prepositions
    words = text.split()
    filtered_words = [w for w in words if w not in ["de", "da", "do", "das", "dos", "e", "-", "–"]]
    return " ".join(filtered_words)

def read_web_data(filepath):
    names = set()
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        # Regex to extract [Name](url)
        matches = re.findall(r'\[(.*?)\]\(http', content)
        for match in matches:
            # Clean up Wikidata references if mixed in (though our file seems clean)
            if not match.startswith("Values"): 
                names.add(match.strip())
    return names

def read_csv_data(filepath):
    names = set()
    with open(filepath, 'r', encoding='latin-1') as f: # Assuming latin-1 or utf-8
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            if 'Aproveitamento Hidráulico' in row:
                names.add(row['Aproveitamento Hidráulico'].strip())
            elif 'Aproveitamento Hidraulico' in row: # Fallback
                names.add(row['Aproveitamento Hidraulico'].strip())
    return names

def main():
    web_file = 'web_data_extracted.txt'
    csv_file = 'AH_Lista.csv'
    
    try:
        web_names = read_web_data(web_file)
    except Exception as e:
        print(f"Error reading web data: {e}")
        return

    try:
        # Try UTF-8 first, then Latin-1
        try:
             csv_names = read_csv_data_encoding(csv_file, 'utf-8')
        except UnicodeDecodeError:
             csv_names = read_csv_data_encoding(csv_file, 'latin-1')
    except Exception as e:
        print(f"Error reading CSV data: {e}")
        return

    print(f"Total Web Entries: {len(web_names)}")
    print(f"Total CSV Entries: {len(csv_names)}")

    web_norm = {name: normalize(name) for name in web_names}
    csv_norm = {name: normalize(name) for name in csv_names}
    
    web_norm_inv = {v: k for k, v in web_norm.items()}
    csv_norm_inv = {v: k for k, v in csv_norm.items()}
    
    common_keys = set(web_norm.values()) & set(csv_norm.values())

    # Potential Matches (Substring or Levenshtein-ish)
    potential_matches = []
    
    # helper to clean for fuzzy
    def clean_for_fuzzy(text):
        return text.replace("-", " ").replace("  ", " ").strip()

    csv_norm_clean = {k: clean_for_fuzzy(v) for k, v in csv_norm.items() if v not in common_keys} # only look at unmatched
    web_norm_clean = {k: clean_for_fuzzy(v) for k, v in web_norm.items() if v not in common_keys} # only look at unmatched
    
    matched_web = set()
    matched_csv = set()

    for w_orig, w_clean in web_norm_clean.items():
        if w_clean in matched_web: continue
        best_match = None
        
        # Check if CSV name is IN Web name or vice versa
        for c_orig, c_clean in csv_norm_clean.items():
            if c_clean in matched_csv: continue
            
            # Substring match
            if (len(c_clean) > 3 and c_clean in w_clean) or (len(w_clean) > 3 and w_clean in c_clean):
                 potential_matches.append((w_orig, c_orig, "Substring Match"))
                 matched_web.add(w_clean)
                 matched_csv.add(c_clean)
                 break
            
            # Check for Roman Numeral differences (e.g. "Bemposta I" vs "Bemposta")
            # Remove I, II, 1, 2 at end
            w_base = re.sub(r' (i|ii|iii|1|2)$', '', w_clean)
            c_base = re.sub(r' (i|ii|iii|1|2)$', '', c_clean)
            if (len(w_base) > 3 and w_base == c_base):
                 potential_matches.append((w_orig, c_orig, "Name Variant I/II"))
                 matched_web.add(w_clean)
                 matched_csv.add(c_clean)
                 break

    # Re-calculate Unmatched
    final_only_web = [k for k, v in web_norm.items() if v not in common_keys and clean_for_fuzzy(v) not in matched_web]
    final_only_csv = [k for k, v in csv_norm.items() if v not in common_keys and clean_for_fuzzy(v) not in matched_csv]

    # Generate Report
    with open('comparison_results.md', 'w', encoding='utf-8') as f:
        f.write("# Hydro Data Comparison Report\n\n")
        f.write(f"- Total Web Entries: {len(web_names)}\n")
        f.write(f"- Total CSV Entries: {len(csv_names)}\n")
        f.write(f"- Exact Matches (Normalized): {len(common_keys)}\n")
        f.write(f"- Potential Matches Found: {len(potential_matches)}\n")
        f.write(f"- Likely Only in Web: {len(final_only_web)}\n")
        f.write(f"- Likely Only in CSV: {len(final_only_csv)}\n\n")
        
        f.write("## Method\n")
        f.write("1. **Exact Match**: Normalized (lowercase, removed prefixes like 'Central Hidroelétrica').\n")
        f.write("2. **Potential Match**: Substring matching (e.g. 'Bemposta' in 'Bemposta I') or Roman Numeral normalization.\n\n")

        f.write("## 1. Exact Matches\n")
        for key in sorted(common_keys):
            f.write(f"- {web_norm_inv[key]} (Web) == {csv_norm_inv[key]} (CSV)\n")

        f.write("\n## 2. Potential Matches\n")
        for w, c, reason in sorted(potential_matches):
            f.write(f"- **{w}** (Web) ~ **{c}** (CSV) [{reason}]\n")
            
        f.write("\n## 3. Only in Web (OpenInfraMap)\n")
        for key in sorted(final_only_web):
            f.write(f"- {key}\n")
            
        f.write("\n## 4. Only in CSV (AH_Lista)\n")
        for key in sorted(final_only_csv):
            f.write(f"- {key}\n")

def read_csv_data_encoding(filepath, encoding):
    names = set()
    with open(filepath, 'r', encoding=encoding) as f:
        reader = csv.DictReader(f, delimiter=';')
        # Check first row keys to handle potential BOM or encoding issues on keys
        first_row = next(reader)
        key = 'Aproveitamento Hidráulico'
        # Handle cases where encoding might mess up the header
        if key not in first_row:
             # Try to find a key that looks like it
             for k in first_row.keys():
                 if 'Aproveitamento' in k:
                     key = k
                     break
        
        # Add first row
        if key in first_row:
             if first_row[key].strip():
                names.add(first_row[key].strip())

        for row in reader:
            if key in row and row[key].strip():
                names.add(row[key].strip())
    return names

if __name__ == "__main__":
    main()
