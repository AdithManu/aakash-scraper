from fetch import fetch_single
from cleanup import write_valid
import datetime
import os
import shutil
from jsonify_data import jsonify_data
from rank import print_rank
from modules import print_fails



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



def run_single(roll_no_prefix, test_id, psid, dump_filename, course):
    print(dump_filename)


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


    # 410252050026
    for i in range(0,500):
        
        roll_no = f'{roll_no_prefix}{i:03d}' # 2yr jee 
        # 410242120
        # roll_no = f'410252050{i:03d}' # 1yr jee 
        # roll_no = f"410241120{i:03d}" # 2yr neet
        # roll_no = f"410242120{i:03d}"
        print(i)
        fetch_single(i={"Enrollment ID": roll_no, 'PSID': psid}, test_id=test_id, output_folder=all_html)
        fails = write_valid(all_html=all_html, valid_html=valid_html)
        if len(fails) == 0:
            break
        else:
            clean_directory(all_html)


    json_data = jsonify_data(valid_html, dump_file=dump_filename, course=course)



    # print_rank(json_data)

    #     print("\nFails: ", fails)

    print_rank(json_data,course=course)

    if fails:
        print_fails(fails,course=course)




fails = [
    
#         # {'name': 'ADITH MANU', 'rollNo': 410242120050, 'psid': '00011939166'},    
# {'name': 'APOORVA RAJ', 'rollNo': 410242120077, 'psid': '00010200893'},    
# # {'name': 'KAVANA GOWDA', 'rollNo': 410242120267, 'psid': '00011935852'},    
# # {'name': 'MOHAMMAD AHAYAAN HUSSAIN.', 'rollNo': 410242120104, 'psid': '00012903119'},    
# # {'name': 'MOHAMMED SUFYAAN', 'rollNo': 410242120169, 'psid': '00012902274'},    
# # {'name': 'NEHA VINAYAJITH', 'rollNo': 410242120221, 'psid': '00012568381'},    
# # {'name': 'NINAAD MADHUSUDAN', 'rollNo': 410242120103, 'psid': '00012941668'},    
# # {'name': 'PRANAV VIJAY', 'rollNo': 410242120029, 'psid': '00008877136'},    
# # {'name': 'PRISHA BANSAL', 'rollNo': 410242120293, 'psid': '00005001083'},    
# # {'name': 'RITWIK BHARDWAJ', 'rollNo': 410242120109, 'psid': '00012905084'},    
# # {'name': 'RNAGA DHEERAJ', 'rollNo': 410242120207, 'psid': '00013786670'},    
# # {'name': 'SAMARTH M', 'rollNo': 410242120105, 'psid': '00012935833'},    
# # {'name': 'SANJANA KULKARNI', 'rollNo': 410242120001, 'psid': '00012346044'},    
# # {'name': 'SANJAY R', 'rollNo': 410242120038, 'psid': '00012571895'},    
# # {'name': 'SANVI ANTIN', 'rollNo': 410242120083, 'psid': '00012679537'},    
# # {'name': 'SARAH AHMED', 'rollNo': 410242120177, 'psid': '00013045770'},    
# # {'name': 'SHANKAR NAIR', 'rollNo': 410242120060, 'psid': '00012544677'},    
# # {'name': 'SHREYA RB', 'rollNo': 410242120282, 'psid': '00005478821'},    
# # {'name': 'SWARNAVERMA .', 'rollNo': 410242120096, 'psid': '00012841837'},    
# # {'name': 'SYED SHAHNAWAZ', 'rollNo': 410242120151, 'psid': '00013197106'},    
# # {'name': 'SYEDA MUSFIRA AFREEN.', 'rollNo': 410242120115, 'psid': '00013063683'},    
# # {'name': 'VANSH A', 'rollNo': 410242120027, 'psid': '00009371324'},    
# # {'name': 'YNITHIN REDDY', 'rollNo': 410242120145, 'psid': '00013079466'},    
# # {'name': 'SAKET N GUPTA.', 'rollNo': 410252050026, 'psid': '00014942557'},    
# # {'name': 'MYESHA AHMED', 'rollNo': 410252050046, 'psid': '00015134447'},    
# {'name': 'TEJAS RAMPUR', 'rollNo': 410252050021, 'psid': '00014916891'},

# {'name': 'AHAAN DANGWAL', 'rollNo': 410242120091, 'psid': '00012804213'},    
{'name': 'APOORVA RAJ', 'rollNo': 410242120077, 'psid': '00010200893'},    
# {'name': 'GANESH HARIHARA DAYALU', 'rollNo': 410242120080, 'psid': '00012673561'},    
{'name': 'RITWIK BHARDWAJ', 'rollNo': 410242120109, 'psid': '00012905084'},    
{'name': 'SARAH AHMED', 'rollNo': 410242120177, 'psid': '00013045770'},    
{'name': 'SAKET N GUPTA.', 'rollNo': 410252050026, 'psid': '00014942557'},
    
]

