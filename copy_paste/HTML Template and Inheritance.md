### Page 11
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css')}}"/>
</head>
<body>
    {{ data }}
</body>
</html>
```

### Page 12
```html
<div class="gallery">
    {% for item in items %}
    <a href="/item/{{ item.id }}">
        <img src={{ item.image }} alt="{{ item.alt }}" width="200" height="200">
    </a>
    {% endfor %}
</div>
<a href="/add_new_item"><button>Add New Item</button></a>
```

### Page 13
```python
@app.route("/")
def home():
    data = "This is Testing"
    return render_template("base.html", data=data)
```

### Page 14
templates/base.html
```html
<body>
    {% block content %}
    {% endblock %}
</body>
```

templates/pages/home.html
```html
{% extends "base.html" %}
{% block content %}
<div class="gallery">
    {% for item in items %}
    <a href="/item/{{ item.id }}">
        <img src={{ item.image }} alt="{{ item.alt }}" width="200" height="200">
    </a>
    {% endfor %}
</div>
<a href="/add_new_item"><button>Add New Item</button></a>
{% endblock %}
```

### Page 15
templates/base.html
```html
<body>
    {% block content %}
    <h1> This is Base Template</h1>
    {% endblock %}
</body>
```

templates/pages/home.html
```html
{% extends "base.html" %}
{% block content %}
{{ super() }}
<div class="gallery">
    {% for item in items %}
    <a href="/item/{{ item.id }}">
        <img src={{ item.image }} alt="{{ item.alt }}" width="200" height="200">
    </a>
    {% endfor %}
</div>
<a href="/add_new_item"><button>Add New Item</button></a>
{% endblock %}
```

### Page 16
templates/base.html
```html
<body>
    {% include 'header.html' %}
    {% block content %}
    <h1>This is Base Template</h1>
    {% endblock %}
    {% include 'footer.html' %}
</body>
```

templates/header.html
```html
<header>
    <h1>This is header</h1>
</header>
```

templates/footer.html
```html
<footer>
    <h1>This is footer</h1>
</footer>
```

### Page 17
templates/forms.html
```html
{% macro input(name, value='', type='text') -%}
    <input type="{{ type }}" value="{{ value|e }}" name="{{ name }}">
{%- endmacro %}
```
```html
{% import 'forms.html' as forms %}
<dl>
    <dt>Username</dt>
    <dd>{{ forms.input('username') }}</dd>
    <dt>Password</dt>
    <dd>{{ forms.input('password', type='password') }}</dd>
</dl>
```
