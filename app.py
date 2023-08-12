from flask import Flask, render_template, request
from summarize_function import summarize

app=Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarizer():
    text = request.form['text']
    num_sentences = int(request.form['num_sentences'])
    summary = summarize(text, num_sentences)
    return render_template('summary.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)