test_id = 1191081
course='JEE'


for fail in fails:
    run_single(roll_no_prefix=fail['rollNo']//1000, test_id=test_id, psid=fail['psid'], dump_filename=f"individuals/{fail['name']}.json", course=course)

# tests = [
# {'date': '2025-09-13', 'test_id': 1189341, 'test_name': "Part Test SS JEE(Main) & KCET-2526"},
# {'date': '2025-09-06', 'test_id': 1186662, 'test_name': "Unit Test SS JEE(Main) & KCET-2526"},
# {'date': '2025-08-28', 'test_id': 1184428, 'test_name': "Part Test SS JEE(Main) & KCET-2526"},
# {'date': '2025-07-31', 'test_id': 1173808, 'test_name': "Part Test SS JEE(Main) & KCET-2526"},
# {'date': '2025-07-27', 'test_id': 1171854, 'test_name': "AKCETS SS JEE(Main) & KCET-2526"},
# {'date': '2025-07-11', 'test_id': 1166667, 'test_name': "Unit Test SS JEE(Main) & KCET-2526"},
# {'date': '2025-07-04', 'test_id': 1154201, 'test_name': "Part Test SS JEE(Main) & KCET-2526"},
# {'date': '2025-06-19', 'test_id': 1164185, 'test_name': "Part Test SS JEE(Main) & KCET-2526"},
# {'date': '2025-06-04', 'test_id': 1159051, 'test_name': "Unit Test SS JEE(Main) & KCET-2526"},
# {'date': '2025-05-29', 'test_id': 1153129, 'test_name': "Part Test SS JEE(Main) & KCET-2526"},
# {'date': '2024-09-28', 'test_id': 1062932, 'test_name': "Unit Test_FS-2426(Ph-1)_Wknd"},
# ]
# tests.reverse()


# roll_no = 410242120005
# psid = '00005936714'
# course='JEE'


# for test in tests:
#     test_id = test['test_id']
#     # os.mkdir(f"dump_folder/{test_id}")
#     all_html = f"dump_folder/{test_id}/all"
#     # os.mkdir(all_html)
#     valid_html = f"dump_folder/{test_id}/valid"
#     # os.mkdir(valid_html)
#     # fetch_single(i={"Enrollment ID": roll_no, 'PSID': psid}, test_id=test_id, output_folder=all_html)
#     fails = write_valid(all_html=all_html, valid_html=valid_html)
#     # if len(fails) == 0:
#     #     break
#     # else:
#     #     clean_directory(all_html)

#     if len(fails) > 0:
#         continue    
#     json_data = jsonify_data(valid_html, dump_file=f"sidd/{test_id}.json", course=course)


#     max_marks = float(json_data[0]['Score']['Total']['Maximum Score'])
#     print("\n\n\n",f"Out of {max_marks}", "\t", test['date'],"\t",test['test_name'],"\n")
#     print_rank(json_data,course=course)

#     # if fails:
#     #     print_fails(fails,course=course)
