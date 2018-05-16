# Flask Package Note

## flask app 基本架構
```commandline
minimal_flask
├── README.md
├── minimal_flask
│   ├── __init__.py
│   ├── static
│   │   └── style.css
│   ├── templates
│   │   └── index.html
│   └── views.py
└── setup.py

```

## 從 module 到 package
- 新增跟 package (e.g., `minimal_flask`) 同名的資料夾, 把本來的所有資料丟進去
- 新增 `setup.py`
- 將 `app.py` 改名成 `__init__.py`
- 將 `app.py` 裡頭的 view functions (頭上有 `@route` 的 functions) 丟到另外一個 `views.py` 裡頭
- `app.py` import view module, e.g., `import minimal_flask.views`
- `views.py` import app, e.g., `from minimal_flask import app`

## Environment

```commandline
source activate flask
```


## Package 設定
環境變數
```commandline
export FLASK_APP=minimal_flask
export FLASK_DEBUG=true
```

在 project 資料夾下安裝 package:
```commandline
pip install -e .
```

執行 application
```commandline
flask run
```

## 注意點
- Package 跟 folder 有兩個字以上用 underscore `_`, 不要用`-`. 要不會出現 `ModuleNotFoundError`.


## References
- [Larger Applications](http://flask.pocoo.org/docs/0.12/patterns/packages/)

## Resources
- [BootstrapCDN](https://www.bootstrapcdn.com/)
- [Bootsnipp - templates](https://bootsnipp.com/)
- [faviconer](http://www.faviconer.com/icon/index)
