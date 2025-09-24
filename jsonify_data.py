import os
import json
from bs4 import BeautifulSoup
from psids import user_details as jee_psids
from neet_psids import user_details as neet_psids



def safe_get_text(element):
    return element.get_text(strip=True) if element else ""


base_url = "http://aakashleap.com:3131"


def jsonify_data(valid_html, dump_file=False, fails=None, course='JEE'):
    
    if course == 'JEE':
        valid_psid_nos = [i['PSID'] for i in jee_psids]
    else:
        valid_psid_nos = [i['PSID'] for i in neet_psids]
    folder_path = valid_html
    students_data = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".html"):
            with open(
                os.path.join(folder_path, filename), "r", encoding="unicode_escape"
            ) as file:

                soup = BeautifulSoup(file, "lxml")

                PSID = safe_get_text(soup.select_one("td:-soup-contains('PSID:') + td"))

                student_info = {
                    "Student Name": safe_get_text(
                        soup.select_one("td:-soup-contains('Student Name:') + td")
                    ),
                    "Father's Name": safe_get_text(
                        soup.select_one("""td:-soup-contains("Father's Name:") + td""")
                    ),
                    "Course Name": safe_get_text(
                        soup.select_one("td:-soup-contains('Course Name:') + td")
                    ),
                    "Profile Picture": base_url
                    + soup.select_one('img[alt="Student Pic"]')["src"].lstrip("."),
                    "Remark Notice": safe_get_text(
                        soup.select_one("p:-soup-contains('Dear Student') + p")
                    ),
                    "PSID": PSID,
                    "Roll No.": safe_get_text(
                        soup.select_one("td:-soup-contains('Roll No:') + td")
                    ),
                    "Batch": safe_get_text(
                        soup.select_one("td:-soup-contains('Batch:') + td")
                    ),
                    "Score": {"Subjects": {}, "Total": {}},
                }

                score_table = soup.select_one(".score-analysis > table")
                rows = score_table.select("tr")[1:]

                for row in rows:
                    cols = row.select("td")
                    if len(cols) == 9:
                        subject_name = safe_get_text(cols[0])
                        if subject_name == "Total":
                            continue
                        student_info["Score"]["Subjects"][subject_name] = {
                            "Maximum Score": safe_get_text(cols[1]),
                            "Your Score": safe_get_text(cols[2]),
                            "%age of Marks": safe_get_text(cols[3]),
                            "Percentile": safe_get_text(cols[4]),
                            "Average Score": safe_get_text(cols[5]),
                            "Topper Score": safe_get_text(cols[6]),
                            "Subject Rank": safe_get_text(cols[7]),
                            "Highest Score (Subject Wise)": safe_get_text(cols[8]),
                        }

                total_row = rows[-1]
                total_cols = total_row.select("td")

                student_info["Score"]["Total"] = {
                    "Maximum Score": safe_get_text(total_cols[1]),
                    "Your Score": safe_get_text(total_cols[2]),
                    "%age of Marks": safe_get_text(total_cols[3]),
                    "Percentile": safe_get_text(total_cols[4]),
                    "Average Score": safe_get_text(total_cols[5]),
                    "Topper Score": safe_get_text(total_cols[6]),
                    "Highest Score (Subject Wise)": safe_get_text(total_cols[8]),
                }
                # print(student_info,valid_psid_nos)
                # if student_info["PSID"] not in valid_psid_nos:
                #     continue
                students_data.append(student_info)

    sorted_data = sorted(students_data, key=lambda x: x["Student Name"])


    if dump_file:
        with open(dump_file, "w", encoding="utf-8") as json_file:
            json.dump({"data": sorted_data,"fails": fails}, json_file, ensure_ascii=False, indent=2)

    return sorted_data
