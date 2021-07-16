from flask import Flask, render_template

app = Flask(__name__)

@app.route('/words/<string:w>')

def words(w):
    f = open ('words.txt')
    word_list = f.read().splitlines()
    
    l=[]
    w1=w.upper()
    
    for word in word_list:
        if sorted (w1) == sorted (word):
            l.append(word)
        
        
    return render_template ('anagrams.html', list=l)
