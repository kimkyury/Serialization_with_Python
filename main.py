from factory.object import *  #얘를 통해서 contol도 상속받음

def select_format() : #형식을 지정하는 함수
    form_flag = input("엑셀로 진행:1, Json으로 진행:2, Pickle로 진행:3 \n선택해주세요: ")
    return form_flag


if __name__ == "__main__":  # 프로젝트 실행과 함께 시작
     #무작위의 이름을 담을 공간 생성 (faker은 object에서 가져옴)
    
    act_flag = int(input("새 파일 생성하기:1, 이전 파일 수정하기:2, 파일 확인하기:3 \n선택해주세요: "))
    form_flag = int(select_format())

    if ((act_flag ==1) and (form_flag == 1)):   # 새파일을 엑셀로
        IPmans = faker_generator()  # Fake 인간 생성
        wb = xl.create_excel() # 기본엑셀파일[A1, B1, C1]만듦.  (def from excelControl.py)import object.py에서 control.py를 끌고왔음
        xl.set_Ipmans(wb['data'], IPmans) # 만든 엑셀파일 저장 (def from excelControl.py)






    elif (act_flag ==1 and form_flag == 2):   # 새파일을 JSON으로
        print("수정중")
    elif (act_flag ==1 and form_flag == 3):   # 새파일을 Pickle로
        print("수정중")


    elif (act_flag ==2 and form_flag == 1):   # 수정을 엑셀로
        print("수정중")
    elif (act_flag ==2 and form_flag == 2):   # 수정을 JSON으로
        print("수정중")
    elif (act_flag ==2 and form_flag == 3):   # 수정을 Pickle로
        print("수정중")


    elif (act_flag ==3 and form_flag == 1):   # 확인을 엑셀로
        print("수정중")
    elif (act_flag ==3 and form_flag == 2):   # 확인을 JSON으로
        print("수정중")
    elif (act_flag ==3 and form_flag == 3):   # 확인을 Pickle로
        print("수정중")
        
    else:
        print("재실행 후, 번호를 하나씩만 골라주세요. ")
    