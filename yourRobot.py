'''
Your robot.Train it to answer your quesions :)

author : mengguoru
date   : 2016/03/28
'''
import pickle
if __name__ == '__main__':
    with open('data.pkl','rb') as db:
        data = pickle.load(db)
    print(
        '''
        Your robot.Train it to answer your quesions :)

        Press
            q  quit,
            s  show data
        '''
    )
    while True:
        request = input('say to robot:')
        if request in data:
            print(data[request])
        elif request == 'q':
            break
        elif request == 's':
            print(data)
        else:
            print('this question not exist')
            answer = input('input your training answer')
            data[request] = answer
    with open('data.pkl','wb') as db:
        pickle.dump(data,db)