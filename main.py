from fetch import fetch
from cleanup import write_valid
import datetime
import os
import shutil
from jsonify_data import jsonify_data
from rank import print_rank


test_id = 1159051

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
folder_name = f"results_{timestamp}_ID{test_id}"

# folder_name = 'results_2025-07-05_00-45-25_ID1159051'
if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
os.makedirs(folder_name)


all_html = os.path.join(folder_name, "all_html")
valid_html = os.path.join(folder_name, "valid_html")
os.makedirs(all_html)
os.makedirs(valid_html)


fetch(test_id=test_id, output_folder=all_html)
fails = write_valid(all_html=all_html, valid_html=valid_html)

output_json_file = os.path.join(folder_name, "students_data.json")
json_data = jsonify_data(valid_html, dump_file=output_json_file)

print_rank(json_data)

if fails:
    print("\nFails: ", fails)


