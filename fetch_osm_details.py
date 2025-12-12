import requests
import json
import csv
import re
import time

def extract_ids_from_file(filepath):
    ids = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        # Extract ID from URLs like https://openinframap.org/.../plants/1227770834
        # Note: some IDs might be negative (relations in some contexts, though URL usually creates positive ref)
        matches = re.findall(r'/plants/(-?\d+)', content)
        for m in matches:
            ids.append(m)
    return list(set(ids))

def fetch_osm_data(ids):
    # Split IDs
    # OpenInfraMap uses negative IDs for Relations (convention)
    # Positive IDs could be Node, Way, or Relation
    
    pos_ids = [i for i in ids if int(i) > 0]
    neg_ids = [str(abs(int(i))) for i in ids if int(i) < 0]
    
    all_elements = []
    
    url = "https://overpass-api.de/api/interpreter"
    chunk_size = 40
    
    # Process Positive IDs (Generically)
    for i in range(0, len(pos_ids), chunk_size):
        chunk = pos_ids[i:i+chunk_size]
        chunk_str = ",".join(chunk)
        
        query = f"""
        [out:json][timeout:60];
        (
          node(id:{chunk_str});
          way(id:{chunk_str});
          relation(id:{chunk_str});
        );
        out center;
        """
        try:
            print(f"Fetching Positive chunk {i//chunk_size + 1}/{len(pos_ids)//chunk_size + 1}...")
            response = requests.post(url, data={'data': query})
            response.raise_for_status()
            data = response.json()
            all_elements.extend(data.get('elements', []))
            time.sleep(1) 
        except Exception as e:
            print(f"Error fetching positive chunk: {e}")

    # Process Negative IDs (Strictly Relations)
    for i in range(0, len(neg_ids), chunk_size):
        chunk = neg_ids[i:i+chunk_size]
        chunk_str = ",".join(chunk)
        
        query = f"""
        [out:json][timeout:60];
        (
          relation(id:{chunk_str});
        );
        out center;
        """
        try:
            print(f"Fetching Relation chunk {i//chunk_size + 1}/{len(neg_ids)//chunk_size + 1}...")
            response = requests.post(url, data={'data': query})
            response.raise_for_status()
            data = response.json()
            all_elements.extend(data.get('elements', []))
            time.sleep(1)
        except Exception as e:
            print(f"Error fetching relation chunk: {e}")
            
    return all_elements

def process_osm_elements(elements):
    rows = []
    for el in elements:
        tags = el.get('tags', {})
        
        # Determine Name
        name = tags.get('name', '')
        if not name:
             name = tags.get('alt_name', '')
        
        # Metadata
        row = {
            'OSM_ID': el['id'],
            'Type': el['type'],
            'Name': name,
            'Capacity': tags.get('plant:output:electricity', ''),
            'Operator': tags.get('operator', ''),
            'Start_Date': tags.get('start_date', ''),
            'Wikipedia': tags.get('wikipedia', ''),
            'Wikidata': tags.get('wikidata', ''),
            'Source_Method': tags.get('plant:method', ''),
            'Water_Source': tags.get('plant:source', ''),
        }
        
        # Coordinates (Center)
        # 'out center' gives 'lat'/'lon' for nodes, and 'center' object for ways/relations
        if 'lat' in el and 'lon' in el:
            row['Lat'] = el['lat']
            row['Lon'] = el['lon']
        elif 'center' in el:
            row['Lat'] = el['center']['lat']
            row['Lon'] = el['center']['lon']
        else:
            row['Lat'] = ''
            row['Lon'] = ''
            
        rows.append(row)
    return rows

def save_to_csv(rows, filepath):
    if not rows:
        print("No data to save.")
        return
        
    fieldnames = ['OSM_ID', 'Type', 'Name', 'Lat', 'Lon', 'Capacity', 'Operator', 'Start_Date', 'Wikipedia', 'Wikidata', 'Source_Method', 'Water_Source']
    
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {len(rows)} enriched entries to {filepath}")

def main():
    input_file = 'web_data_extracted.txt'
    output_file = 'AH_Web_Enriched.csv'
    
    ids = extract_ids_from_file(input_file)
    print(f"Found {len(ids)} unique IDs to fetch.")
    
    if ids:
        elements = fetch_osm_data(ids)
        rows = process_osm_elements(elements)
        save_to_csv(rows, output_file)

if __name__ == "__main__":
    main()
