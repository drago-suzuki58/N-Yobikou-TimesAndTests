import os
import re

def extract_elements_from_html(html_file, tag):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    pattern = f"<{tag}>(.*?)</div>"
    elements = re.findall(pattern, html_content)

    return elements

def calculate_problem_count(elements):
    return len(elements)

directory = "data"
tag = "div font-size=\"1.2rem\" color=\"gray.darkness2\" class=\"sc-aXZVg iFkSEV\""

subject_problems = {}
file_count = 0

if not os.path.exists(directory):
    os.makedirs(directory)

print("\033[32m問題数\033[0m")

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        html_file = os.path.join(directory, filename)
        elements = extract_elements_from_html(html_file, tag)
        problem_count = calculate_problem_count(elements)
        print(f"{problem_count}\t: {filename}")

        subject_name = filename.split(" ")[0]
        if subject_name not in subject_problems:
            subject_problems[subject_name] = problem_count
        else:
            subject_problems[subject_name] += problem_count

        file_count += 1

print(f"\n合計ファイル数: {file_count}")

print("\n教科別問題数")
for subject, problem_count in subject_problems.items():
    print(f"{problem_count}\t: {subject}")

total_subject_problems = sum(subject_problems.values())
print(f"\n全教科合計問題数\n{total_subject_problems}")