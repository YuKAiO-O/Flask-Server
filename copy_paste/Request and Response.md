### Page 18
============================================================================
```python
@app.route("/item/<id>")
def item(id):
    return f"{id}"

@app.route("item_num/<int:id>")
def item_num(id):
    return f"{id}"
```

### Page 19
============================================================================
```python
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<int:id>")
def show_id(id):
    return f"<p>Hello, {id}</p>"
```

### Page 20
============================================================================
```python
@app.route("/add_new_item", methods=["POST", "GET"])
def add_new_item():
    if request.method == "GET":
        return "This is get method."
    if request.method == "POST":
        data = request.get_data()
        return f"{data}"
    return "none"
```

### Page 21
============================================================================
```python
@app.route("/post_data", methods=["POST"])
def post_data():
    return request.get_data()
```

curl -X POST -d "Oh This is COOL" 127.0.0.1:5000/post_data
curl -X POST -d "username=admin, password=2024" 127.0.0.1:5000/post_data

### Page 22
============================================================================
```python
@app.route("/post_json", methods=["POST"])
def post_json():
    return request.get_json()
```

curl -X POST -H "Content-Type:application/json" -d @test.json 127.0.0.1:5000/post_json

### Page 23
============================================================================
```python
@app.route("/look_request")
def look_request():
    print(request.args)
    print(request.method)
    print(request.host)
    return "ok"
```

curl -X GET 127.0.0.1:5000/look_request?params=1234

### Page 24
============================================================================
```python
SRC_PATH =  pathlib.Path(__file__).parent.absolute()
UPLOAD_FOLDER = os.path.join(SRC_PATH,  'static', 'uploads')
file = request.files["image"]
image = ""
if file.filename != '':
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    image = url_for("static", filename=f"uploads/{file.filename}")
```

### Page 25
============================================================================
```python
@app.route("/")
def home():
    return "This is Home Page."

@app.route("/return_home")
def return_home():
    return redirect(url_for("home"))
```

### Page 26
============================================================================
```python
@app.errorhandler(404)
@app.errorhandler(500)
def error(e):
    return make_response(
       "Page not Found", {'Content-Type': 'text/plain'}
    )
```