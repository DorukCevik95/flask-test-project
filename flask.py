from flask import Flask
import random
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Text!</h1>'

@app.route("/bilgiler")
def bilgi():
    bilgiler = [
        "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
        "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
        "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
    ]
    return '<p>' + random.choice(bilgiler) + '</p>'

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@app.route("/secret")
def pics():
    image_url = get_duck_image_url()
    return (
        '<h2>Bunlara bir göz atın!</h2>'
        '<img src="' + image_url + '" alt="Ördek" width="400">'
    )

if __name__ == "__main__":
    app.run(debug=True)
