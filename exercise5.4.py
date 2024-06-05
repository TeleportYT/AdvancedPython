def check_id_valid(id_number):
    digits = [int(d) for d in str(id_number)]
    isEven = False
    sumD = 0
    for digit in digits:
        digit = (digit if not isEven else digit*2) + 9
        sumD += sum(int(d) for d in str(digit)) if digit > 9 else digit
        isEven = not isEven

    return sumD % 10 == 0


print(check_id_valid(123456780))
print(check_id_valid(123456782))

class IDIterator():
    def __init__(self,firstId):
        self._id = firstId

    def __iter__(self):
        return self

    def __next__(self):
        self._id += 1
        while not check_id_valid(self._id):
            if self._id == 999999999:
                raise StopIteration
            self._id+=1
        return self._id


def id_generator(id):
    while True:
        if check_id_valid(id):
            yield id
        id+=1


def __main__():
    id = int(input("Enter id for starter"))
    if input("Generator or Iterator? (gen/it)?") == "gen":
        idMaker = id_generator(id)
    else:
        idMaker = IDIterator(id)

    for i in range(0,10):
        print(next(idMaker))



if __name__ == '__main__':
    __main__()