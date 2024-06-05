
def gen_secs():
    seconds = 0
    while True:
        yield seconds
        seconds += 1
        if seconds==60:
            seconds = 0

def gen_minutes():
    mins = 0
    while True:
        yield mins
        mins += 1
        if mins==60:
            mins = 0

def gen_hours():
    hours = 0
    while True:
        yield hours
        hours += 1
        if hours==23:
            hours = 0


def gen_time():
    gensecs = gen_secs()
    genmins = gen_minutes()
    genhours = gen_hours()
    sec = 0
    min = next(genmins)
    hour = next(genhours)
    while True:
        if sec == 59:
            sec = next(gensecs)
            if min == 59:
                min = next(genmins)
                hour = next(genhours)
            else:
                min = next(genmins)
        else:
            sec = next(gensecs)
        yield f"{hour:02}:{min:02}:{sec:02}"

def gen_years(start=2019):
    while True:
        yield start
        start+=1


def gen_months():
    month = 1
    while True:
        yield month
        month += 1
        if month == 13:
            month = 1



def gen_days(month,leap_year=True):
    maxDays = 27
    if month in [1,3,5,7,8,10,12]:
        maxDays = 31
    elif month in [4,6,9,11] :
        maxDays = 30
    elif leap_year:
        maxDays=29
    else:
        maxDays = 28

    day = 1
    while True:
        yield day
        day+=1
        if day > maxDays:
            day = 1


def isYearLeap(year):
    if year%4==0 and not year%100!=0:
        return True
    elif year%4==0 and year%100==0 and year%1000==0:
        return True
    else:
        return False
def gen_date():
    genTime = gen_time()
    genYear = gen_years()
    genMonths = gen_months()
    month = next(genMonths)
    year = next(genYear)
    isLeap = isYearLeap(year)
    genDays = gen_days(1, isLeap)
    day = next(genDays)
    time = next(genTime)
    while True:
        yield f"{day:02}/{month:02}/{year:04} {time}"
        time = next(genTime)
        if time == "00:00:00":
            day = next(genDays)
            if day == 1:
                month = next(genMonths)
                if month == 1:
                    year = next(genYear)
                    isLeap = isYearLeap(year)
                else:
                    genDays = gen_days(month, isLeap)

def dateIteration(genDate):
    while True:
        yield next(genDate)
        for i in range(0,1000000):
            next(genDate)


def __main__():
    genDate = gen_date()
    afterEachIteration = dateIteration(genDate)
    while True:
         print(next(afterEachIteration))


if __name__ == '__main__':
    __main__()