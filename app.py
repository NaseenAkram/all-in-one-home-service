from flask import Flask, request
import requests
import os

BOOKINGS_PASSWORD = "FARIDABAD@2026"

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
<head>
<title>ALL IN ONE HOME SERVICE</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="AC Repair, Refrigerator Repair, Washing Machine Repair and Geyser Service in Arwal Bihar. Call 7739900391.">
</head>
    <body style="font-family:Arial;background:#f4f7fb;margin:0;">

<div style="background:#0d47a1;color:white;padding:60px 15px;text-align:center;">
<h1 style="font-size:clamp(28px,5vw,42px);margin-bottom:10px;">
ALL IN ONE HOME SERVICE
</h1>
        <h3>Fast & Trusted Home Appliance Repair Service</h3>

        <p>📍 Service Available Across Arwal District</p>

        <h2>📞 7739900391</h2>
        <h3>📞 6206534287</h3>

<a href="https://wa.me/917739900391">
<button style="background:#25D366;color:white;padding:15px 30px;border:none;border-radius:8px;font-size:18px;font-weight:bold;">
WhatsApp Now
</button>
</a>

<a href="tel:+917739900391">
<button style="background:#ff9800;color:white;padding:15px 30px;border:none;border-radius:8px;font-size:18px;font-weight:bold;">
Call Now
</button>
</a>
    </div>

<div style="padding:30px;text-align:center;">

<div style="
background:red;
color:white;
padding:20px;
text-align:center;
font-size:18px;
font-weight:bold;
border-radius:10px;
margin-bottom:20px;">
🚨 Same Day Home Service Available
📞 Call Now: 7739900391
</div>
<div style="text-align:center;margin:15px 0;">
    <a href="/booking" style="text-decoration:none;">
        <button style="
background:#ff9800;
        color:white;
        padding:16px 35px;
        border:none;
        border-radius:50px;
        font-size:20px;
        font-weight:bold;
        cursor:pointer;
        box-shadow:0 5px 15px #999;">
        📋 BOOK SERVICE NOW
        </button>
    </a>
</div>
<h2 style="color:#0d47a1;">Our Services</h2>

<div style="background:white;padding:25px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;font-size:20px;font-weight:bold;">
❄️ AC Service & Repair
        </div>

<div style="background:white;padding:25px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;font-size:20px;font-weight:bold;">
🧊 Refrigerator Repair
        </div>

<div style="background:white;padding:25px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;font-size:20px;font-weight:bold;">
🌀 Washing Machine Repair
        </div>

<div style="background:white;padding:25px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;font-size:20px;font-weight:bold;">
🔥 Geyser Service
        </div>

        <h2 style="color:#0d47a1;">Why Choose Us?</h2>

        <p>✔ Service Across Arwal District</p>
        <p>✔ Fast Response</p>
        <p>✔ Affordable Charges</p>
        <p>✔ Trusted Service</p>
<h2 style="color:#0d47a1;">Customer Reviews</h2>

<div style="background:white;padding:15px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;">
⭐⭐⭐⭐⭐ Excellent AC Service
</div>

<div style="background:white;padding:15px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;">
⭐⭐⭐⭐⭐ Fast Refrigerator Repair
</div>

<div style="background:white;padding:15px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;">
⭐⭐⭐⭐⭐ Trusted Washing Machine Service
</div>

<h2 style="color:#0d47a1;text-align:center;margin-top:30px;width:100%;">
Frequently Asked Questions
</h2>

<div style="background:white;padding:15px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;">
<b>Q. Same Day Service Available?</b><br>
Yes, same day service available.
</div>

<div style="background:white;padding:15px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;">
<b>Q. Which Areas Do You Serve?</b><br>
Arwal District and nearby areas.
</div>

<div style="background:white;padding:15px;margin:15px;border-radius:12px;box-shadow:0 0 10px #ddd;">
<b>Q. Do You Repair All Brands?</b><br>
Yes, we repair most major brands.
</div>

<div style="display:flex;justify-content:center;gap:30px;flex-wrap:wrap;padding:30px;">

<div style="background:white;padding:20px 40px;border-radius:15px;box-shadow:0 5px 15px #ddd;">
<h1 style="color:#0d47a1;">150+</h1>
<p>Services Completed</p>
</div>

<div style="background:white;padding:20px 40px;border-radius:15px;box-shadow:0 5px 15px #ddd;">
<h1 style="color:#0d47a1;">75+</h1>
<p>Happy Customers</p>
</div>

<div style="background:white;padding:20px 40px;border-radius:15px;box-shadow:0 5px 15px #ddd;">
<h1 style="color:#0d47a1;">24x7</h1>
<p>Support Available</p>
</div>

</div>



    </div>
