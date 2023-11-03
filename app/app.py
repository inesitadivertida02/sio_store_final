from detishop import app

if __name__ == "__main__":
    app.secret_key="#v%DHrsdepn4t+(ZU8Gq"
    app.debug = True
    app.run(host='0.0.0.0', port=8001)