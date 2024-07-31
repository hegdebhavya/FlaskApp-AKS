from flask import Flask, render_template_string
app = Flask(__name__)
html = """
<!DOCTYPE html>
<html>
<head>
<title>AKS Flask App</title>
<style>
        body {
            background-color: #f0f8ff;
            text-align: center;
            padding-top: 200px;
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #2e8b57;
        }
</style>
</head>
<body>
<h1>Yay! Your first AKS app is deployed!</h1>
</body>
</html>
""" 
@app.route('/')
def homepage():
    return render_template_string(html)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
