from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """


ALL IN ONE HOME SERVICE



<body style="font-family:Arial;background:#f4f7fb;margin:0;">

<div style="background:#0d47a1;color:white;padding:50px;text-align:center;">
    <h1>ALL IN ONE HOME SERVICE</h1>
    <h3>Fast & Trusted Home Appliance Repair Service</h3>

    <p>📍 Service Available Across Arwal District</p>

    <h2>📞 7739900391</h2>
    <h3>📞 6206534287</h3>

    <a href="https://wa.me/917739900391">
        <button style="background:#25D366;color:white;padding:12px 25px;border:none;border-radius:8px;font-size:16px;">
            WhatsApp Now
        </button>
    </a>

    <a href="tel:+917739900391">
        <button style="background:#ff9800;color:white;padding:12px 25px;border:none;border-radius:8px;font-size:16px;">
            Call Now
        </button>
    </a>
</div>

<div style="padding:30px;text-align:center;">

    <h2 style="color:#0d47a1;">Our Services</h2>

    <div style="background:white;padding:20px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;">
        🧊 AC Service & Repair
    </div>

    <div style="background:white;padding:20px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;">
        ❄ Refrigerator Repair
    </div>

    <div style="background:white;padding:20px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;">
        🧺 Washing Machine Repair
    </div>

    <div style="background:white;padding:20px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;">
        🔥 Geyser Service
    </div>

    <h2 style="color:#0d47a1;">Why Choose Us?</h2>

    <p>✔ Service Across Arwal District</p>
    <p>✔ Fast Response</p>
    <p>✔ Affordable Charges</p>
    <p>✔ Trusted Service</p>

    <form action="/booking">
        <button style="background:#1976d2;color:white;padding:12px 25px;border:none;border-radius:8px;font-size:16px;">
            Book Service
        </button>
    </form>

    <br>

    <a href="/bookings">
        <button style="background:black;color:white;padding:12px 25px;border:none;border-radius:8px;">
            View Bookings
        </button>
    </a>

</div>

<div style="background:#0d47a1;color:white;padding:20px;text-align:center;">
    <h3>ALL IN ONE HOME SERVICE</h3>
    <p>Arwal District, Bihar</p>
    <p>📞 7739900391 | 6206534287</p>
</div>

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

    try:
        requests.post(
            "https://script.google.com/macros/s/AKfycbwP3FIxxUnLiHQ9vd9XOYlzomKkUDDCXvTUrkqoF92Y8uRgNMTnrN5JKVMH-GXlRcZo/exec",
            json={
                "name": name,
                "mobile": mobile,
                "address": address,
                "service": service
            }
        )
    except:
        pass

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
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
