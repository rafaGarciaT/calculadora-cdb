from datetime import datetime


def date_info():
    d = datetime.today().day
    m = datetime.today().month
    a = datetime.today().year
    h = datetime.today().hour
    mn = datetime.today().minute
    s = datetime.today().second
    return {'d': d, 'm': m, 'a': a, 'h': h, 'mn': mn, 's': s}
