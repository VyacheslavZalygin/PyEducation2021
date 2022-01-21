import sys

# проверяет, что это число или точка
def validate(char):
    try: 
        int(char)
        return True
    except: 
        return char == '.'

def validate_ip(ip):
    for char in ip:
        if not validate(char):
            return False
    ip = [x for x in ip.split()]
    if len(ip) != 4:
        return False
    for octet in ip:
        # проверка на наличие незначащих нулей
        if str(int(octet)) != octet:
            return False
        # проверка на вхождение в отрезок от 0 до 255
        if not (0 <= int(octet) <= 255):
            return False
    return True

ip = sys.stdin.read().strip()
print("OK" if validate_ip(ip) else "Invalid Address")