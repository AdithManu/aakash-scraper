# import json


# def print_rank(json_data):
#     student_scores = []
#     for student in json_data:
#         name = student['Student Name']
#         score = float(student['Score']['Total']['Your Score'])
#         percentage = float(student['Score']['Total']['%age of Marks'])
#         student_scores.append((name, score, percentage))

#     student_scores.sort(key=lambda x: x[1], reverse=True)

#     header = (f"#   {'Name':<30}{'Score':>6}\t{'Percentage':>5}")
#     print(header)
#     print("-" * 60)

#     for i, (name, score, percentage) in zip(range(len(json_data)),student_scores):
#         print(f"{f'{(i+1):01d}':<4}{name:<30}{score:>6.2f}\t{percentage:>5.2f}")
import json


# def print_rank(json_data, course='JEE'):
#     student_scores = []
#     for student in json_data:
#         name = student['Student Name']
#         physics_score = float(student['Score']['Subjects']['Physics']['Your Score'])
#         chemistry_score = float(student['Score']['Subjects']['Chemistry']['Your Score'])
        
#         maths_score = float(student['Score']['Subjects']['Maths']['Your Score'])
#         total_score = float(student['Score']['Total']['Your Score'])
#         percentage = float(student['Score']['Total']['%age of Marks'])
#         student_scores.append((name, physics_score, maths_score, chemistry_score, total_score, percentage))

#     student_scores.sort(key=lambda x: x[4], reverse=True)  # Sort by total score

#     header = (f"#   {'Name':<28}  {'Phy':>8} {'Math':>8} {'Chem':>8}     {'Total Score':>12} {'Percentage':>12}")
#     print(header)
#     print("-" * 90)

#     for i, (name, physics, maths, chemistry, total, percentage) in zip(range(len(json_data)), student_scores):
#         print(f"{f'{(i+1):01d}':<4}{name:<30} {physics:>8.2f} {maths:>8.2f} {chemistry:>8.2f} {total:>12.2f} {percentage:>12.2f}")



import json
import re

def extract_ranks(remark_notice):
    # Extract Centre Rank and total students
    centre_rank_pattern = r"Centre\s+Rank\s+is\s+(\d+)\s+out\s+of\s+(\d+)"
    centre_match = re.search(centre_rank_pattern, remark_notice, re.DOTALL)
    
    # Extract AIR and total students
    air_pattern = r"AIR\s+is\s+(\d+)\s+out\s+of\s+(\d+)"
    air_match = re.search(air_pattern, remark_notice, re.DOTALL)
    
    results = {}
    
    if centre_match:
        results['centre_rank'] = int(centre_match.group(1))
        results['centre_total'] = int(centre_match.group(2))
    
    if air_match:
        results['air_rank'] = int(air_match.group(1))
        results['air_total'] = int(air_match.group(2))
    
    return results

def print_rank(json_data, course='JEE'):
    student_scores = []
    for student in json_data:
        # print(student)
        name = student['Student Name']
        physics_score = float(student['Score']['Subjects']['Physics']['Your Score'])
        chemistry_score = float(student['Score']['Subjects']['Chemistry']['Your Score'])
        total_score = float(student['Score']['Total']['Your Score'])
        percentage = float(student['Score']['Total']['%age of Marks'])
        
        if course == 'JEE':
            math_score = float(student['Score']['Subjects']['Maths']['Your Score'])
            remark_notice = extract_ranks(student['Remark Notice'])
            
            student_scores.append((name, physics_score, math_score, chemistry_score, total_score, percentage, remark_notice, "JEE"))
        elif course == 'NEET':
            botany_score = float(student['Score']['Subjects']['Botany']['Your Score']) 
            zoology_score = float(student['Score']['Subjects']['Zoology']['Your Score']) 
            student_scores.append((name, physics_score, botany_score, zoology_score, chemistry_score, total_score, percentage, "NEET"))

    student_scores.sort(key=lambda x: x[4] if x[-1] == "JEE" else x[5], reverse=True)

    jee_students = [s for s in student_scores if s[-1] == "JEE"]
    neet_students = [s for s in student_scores if s[-1] == "NEET"]
    
    if jee_students:
        print("=== JEE STUDENTS ===")
        header = (f"#   {'Name':<30}{'  Physics':>8} {'Maths ':>8}{'   Chemistry':>12}  {'Total Score':>12}{'Percentage':>12}   |{'Rank':>15}")
        print(header)
        print("-" * 120)
        
        for i, (name, physics, math, chemistry, total, percentage, rank, _) in enumerate(jee_students):
            center_rank = f"{rank['centre_rank']}/{rank['centre_total']}"
            air_rank = f"{rank['air_rank']}/{rank['air_total']}"
            rank_text=f'C: {center_rank:<8} A: {air_rank:<8}'
            print(f"{f'{(i+1):01d}':<4}{name:<30}{physics:>8.2f} {math:>8.2f}{chemistry:>12.2f}{total:>12.2f}{percentage:>12.2f}      |   {rank_text:<20}")
    
    if neet_students:
        print("\n=== NEET STUDENTS ===")
        header = (f"#   {'Name':<30}{'Physics':>8}  {'Botany':>8}{'Zoology':>10} {'Chemistry':>12}{'Score  ':>12}{'   Percentage':>12}")
        print(header)
        print("-" * 100)
        
        for i, (name, physics, botany, zoology, chemistry, total, percentage, _) in enumerate(neet_students):
            print(f"{f'{(i+1):01d}':<4}{name:<30}{physics:>8.2f}  {botany:>8.2f}{zoology:>10.2f}{chemistry:>12.2f}{total:>12.2f}{percentage:>12.2f}")