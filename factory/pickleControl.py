from factory.object import *  #얘를 통해서 contol도 상속받음
from factory.jsonControl import *
import pickle


def save_pickle(IPmans) :
        if os.path.isdir('result') is False:
                os.mkdir('result')
        title = input('저장할 파일이름을 입력해주세요:')
        with open('./result/' + title + '.pickle', 'wb') as f:
            pickle.dump(IPmans, f, pickle.HIGHEST_PROTOCOL)
        print('생성완료')
       