from fetch import fetch_single
from cleanup import write_valid
import datetime
import os
import shutil
from jsonify_data import jsonify_data
from rank import print_rank


def clean_directory(directory_path):
    if os.path.exists(directory_path):
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")


test_id = 1159051
psid='00012346044'

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
folder_name = f"results(S)_{timestamp}_ID{test_id}"

# folder_name = 'results(S)_2025-07-05_00-45-25_ID1159051'
if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
os.makedirs(folder_name)


all_html = os.path.join(folder_name, "all_html")
valid_html = os.path.join(folder_name, "valid_html")
os.makedirs(all_html)
os.makedirs(valid_html)


for i in range(500):
    roll_no = f"410242120{i:03d}"
    print(i)
    fetch_single(i={"Enrollment ID": roll_no, 'PSID': psid}, test_id=test_id, output_folder=all_html)
    fails = write_valid(all_html=all_html, valid_html=valid_html)
    if len(fails) == 0:
        break
    else:
        clean_directory(all_html)

json_data = jsonify_data(valid_html)

print_rank(json_data)

if fails:
    print("\nFails: ", fails)
