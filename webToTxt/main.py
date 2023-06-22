import requests, os, sys, threading
from bs4 import BeautifulSoup

session = requests.Session()

url = 'https://diemthi.hcm.edu.vn/Home/Show'

def get_score(indicator, min, max):
    exe_dir = os.path.dirname(sys.argv[0])
    file_path = os.path.join(exe_dir, f'result{indicator}.txt')
    for i in range(min, max):
        sbd = str(i)
        r = requests.post(url, data={'SoBaoDanh': sbd}, allow_redirects=True)
        soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
        result = soup.find('table')
        if result != None:
            name = result.find('tr').findNext('tr').find('td').text
            score = result.find('tr').findNext('tr').find('td').find_next_sibling('td').text
            if indicator == 9: print(sbd)
            with (open(file_path, 'a', encoding='utf-8')) as f:
                for t in [name, score]:
                    f.write(t.replace('  ',' ').replace('  ','').replace('\n',''))

try:
    # first = 93309
    # last = 93310
    # for l in range(1, 31):
    threading.Thread(target=get_score, args=(3, 96453, 99763)).start()
    # first += 3310
    # last += 3310
except:
    print("Error: unable to start thread")
