#인간 생성, 데이터 직렬화, 출력하기 함수 존재


from faker import Faker  #가상 랜덤데이터
import factory.excelControl as xl # factory폴더의 control를 불러와서 x1로 이름 짓기 


class Ipman:  #만든 데이터를 출력시키기 위한 class
    def __init__(self, name, address, ip):
        self.name = name
        self.address = address
        self.ip = ip
    def show_data(self):
        print('name :', self.name)
        print('address :', self.address)
        print('ip :', self.ip)

def show_whole(Ipmans): #파일의 리스트를 보는 함수
    for i in Ipmans:
        i.show_data()



def faker_generator(cnt = 0): #초기값은 cnt=0, 가상의 인물을 개수만큼 만드는 함수
    #초기실행(새로만들기)인지 확인
    if cnt == 0:
        input('\n   만들어봅시다! enter를 누르세요!\n   ') # 가상환경 쓸 경우, 버퍼에 가상환경 주소가 남아 있는 것을 해결하기 위해
        cnt = input('생성 갯수는 얼마인가요? (숫자만 입력)> ')
    
    #해당 개수만큼 생성
    f = Faker('ko_KR')
    IPmans = []
    for i in range(int(cnt)):
        IPmans.append(Ipman(f.name(), f.address(), f.ipv4_private())) # 0~(cnt-1)까지의 index를 가짐

    #사람(이름,주소,IP) 들이 담긴 리스트 리턴
    return IPmans 



def serialization(data): #직렬화시킨 데이터의 리스트를 리턴
    IPmans = [] #정리된 데이터들을 담을 리스트
    for i in range(len(data)):
        ipman = Ipman(data[i]['name'], data[i]['address'], data[i]['ip'])
        IPmans.append(ipman)
    return IPmans










