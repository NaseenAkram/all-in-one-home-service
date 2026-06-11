from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>ALL IN ONE HOME SERVICE</title>
    </head>

    <body style="font-family:Arial;text-align:center;background:#e8f5e9;padding:30px;">

    <h1 style="color:green;">ALL IN ONE HOME SERVICE</h1>

    <h3>📍 Arwal</h3>

    <h3>📞 7739900391</h3>
    <h3>📞 6206534287</h3>

    <a href="https://wa.me/917739000391">
        <button style="background:green;color:white;padding:10px 20px;border:none;border-radius:5px;">
            WhatsApp Now
        </button>
    </a>

    <h2>Our Services</h2>

    <p>✅ AC Service & Repair</p>
    <p>✅ Refrigerator Repair</p>
    <p>✅ Washing Machine Repair</p>
    <p>✅ Geyser Service</p>

    <br>

    <form action="/booking">
        <button style="background:blue;color:white;padding:10px 20px;border:none;border-radius:5px;" type="submit">
            Book Service
        </button>
    </form>

    <br><br>

    <a href="/bookings">
        <button style="background:black;color:white;padding:10px 20px;border:none;border-radius:5px;">
            View Bookings
        </button>
    </a>

    </body>
    </html>
    """

@app.route("/booking", methods=["GET", "POST"])
def booking():

    if request.method == "POST":

        name = request.form["name"]
        mobile = request.form["mobile"]
        address = request.form["address"]
        service = request.form["service"]

        with open("bookings.txt", "a") as f:
            f.write(f"Name: {name}\n")
            f.write(f"Mobile: {mobile}\n")
            f.write(f"Address: {address}\n")
            f.write(f"Service: {service}\n")
            f.write("-------------------\n")

        return """
        <h1 style="color:green;">Booking Submitted Successfully!</h1>
        <h3>We will contact you soon.</h3>
        <a href="/">Go Home</a>
        """

    return """
    <html>
    <body style="font-family:Arial;text-align:center;background:#f5f5f5;padding:30px;">

    <h1>Book Service</h1>

    <form method="POST">

    Name:<br>
    <input type="text" name="name" required><br><br>

    Mobile Number:<br>
    <input type="text" name="mobile" required><br><br>

    Address:<br>
    <input type="text" name="address" required><br><br>

    Service:<br>
    <select name="service">
        <option>AC Service</option>
        <option>Refrigerator Repair</option>
        <option>Washing Machine Repair</option>
        <option>Geyser Service</option>
    </select><br><br>

    <button style="background:green;color:white;padding:10px 20px;border:none;border-radius:5px;" type="submit">
        Submit Booking
    </button>

    </form>

    </body>
    </html>
    """

@app.route("/bookings")
def bookings():

    try:
        with open("bookings.txt", "r") as f:
            data = f.read()
    except:
        data = "No bookings found."

    return f"""
    <html>
    <body style="font-family:Arial;padding:20px;">
        <h1>All Bookings</h1>

        <pre>{data}</pre>

        <br><br>

        <a href="/">
            <button>Go Home</button>
        </a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)