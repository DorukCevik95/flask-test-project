from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Doruk Çevik!</h1>'
@app.route("/bilgiler")
def bilgi():
    bilgiler = ["Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.", "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.", "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."]
    return '<p>' + random.choice(bilgiler) + '</p>'
app.run(debug=True)
