import csv
import json

def inject_data():
    csv_file = 'AH_Master_Merged.csv'
    html_file = 'dashboard_master.html'
    
    # Read CSV
    data = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        data = list(reader)
        
    print(f"Read {len(data)} rows from CSV.")
    
    # Create JSON string
    json_data = json.dumps(data, ensure_ascii=False, indent=2)
    
    # Read the HTML template
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Create the JSON string
    json_data = json.dumps(data, indent=2, ensure_ascii=False)

    # Find the injection markers
    start_marker = "// --- INJECTION MARKER START ---"
    end_marker = "// --- INJECTION MARKER END ---"

    start_idx = html_content.find(start_marker)
    end_idx = html_content.find(end_marker)

    if start_idx != -1 and end_idx != -1:
        # Construct new content
        new_content = (
            html_content[:start_idx] + 
            start_marker + "\n" + 
            f"const masterData = {json_data}; " + "\n" +
            html_content[end_idx:]
        )
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully injected data into index.html")
    else:
        print("Markers not found in index.html")

if __name__ == "__main__":
    inject_data()
