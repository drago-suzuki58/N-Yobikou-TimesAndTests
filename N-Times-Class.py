import os
import re

def extract_numbers_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    pattern = r'(\d+)分'
    numbers = re.findall(pattern, html_content)

    # 数値の文字列を整数に変換
    numbers = [int(number) for number in numbers]

    return numbers

def convert_minutes_to_dhms(minutes):
    days = minutes // (24 * 60)
    hours = (minutes % (24 * 60)) // 60
    minutes = (minutes % (24 * 60)) % 60
    return f"{days}:{hours:02d}:{minutes:02d}:00"

directory = "data"
file_count = 0
total_sum = 0
subject_sums = {}

if not os.path.exists(directory):
    os.makedirs(directory)

print("\033[32m授業動画時間\033[0m")

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        html_file = os.path.join(directory, filename)

        # ファイルから数値を抽出し、それらの数値を合計
        numbers = extract_numbers_from_html(html_file)
        file_sum = sum(numbers)
        total_sum += file_sum

        print(f"{convert_minutes_to_dhms(file_sum)} \t: {filename}")

        # 教科別の合計時間を計算
        subject = filename.split(" ")[0]
        if subject in subject_sums:
            subject_sums[subject] += file_sum
        else:
            subject_sums[subject] = file_sum

        file_count += 1

print(f"\n合計ファイル数: {file_count}")

# 教科別の合計時間を表示
print("\n教科別合計時間:")
for subject, sum in subject_sums.items():
    print(f"{convert_minutes_to_dhms(sum)}\t: {subject}")

print(f"\n全教科合計時間\n {convert_minutes_to_dhms(total_sum)}")
