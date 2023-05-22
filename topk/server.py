from flask import Flask, render_template, request, send_file
from topk import calculate_k

app = Flask('topK')

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == 'POST':
        k = request.form.get('k')
        if k:
            file_name = calculate_k(int(k))
        return send_file(file_name)
    return render_template("index.html")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)