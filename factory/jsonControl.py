import json
import os

def generate_json(data): # json파일 제작
    res = json.dumps(data, indent=4, ensure_ascii=False)
    return res

def set_Ipman(ipmans): #ipmans리스트를 딕셔너리로 변환 후 저장
    data=[]
    for i in ipmans:
        ipman= {
            'name' : i.name,
            'address' : i.address,
            'ip' : i.ip
        }
        data.append(ipman)
    return data

def create_json_file(data): #json파일 저장
    if os.path.isdir('result') is False:
        os.mkdir('result')
    title = input('저장할 파일이름을 입력해주세요:')
    with open('./result/' + title + '.json', 'w', encoding='utf-8') as f: #해당경로에, 쓰기모드로, 인코딩 설정
        json.dump(data, f,  ensure_ascii=False, indent=4)
    

