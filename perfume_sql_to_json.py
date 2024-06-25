import sqlite3
import json
import ast


def save_to_json():
    conn = sqlite3.connect('perfume_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM perfumes')
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description if description[0] not in ('id', 'image_id')]

    perfumes = []
    for counter, row in enumerate(rows):
        perfume = dict(zip(column_names, [value for i, value in enumerate(row) if cursor.description[i][0] not in ('id', 'image_id')]))

        if 'ingredients' in perfume:
            try:
                perfume['ingredients'] = ast.literal_eval(perfume['ingredients'])
            except (ValueError, SyntaxError) as e:
                print(e)

        if not perfume.get('ingredients'):
            continue

        if 'brand' in perfume:
            perfume['brand'] = perfume['brand'].title()
        if 'name_perfume' in perfume:
            perfume['name_perfume'] = perfume['name_perfume'].title()

        # Convert genders
        if 'gender' in perfume:
            gender_map = {'M': 'Male', 'F': 'Female', 'U': 'Unisex'}
            perfume['gender'] = gender_map.get(perfume['gender'], perfume['gender'])

        perfumes.append(perfume)

        # if counter == 1100:
        #     break

    with open('perfumes.json', 'w', encoding='utf-8') as json_file:
        json.dump(perfumes, json_file, ensure_ascii=False, indent=0)

    conn.close()


save_to_json()