<h2 style="color:#0d47a1;text-align:center;">
📍 Our Location
</h2>

<div style="text-align:center;padding:20px;">
<iframe
src="https://maps.google.com/maps?q=Arwal%20Bihar&t=&z=13&ie=UTF8&iwloc=&output=embed"
width="90%"
height="300"
style="border:0;border-radius:15px;">
</iframe>
</div>
    <div style="background:#0d47a1;color:white;padding:20px;text-align:center;">
        <h3>ALL IN ONE HOME SERVICE</h3>
        <p>Arwal District, Bihar</p>
        <p>📞 7739900391 | 6206534287</p>
    </div>
<a href="https://wa.me/917739900391"
style="
position:fixed;
bottom:10px;
right:20px;
background:#25D366;
color:white;
padding:12px 18px;
border-radius:50px;
text-decoration:none;
font-weight:bold;
box-shadow:0 0 10px #999;
z-index:9999;">
💬 WhatsApp
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
            f.write(f"Name: {name}\\n")
            f.write(f"Mobile: {mobile}\\n")
            f.write(f"Address: {address}\\n")
            f.write(f"Service: {service}\\n")
            f.write("-------------------\\n")

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
<html>
<body style="font-family:Arial;background:#f4f7fb;text-align:center;padding:50px;">

<div style="max-width:600px;margin:auto;background:white;padding:40px;border-radius:20px;box-shadow:0 5px 20px #ddd;">

<h1 style="color:green;">✅ Booking Submitted Successfully!</h1>

<h3>Thank You For Choosing ALL IN ONE HOME SERVICE</h3>

<p>Our team will contact you shortly.</p>

<br>

<a href="tel:+917739900391" style="background:#ff9800;color:white;padding:12px 25px;border-radius:8px;text-decoration:none;font-weight:bold;">
📞 Call Now
</a>

&nbsp;&nbsp;

<a href="https://wa.me/917739900391" style="background:#25D366;color:white;padding:12px 25px;border-radius:8px;text-decoration:none;font-weight:bold;">
💬 WhatsApp
</a>

<br><br><br>

<a href="/" style="background:#0d47a1;color:white;padding:12px 25px;border-radius:8px;text-decoration:none;font-weight:bold;">
🏠 Back To Home
</a>

</div>

</body>
</html>
"""

    return """
<html>
<body style="font-family:Arial;background:#f4f7fb;margin:0;">

<div style="background:#0d47a1;color:white;padding:30px;text-align:center;">
<h1>📋 Book Home Service</h1>
<p>Fast & Trusted Appliance Repair Service</p>
</div>

<div style="max-width:500px;margin:30px auto;background:white;padding:30px;border-radius:15px;box-shadow:0 5px 15px #ddd;">

<form method="POST">

<label><b>Your Name</b></label><br>
<input type="text" name="name" required
style="width:95%;padding:12px;margin-top:8px;margin-bottom:15px;border:1px solid #ccc;border-radius:8px;"><br>

<label><b>Mobile Number</b></label><br>
<input type="text" name="mobile" required
style="width:95%;padding:12px;margin-top:8px;margin-bottom:15px;border:1px solid #ccc;border-radius:8px;"><br>

<label><b>Address</b></label><br>
<input type="text" name="address" required
style="width:95%;padding:12px;margin-top:8px;margin-bottom:15px;border:1px solid #ccc;border-radius:8px;"><br>

<label><b>Select Service</b></label><br>
<select name="service"
style="width:100%;padding:12px;margin-top:8px;margin-bottom:20px;border:1px solid #ccc;border-radius:8px;">

<option>AC Service</option>
<option>Refrigerator Repair</option>
<option>Washing Machine Repair</option>
<option>Geyser Service</option>

</select>

<button type="submit"
style="
width:100%;
background:#ff9800;
color:white;
padding:15px;
border:none;
border-radius:10px;
font-size:18px;
font-weight:bold;">
🚀 Submit Booking
</button>

</form>

</div>

</body>
</html>
    """


@app.route("/bookings", methods=["GET", "POST"])
def bookings():

    if request.method == "POST":

        password = request.form["password"]

        if password == BOOKINGS_PASSWORD:

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

        return """
        <html>
        <body style="text-align:center;font-family:Arial;">
            <h2 style="color:red;">Wrong Password</h2>
            <a href="/bookings">Try Again</a>
        </body>
        </html>
        """

    return """
    <html>
    <body style="font-family:Arial;text-align:center;padding:50px;">

        <h2>Admin Login</h2>

        <form method="POST">

            <input type="password"
                   name="password"
                   placeholder="Enter Password"
                   required>

            <br><br>

            <button type="submit">
                Login
            </button>

        </form>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
