from openpyxl import *
import os

def init_Ipmans(sheet):    #엑셀의 변하지 않는 기본 값을 지정함
    sheet['A1'].value = 'Name'
    sheet['B1'].value = 'Address'
    sheet['C1'].value = 'IP'
    return sheet


def set_Ipmans(sheet, IPmans, start=2): #엑셀에 정보를 저장하고, 저장한 내용을 리턴시킴
    for i in range(start, start+len(IPmans)):
        sheet['A' + str(i)] = IPmans[i-start].name 
        sheet['B' + str(i)] = IPmans[i-start].address
        sheet['C' + str(i)] = IPmans[i-start].ip
    return sheet


def get_data(sheet, cnt): #엑셀에서 정보를 읽어와 각 항목을 딕셔녀리 형태로 추가함, 해당 딕셔너리 정보를 리스트 형태로 반환
    data = []
    for i in range(2, cnt+2):
        ipman = {
            'name'      : sheet['A' + str(i)].value,
            'address'   : sheet['B' + str(i)].value,
            'ip'        : sheet['C' + str(i)].value
        }
        data.append(ipman)
    return data


def get_Count_Ipmans(sheet): #엑셀에서 존재하는 인원의 수를 읽어오고 인원수 반환
    count = 1
    while (sheet['A' + str(count)].value is not None) :
        count+=1
    return count-2


def create_excel(): #엑셀 기본 파일을 만들어서(워크북, 시트, 시트이름, 시트기본설정(함수)) 내보냄.
    wb = Workbook()
    sheet = wb.active
    sheet.title = 'data'
    sheet = init_Ipmans(sheet)
    return wb


def save_excel(wb): #엑셀파일을 저장함
    # result 폴더가 없다면 만든다.
    if os.path.isdir('result') is False:  
        os.mkdir('result')
    # result 폴더에 저장
    title = input('저장할 파일이름을 입력해주세요:')
    wb.save('./result/' + title+ '.xlsx')
    print('생성완료')