import os


def write_valid(all_html, valid_html):
    fails = []
    for i in os.listdir(all_html):
        if i.endswith(".html"):
            with open(os.path.join(all_html, i), "r") as f:
                data = f.read()
                if not "Student Performance Report" in data:
                    roll_no = i.split("roll_N-")[1].split(".html")[0]
                    fails.append(roll_no)
                    continue
                else:
                    with open(os.path.join(valid_html, i), "w") as f:
                        f.write(data)
                        f.close()
    return fails
