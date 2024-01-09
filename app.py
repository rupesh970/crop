from flask import Flask, render_template,jsonify,request

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/prediction',methods = ['Get','Post'])
def prediction():
    if request.method=='POST':
        nitro = request.form.get('nitrogen')
        phos = request.form.get('phosphorus')
        kp = request.form.get('potassium')
        temp = request.form.get('temperature')
        hum = request.form.get('humidity')
        ph = request.form.get('ph')
        rain = request.form.get('rainfall')
        print(nitro,phos,kp,temp,hum,ph,rain)
    else:
        return render_template('prediction.html')

    return render_template('prediction.html')




if _name=='__main__':
    app.run()