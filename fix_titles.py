import json

files = ['materi/data-understanding.ipynb', 'materi/data-preparation.ipynb']

for file in files:
    with open(file, 'r') as f:
        nb = json.load(f)
    
    changed = False
    for cell in nb.get('cells', []):
        if cell['cell_type'] == 'markdown':
            new_source = []
            for line in cell['source']:
                if line.startswith('# DATA UNDERSTANDING'):
                    line = '# Data Understanding\n'
                    changed = True
                elif line.startswith('# DATA PREPARATION'):
                    line = '# Data Preparation\n'
                    changed = True
                new_source.append(line)
            cell['source'] = new_source
            
    if changed:
        with open(file, 'w') as f:
            json.dump(nb, f, indent=1)
            print(f"Updated {file}")

