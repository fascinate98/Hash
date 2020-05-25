
def getHash(msg):
    intmsg = convert_to_ascii(msg)
    val = int(intmsg) / 23
    a = str(val).split('.')
    b = a[1]
    hashval = b[6:10]
    print("--------------------debug----------------------")
    print("메세지를 int로 변환 : " + str(intmsg))
    print("메세지를 23으로 나눈 값 : " + str(val))
    print("소숫점 기준으로 split" + str(a))
    print("소수 부분만 출력" + str(b))
    print("7~10번쨰 자리 출력" + str(hashval))

    return str(hashval)

def convert_to_ascii(text):
    return "".join(str(ord(char)) for char in text)

