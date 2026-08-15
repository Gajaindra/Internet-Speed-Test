from flask import Flask, render_template, jsonify
import speedtest

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/speedtest")
def speed_test():

    try:
        # Create speedtest object
        st = speedtest.Speedtest()

        # Find best server
        st.get_best_server()

        # Download speed
        download = st.download() / 1_000_000

        # Upload speed
        upload = st.upload() / 1_000_000

        # Ping
        ping = st.results.ping

        return jsonify({
            "success": True,
            "download": round(download, 2),
            "upload": round(upload, 2),
            "ping": round(ping, 2)
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
