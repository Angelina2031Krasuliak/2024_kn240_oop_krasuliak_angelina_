from flask import Flask, Response, redirect, url_for
import matplotlib.pyplot as plt
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>🌟 Welcome to the Beautiful Math Plotter!</h1>
        <p>Click the button below to see a colorful graph!</p>
        <form action="/plot">
            <button style="padding: 10px 20px; font-size: 18px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;">
                Show Plot 🎨
            </button>
        </form>
    '''

@app.route('/plot')
def plot():
   
    x = np.linspace(-10, 10, 400)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tanh(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label="sin(x)", color="blue", linestyle="--", linewidth=2)
    plt.plot(x, y2, label="cos(x)", color="green", linestyle="-.", linewidth=2)
    plt.plot(x, y3, label="tanh(x)", color="red", linestyle=":", linewidth=2)

    plt.title("🌈 Beautiful Math Functions", fontsize=18)
    plt.xlabel("x", fontsize=14)
    plt.ylabel("y", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return Response(buf.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
