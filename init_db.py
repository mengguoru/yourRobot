import pickle
data = {
    'aa':'blabla',
}
if __name__ == '__main__':
    with open('data.pkl','wb') as db:
        pickle.dump(data,db)