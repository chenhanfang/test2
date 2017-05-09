import requests
# response=requests.get('https://api.github.com')
# dir(response)
# print(response.elapsed)

def download_image():
    url='http://f.hiphotos.baidu.com/zhidao/wh%3D600%2C800/sign=b51022cbe824b899de69713e5e3631ad/50da81cb39dbb6fdcf4eeded0824ab18962b37e7.jpg'
    reponse=requests.get(url,stream=True)
    with open('E:\\demo.jpg') as fd:
        for chunk in reponse.iter_content(128):
            fd.write(chunk)
    print(reponse.status_code)
    print(reponse.reason)
    print(reponse.headers)
    print(reponse.content)

download_image()