import csv
import json
import os

CSV_FILE = "AH_Lista.csv"
HTML_FILE = "dashboard_hidricas.html"

def main():
    # 1. Read CSV Data
    print(f"Reading {CSV_FILE}...")
    data = []
    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        # Use semi-colon delimiter
        reader = csv.DictReader(f, delimiter=';')
        
        for row in reader:
            # Map CSV columns to Dashboard Expected Keys
            # AH_Lista.csv: Bacia Hidrográfica;Aproveitamento Hidráulico;N.º Contrato Concessão (CC);Finalidade CC;...;Data CC - Termo;...
            
            item = {
                "Name": row.get("Aproveitamento Hidráulico", "").replace('\n', ' ').strip(),
                "Contract": row.get("N.º Contrato Concessão (CC)", "").replace('\n', ' ').strip(),
                "Bacia": row.get("Bacia Hidrográfica", "").replace('\n', ' ').strip(),
                "Purpose": row.get("Finalidade CC", "").replace('\n', ' ').strip(),
                "Data Termo": row.get("Data CC - Termo", "").replace('\n', ' ').strip()
            }
            # Basic validation
            if not item["Name"]: continue
            
            data.append(item)
    
    json_data = json.dumps(data, ensure_ascii=False)
    
    # 2. Read HTML
    print(f"Reading {HTML_FILE}...")
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    # 3. Replace content between markers
    marker_start = "// --- INJECTION MARKER START ---"
    marker_end = "// --- INJECTION MARKER END ---"
    
    start_idx = html_content.find(marker_start)
    end_idx = html_content.find(marker_end)
    
    if start_idx != -1 and end_idx != -1:
        new_content = f"{marker_start}\n        const concessionData = {json_data};\n        {marker_end}"
        
        # Replace the chunk
        new_html = html_content[:start_idx] + new_content + html_content[end_idx + len(marker_end):]
        
        print(f"Writing updated HTML to {HTML_FILE}...")
        with open(HTML_FILE, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Success!")
    else:
        print(f"Error: Could not find markers '{marker_start}' or '{marker_end}' in HTML.")

if __name__ == "__main__":
    main()
