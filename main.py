from datetime import datetime,date


x = '2021-09-16T13:45:57.000Z'

def isototimestamp():
    y=datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ')
    z= datetime(datetime.today().year, 1, 1)
    if y > z:
        print(y)
    else:
        print(z)

if __name__ == '__main__':
    isototimestamp()

