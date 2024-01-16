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

directory = "data"
file_count = 0
total_sum = 0
subject_sums = {}

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        html_file = os.path.join(directory, filename)

        # ファイルから数値を抽出し、それらの数値を合計
        numbers = extract_numbers_from_html(html_file)
        file_sum = sum(numbers)
        total_sum += file_sum

        print(f"{file_sum} \t分: {filename}")

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
    print(f"{sum}\t分: {subject}")

print(f"\n全教科合計時間\n {total_sum}分")