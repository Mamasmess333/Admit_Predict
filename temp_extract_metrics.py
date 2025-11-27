import json, pathlib
path = pathlib.Path('College_Scorecard_Most_Recent_Institutional_Data/Notebooks/02_Preprocessing_and_Modeling.ipynb')
nb = json.loads(path.read_bytes().decode('utf-8'))
for cell in nb['cells']:
    if cell.get('cell_type') == 'code':
        for out in cell.get('outputs', []):
            text = ''
            if out.get('output_type') == 'stream':
                text = ''.join(out.get('text', ''))
            elif out.get('output_type') == 'execute_result':
                data = out.get('data', {})
                if 'text/plain' in data:
                    text = ''.join(data['text/plain'])
            if 'MODEL COMPARISON SUMMARY' in text:
                print(text)
