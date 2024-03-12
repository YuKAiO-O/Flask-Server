from flask import Flask, request, redirect, url_for, render_template, make_response
from database import db, Product
import random, pathlib, os

app = Flask(__name__)

# 取得目前檔案所在的資料夾 
SRC_PATH =  pathlib.Path(__file__).parent.absolute()
# 結合目前的檔案路徑和 static 及 uploads 路徑 
UPLOAD_FOLDER = os.path.join(SRC_PATH,  'static', 'uploads')

# sqlalchemy 的其他設定
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{ os.path.join(basedir, 'database.db') }"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.extensions["db"] = db

@app.route("/")
def home():
    query_result = Product.query.all()
    items = []
    for query in query_result:
        items.append({
            "id": query.id,
            "image": query.image,
        })
    return render_template("pages/home.html", items=items, data={})

@app.route("/add_new_item", methods=["POST", "GET"])
def add_new_item():
    if request.method == "GET":
        return render_template("pages/add_new_item.html")
    if request.method == "POST":
        form_data = request.form
        id = random.randint(1, 100)
        file = request.files["image"]
        image = ""
        if file.filename != '':
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            image = url_for("static", filename=f"uploads/{file.filename}")
        product = Product(  
                            id, 
                            form_data.get("title"), 
                            form_data.get("content"), 
                            image,
                            form_data.get("alt")
                        )
        db.session.add(product)
        db.session.commit()

        return redirect(url_for("home"))
    return "failed"

@app.route("/item/<id>")
def item(id):
    query = Product.query.filter_by(id=id).first()
    if query != None:
        item = {
            "title": query.title,
            "content": query.content,
            "image": query.image,
            "alt": query.alt
        }
        return render_template("pages/item.html", item=item)
    else:
        return "failed"

@app.errorhandler(404)
@app.errorhandler(500)
def error(e):
    return make_response(
       "Page not Found", {'Content-Type': 'text/plain'}
    )