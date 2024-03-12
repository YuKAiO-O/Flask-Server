### Page 29
============================================================================
```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
 
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    content = db.Column(db.String(120), unique=True)
    image = db.Column(db.String(200), unique=True)
    alt = db.Column(db.String(50), unique=True)

    def __init__(self, id=None, title=None, content=None, image=None, alt=None):
        self.id = id
        self.title = title
        self.content = content
        self.image = image
        self.alt = alt
```

### Page 31
============================================================================
```python
from database import db, Porduct
db.init_app(app)
app.extensions["db"] = db
```

### Page 32
============================================================================
```python
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{ os.path.join(basedir, 'database.db') }"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.extensions["db"] = db
```

### Page 34
============================================================================
```python
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
```

### Page 35
============================================================================
```python
product = Product(  
                    id, 
                    form_data.get("title"), 
                    form_data.get("content"), 
                    image,
                    form_data.get("alt")
                )
db.session.add(product)
db.session.commit()
```

### Page 36
============================================================================
```python
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
```