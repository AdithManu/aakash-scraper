from fetch import fetch
from cleanup import write_valid
import datetime
import os
import shutil
from jsonify_data import jsonify_data
from rank import print_rank
import json


from psids import user_details as jee_psids
from neet_psids import user_details as neet_psids



def extract_process(test_id:int, course='JEE'):
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


    fetch(test_id=test_id, output_folder=all_html, course=course)
    fails = write_valid(all_html=all_html, valid_html=valid_html)

    output_json_file = os.path.join(folder_name, "students_data.json")
    json_data = jsonify_data(valid_html, dump_file=output_json_file, fails=fails, course=course)
    return json_data, fails


def from_df(filename="students_data.json"):
    d = open(filename, "r")
    data = json.loads(d.read())
    json_data = data['data']
    fails = data['fails']
    return json_data, fails


def print_fails(fails, course='JEE'):
    if fails:
        done = []
        print("\nFails: ")
        header = (f"#   {'Name':<30}  {'Roll No.':<15}        {'PSID':<15}")
        print(header)
        print("-" * 68)
        # print(f"{f'{(j+1):01d}':<4}{student_name:<30}{enrollment_id:<15}\t{psid:<15}")
        j = 0
        if course == 'JEE':
            user_details = jee_psids
        else:
            user_details = neet_psids
        for i in user_details:
            if i['Enrollment ID'] in fails:
                student_name = i['Student Name']
                enrollment_id = i['Enrollment ID']
                psid = i['PSID']
                print(f"{f'{(j+1):01d}':<4}{student_name:<30}{enrollment_id:<15}\t{psid:<15}")
                # print(i['Student Name'], i['Enrollment ID'], i['PSID'])
                done.append(i['Enrollment ID'])
                j=j+1
        unknown = [i for i in fails if i not in done]
        if unknown:
            print("\nUnknown Roll Numbers: ", unknown)

