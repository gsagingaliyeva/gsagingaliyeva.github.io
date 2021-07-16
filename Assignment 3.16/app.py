from flask import Flask, render_template

app = Flask(__name__)

@app.route("/fizzbuzz/<int:fizzbuzzto>")

def fizzbuzz(fizzbuzzto):
    l=[]
    n=1
    while n < fizzbuzzto:
        if n%3==0 and n%5==0:
            l.append("fizzbuzz")
        elif n%3==0:
            l.append("fizz")
        elif n%5==0:
            l.append("buzz")
        else:
            l.append(n)
        n=n+1
    
    return render_template ('fizzbuzz.html', numbers=l)
