# i know it is dumb to convert to txt then to json, but i'm lazy to change the code
# and it works so i don't care

import sys, os, json

exe_dir = os.path.dirname(sys.argv[0])
read_path = os.path.join(exe_dir, f'result_all.txt')
write_path = os.path.join(exe_dir, f'diemthi.json')

with (open(read_path, 'r', encoding='utf-8')) as f:
    data = {}
    while True:
        name = f.readline()
        if not name: break
        sbd = name[:name.index('_')]
        print(sbd)
        name = name[name.index('_') + 1 : len(name)].replace('\n', '').lower().title()
        score = f.readline()
        litScore = score[score.index("Văn: "):score.index("Toán")].replace("Văn: ", '').replace(" ", '')
        mathScore = score[score.index("Toán: "):score.index("Ngoại Ngữ")].replace("Toán: ", '').replace(" ", '')
        engScore = score[score.index("Ngoại Ngữ: "):score.index("Môn Chuyên")].replace("Ngoại Ngữ: ", '').replace(" ", '')
        speScore = score[score.index("Môn Chuyên: "):].replace("Môn Chuyên: ", '').replace(" ", '').replace('\n', '')

        if litScore == '': litScore = '0'
        if mathScore == '': mathScore = '0'
        if engScore == '': engScore = '0'
        if speScore == '': speScore = '0'

        litScore = float(litScore)
        mathScore = float(mathScore)
        engScore = float(engScore)
        speScore = float(speScore)

        totalScore = litScore + mathScore + engScore
        totalSpeScore = totalScore + speScore*2

        student_data = {
            'Họ và Tên': name,
            'Điểm thi từng môn' : {
                'Ngữ Văn': litScore,
                'Toán': mathScore,
                'Ngoại Ngữ': engScore,
                'Môn Chuyên': speScore,
            },
            'Tổng điểm': {
                'Không chuyên': totalScore,
                'Chuyên': totalSpeScore 
            }
        }

        data[sbd] = student_data

with (open(write_path, 'a', encoding='utf-8')) as w:
    json.dump(data, w, ensure_ascii=False, indent=4)

    