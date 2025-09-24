import os,json

new_data = []
for file in os.listdir('individuals'):
    with open(f'individuals/{file}') as f:
        data = json.load(f)
        if data['data'] == []:
            print(file)
        else:
            new_data.append(data['data'][0])

existing_data = json.load(open('students_data.json'))
existing_data['data'].extend(new_data)


f = open('all_together.json','w')
f.write(json.dumps(existing_data, indent=2))
f.close()