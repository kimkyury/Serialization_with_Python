from factory.object import *  #얘를 통해서 contol도 상속받음
from factory.jsonControl import *
from factory.pickleControl import *
import pickle

def select_format() : #형식을 지정하는 함수
    form_flag = input("엑셀로 진행:1, Json으로 진행:2, Pickle로 진행:3 \n선택해주세요: ")
    return form_flag


if __name__ == "__main__":  # 프로젝트 실행과 함께 시작

    act_flag = int(input("새 파일 생성하기:1, 이전 파일 추가하기:2, 파일 확인하기:3 \n선택해주세요: "))
    form_flag = int(select_format())

    #새파일 제작
    if ((act_flag ==1) and (form_flag == 1)):   #엑셀로
        IPmans = faker_generator()  # Fake 인간 생성
        wb = xl.create_excel() # 기본엑셀파일 생성.  (def from excelControl.py)import object.py에서 control.py를 끌고왔음
        xl.set_Ipmans(wb['data'], IPmans) # 만든 xlsx에 fake담기 (def from excelControl.py)
        xl.save_excel(wb) #만든 엑셀파일 지정경로로 저장

    elif ((act_flag ==1) and (form_flag == 2)):   # 새파일을 JSON으로
        IPmans = faker_generator() # Fake 인간 생성
        data = set_Ipman(IPmans)# Fake리스트를 dic형식으로 변환
        create_json_file(data) #json파일저장

    elif ((act_flag ==1) and (form_flag == 3)):   #Pickle로
        IPmans = faker_generator() # Fake 인간 생성
        save_pickle(IPmans) #피클파일 저장



    #이전 파일 추가
    elif (act_flag ==2 and form_flag == 1):   #엑셀로
        print("수정중")
    elif (act_flag ==2 and form_flag == 2):   #JSON으로
        print("수정중")
    elif (act_flag ==2 and form_flag == 3):   #Pickle로
        print("수정중")



    #파일 확인
    elif ((act_flag ==3) and (form_flag == 1)):   # 확인을 엑셀로
        title=input("찾는 엑셀파일명을 입력해주세요: ")
        wb = xl.load_workbook('./result/' + title + '.xlsx')
        count = xl.get_Count_Ipmans(wb['data'])
        IPmans = serialization(xl.get_data(wb['data'], count))
        show_whole(IPmans)

    elif (act_flag ==3 and form_flag == 2):   # 확인을 JSON으로
        title=input("찾는 json파일명을 입력해주세요: ")
        with open('./result/' + title + '.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        IPmans = serialization(data)
        show_whole(IPmans)

    elif (act_flag ==3 and form_flag == 3):   # 확인을 Pickle로
        title=input("찾는 피클파일명을 입력해주세요: ")
        with open('./result/'+ title + '.pickle', 'rb') as f:
            data = pickle.load(f)
        show_whole(data)
        
        
        
    else:
        print("재실행 후, 번호를 하나씩만 골라주세요. ")
    