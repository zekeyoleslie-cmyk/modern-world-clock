from flask import Flask, render_template
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

CITIES = [
    {"continent": "Africa",  "flag": "🇨🇲", "city": "Douala",       "tz": "Africa/Douala"},
    {"continent": "Africa",  "flag": "🇳🇬", "city": "Lagos",        "tz": "Africa/Lagos"},
    {"continent": "Africa",  "flag": "🇰🇪", "city": "Nairobi",      "tz": "Africa/Nairobi"},
    {"continent": "Africa",  "flag": "🇿🇦", "city": "Johannesburg", "tz": "Africa/Johannesburg"},
    {"continent": "Europe",  "flag": "🇬🇧", "city": "London",       "tz": "Europe/London"},
    {"continent": "Europe",  "flag": "🇫🇷", "city": "Paris",        "tz": "Europe/Paris"},
    {"continent": "Europe",  "flag": "🇩🇪", "city": "Berlin",       "tz": "Europe/Berlin"},
    {"continent": "Asia",    "flag": "🇦🇪", "city": "Dubai",        "tz": "Asia/Dubai"},
    {"continent": "Asia",    "flag": "🇮🇳", "city": "New Delhi",    "tz": "Asia/Kolkata"},
    {"continent": "Asia",    "flag": "🇯🇵", "city": "Tokyo",        "tz": "Asia/Tokyo"},
    {"continent": "Asia",    "flag": "🇨🇳", "city": "Beijing",      "tz": "Asia/Shanghai"},
    {"continent": "Americas","flag": "🇺🇸", "city": "New York",     "tz": "America/New_York"},
    {"continent": "Americas","flag": "🇺🇸", "city": "Los Angeles",  "tz": "America/Los_Angeles"},
    {"continent": "Americas","flag": "🇧🇷", "city": "São Paulo",    "tz": "America/Sao_Paulo"},
    {"continent": "Oceania", "flag": "🇦🇺", "city": "Sydney",       "tz": "Australia/Sydney"},
    {"continent": "Oceania", "flag": "🇳🇿", "city": "Auckland",     "tz": "Pacific/Auckland"},
    {"continent": "UTC",     "flag": "🌍", "city": "UTC",           "tz": "UTC"},
]


@app.route("/")
def index():
    now = datetime.now()
    hour = now.hour
    ampm = "AM" if hour < 12 else "PM"
    h12 = hour % 12 or 12

    world_rows = []
    for c in CITIES:
        local = datetime.now(ZoneInfo(c["tz"]))
        world_rows.append({
            **c,
            "time": local.strftime("%H:%M:%S"),
        })

    return render_template(
        "index.html",
        h=f"{h12:02d}",
        m=f"{now.minute:02d}",
        s=f"{now.second:02d}",
        ampm=ampm,
        world_rows=world_rows,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
