import re
from datetime import datetime, timedelta
import os


def extract_elements_from_html(html_file, tag):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    pattern = f"<{tag}>(.*?)</div>"
    elements = re.findall(pattern, html_content)

    return elements


def calculate_total_time(elements):
    total_time = timedelta()
    for element in elements:
        match = re.search(r'(\d+):\d{2}', element)
        if match is not None:
            time_str = match.group()
            time_obj = datetime.strptime(time_str, '%M:%S').time()
            total_time += timedelta(minutes=time_obj.minute, seconds=time_obj.second)

    return total_time


def format_time(total_time):
    total_days = total_time.days
    total_hours = total_time.seconds // 3600
    total_minutes = (total_time.seconds % 3600) // 60
    total_seconds = total_time.seconds % 60
    formatted_time = f"{total_days}:{int(total_hours):02}:{int(total_minutes):02}:{int(total_seconds):02}"

    return formatted_time


directory = "data"
tag = "div font-size=\"12px\" color=\"gray.darkness2\" class=\"sc-aXZVg iuHQbN\""

subject_times = {}
file_count = 0

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        html_file = os.path.join(directory, filename)
        elements = extract_elements_from_html(html_file, tag)
        total_time = calculate_total_time(elements)
        formatted_time = format_time(total_time)
        print(f"{formatted_time}\t: {filename}")

        subject = filename.split(" ")[0]
        if subject in subject_times:
            subject_times[subject] += total_time
        else:
            subject_times[subject] = total_time

        file_count += 1

print(f"\n合計ファイル数: {file_count}")

print("\n教科別合計時間")
for subject, total_time in subject_times.items():
    formatted_time = format_time(total_time)
    print(f"{formatted_time}\t : {subject}")

total_subject_time = sum(time.total_seconds() for time in subject_times.values())
total_subject_time = timedelta(seconds=total_subject_time)
formatted_total_subject_time = format_time(total_subject_time)
print(f"\n全教科合計時間\n{formatted_total_subject_time}")