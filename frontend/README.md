To run the frontend on your localhost, follow the steps below.

```
pip install flask couchdb numpy pandas gunicorn
gunicorn  --workers=20 -D app:app -b 0.0.0.0:5000
```

