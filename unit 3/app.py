from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Welcome to Planet Earth!"
    
    text = """Earth is the third planet from the Sun. About 29.2% of Earth's surface is land consisting of continents and islands. 
    There are seven continents on planet Earth: Africa, Antarctica, Asia, Australia, Europe, North America and South America."""

    choices = [
        ('africa',"Africa"),
        ('antarctica',"Antarctica"),
        ('asia', "Asia"),
        ('australia',"Australia"),
        ('europe',"Europe"),
        ('northamerica',"North America"),
        ('southamerica', "South America")

    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/africa")
def africa():
    title = "Welcome to Africa!"
    
    text = """Africa is the Earth's second-largest and second-most populous continent, after Asia. 
    At about 30.3 million km² including adjacent islands, it covers 6% of Earth's total surface area and 20% of its land area. 
    With ~1.3 billion people, it accounts for about 16% of the world's human population."""

    choices = [
        ('start',"Go to next continent"),
        ('next',"Depart Earth. Explore next planet")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/antarctica")
def antarctica():
    title = "Welcome to Antarctica!"
    
    text = """Antarctica, the southernmost continent and site of the South Pole, is a virtually uninhabited, ice-covered landmass.  
    The peninsula’s isolated terrain also shelters rich wildlife, including many penguins."""

    choices = [        
        ('start',"Go to next continent"),
        ('next',"Depart Earth. Explore next planet")
        ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/asia")
def asia():
    title = "Welcome to Asia!"
    
    text = """Asia is Earth's largest and most populous continent, located primarily in the Eastern and Northern Hemispheres. 
    It shares the continental landmass of Eurasia with the continent of Europe and the continental landmass of Afro-Eurasia with both Europe and Africa."""

    choices = [
        ('start',"Go to next continent"),
        ('next',"Depart Earth. Explore next planet")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/australia")
def australia():
    title = "Welcome to Australia!"
    
    text = """Australia, officially the Commonwealth of Australia, is a sovereign country comprising the mainland of the Australian continent, the island of Tasmania, and numerous smaller islands. 
    It is the largest country in Oceania and sixth-largest country on Earth."""

    choices = [
        ('start',"Go to next continent"),
        ('next',"Depart Earth. Explore next planet")
    ]
    

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/europe")
def europe():
    title = "Welcome to Europe!"
    
    text = """Europe is a continent located entirely in the Northern Hemisphere and mostly in the Eastern Hemisphere."""

    choices = [
        ('start',"Go to next continent"),
        ('next',"Depart Earth. Explore next planet")
]
    

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/northamerica")
def northamerica():
    title = "Welcome to North America!"
    
    text = """North America is a continent entirely within the Northern Hemisphere and almost all within the Western Hemisphere."""

    choices = [
        ('start',"Go to next continent"),
        ('next',"Depart Earth. Explore next planet")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/southamerica")
def southamerica():
    title = "Welcome to South America!"
    
    text = """South America is a continent entirely in the Western Hemisphere and mostly in the Southern Hemisphere, with a relatively small portion in the Northern Hemisphere."""

    choices = [
        ('start',"Go to next continent"),
        ('next',"Depart Earth. Explore next planet")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/nextplanet")
def next():
    title = "Next planet in Solar system is Mars!"
   
    text = """Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, 
    being larger than only Mercury. Our journey will take 5 days."""

    choices = [
        ]

    return render_template('adventure.html', title=title, text=text, choices=choices)
