import json


def print_rank(json_data):
    student_scores = []
    for student in json_data:
        name = student['Student Name']
        score = float(student['Score']['Total']['Your Score'])
        percentage = float(student['Score']['Total']['%age of Marks'])
        student_scores.append((name, score, percentage))

    student_scores.sort(key=lambda x: x[1], reverse=True)

    header = (f"#   {'Name':<30}{'Score':>6}\t{'Percentage':>5}")
    print(header)
    print("-" * 60)

    for i, (name, score, percentage) in zip(range(len(json_data)),student_scores):
        print(f"{f'{(i+1):01d}':<4}{name:<30}{score:>6.2f}\t{percentage:>5.2f}")
