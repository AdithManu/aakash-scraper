import requests
import base64
import os

from psids import user_details as jee_psids
from neet_psids import user_details as neet_psids

import threading


def encode_to_base64(input_string):
    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


URL = "http://aakashleap.com:3131/API/ResultRpt"


# def fetch(test_id, output_folder):
#     for i in user_details[:50]:
#         roll_no = i["Enrollment ID"]
#         rid = encode_to_base64(f"1,{test_id},{roll_no}")
#         r = requests.post(
#             url=URL,
#             params={"rid": rid},
#             data={
#                 "psid": i["PSID"],
#             },
#         )
#         with open(os.path.join(output_folder, f"roll_N-{roll_no}.html"), "w") as f:
#             f.write(r.text)
#             f.close()


# def fetch(test_id, output_folder, _range: range = range(0, 500)):
#     for i in _range:
#         roll_no = f"410242120{i:03d}"
#         rid = encode_to_base64(f"1,{test_id},{roll_no}")
#         r = requests.get(url=URL, params={"rid": rid})
#         with open(os.path.join(output_folder, f"roll_N-{roll_no}.html"), "w") as f:
#             f.write(r.text)
#             f.close()


def fetch_single(i, test_id, output_folder):
    roll_no = i["Enrollment ID"]
    rid = encode_to_base64(f"1,{test_id},{roll_no}")
    r = requests.post(
        url=URL,
        params={"rid": rid},
        data={"psid": i["PSID"]},
    )
    with open(os.path.join(output_folder, f"roll_N-{roll_no}.html"), "w") as f:
        f.write(r.text)

def fetch(test_id, output_folder, max_threads=10, course='JEE'):
    if course == 'JEE':
        user_details = jee_psids
    else:
        user_details = neet_psids
    threads = []
    for i in user_details[:50]:
        thread = threading.Thread(target=fetch_single, args=(i, test_id, output_folder))
        threads.append(thread)
        thread.start()
        
        while threading.active_count() > max_threads:
            pass

    for thread in threads:
        thread.join()
