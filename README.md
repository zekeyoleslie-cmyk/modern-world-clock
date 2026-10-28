================================================================================
                            MODERN CLOCK APP
================================================================================

A sleek, responsive clock application featuring a live local time display, a
world clock table covering 17 major cities across 6 continents, dark/light
theme switching, and a focus mode — available as both a modern web app and a
native Python desktop application.

--------------------------------------------------------------------------------
TABLE OF CONTENTS
--------------------------------------------------------------------------------

  1.  Overview
  2.  Features
  3.  Screenshots / Preview
  4.  Project Structure
  5.  Tech Stack
  6.  Getting Started
        - Web Version (HTML / CSS / JavaScript)
        - Python Web Version (Flask)
        - Python Desktop Version (Tkinter)
  7.  Keyboard & UI Controls
  8.  Technical Highlights
  9.  World Clock Cities
 10.  Customization
 11.  Known Limitations
 12.  Future Enhancements
 13.  Contributing
 14.  License
 15.  Author
 16.  Acknowledgments

--------------------------------------------------------------------------------
1. OVERVIEW
--------------------------------------------------------------------------------

Modern Clock App is a multi-platform clock display built around a single,
consistent visual identity. It shows the current hour, minute, and second with
an AM/PM indicator, and simultaneously tracks live local time across 17 cities
spanning Africa, Europe, Asia, the Americas, Oceania, and UTC.

The project is delivered in three interchangeable builds so you can pick the
one that fits your environment:

  - Web build         : Pure HTML + CSS + JavaScript (browser-native)
  - Python web build  : Flask server that renders the site in Python
  - Python desktop    : Native Tkinter application (no browser required)

All three builds share the same features, color palette, and world clock
dataset, so the experience is consistent across platforms.

--------------------------------------------------------------------------------
2. FEATURES
--------------------------------------------------------------------------------

CORE FEATURES
  [x] Live local clock with HH : MM : SS display
  [x] AM / PM indicator
  [x] World clock table with live times for 17 cities
  [x] Automatic time-zone handling via IANA tz database
  [x] Dark mode (default) and light mode

USER EXPERIENCE
  [x] Glassmorphic card design with backdrop blur
  [x] Smooth theme transition
  [x] Focus Mode — hides the world clock for a distraction-free view
  [x] Fully responsive layout (web builds)
  [x] Native desktop UI with ttk.Treeview table (Tkinter build)

PLATFORM COVERAGE
  [x] Browser (Chrome, Firefox, Safari, Edge, Opera)
  [x] Local Python server (Flask)
  [x] Native desktop (Windows, macOS, Linux via Tkinter)

--------------------------------------------------------------------------------
3. SCREENSHOTS / PREVIEW
--------------------------------------------------------------------------------

DARK MODE (default)
  +----------------------------------------------------------+
  |                     MODERN CLOCK                          |
  |                                                           |
  |   +---------+  +---------+  +---------+                   |
  |   |   09    |  |   42    |  |   17    |                   |
  |   |  HOURS  |  | MINUTES |  | SECONDS |                   |
  |   |         |  |         |  |   AM    |                   |
  |   +---------+  +---------+  +---------+                   |
  |                                                           |
  |        [ Theme ]        [ Focus Mode ]                    |
  |                                                           |
  |   WORLD CLOCK                                             |
  |   CONTINENT  CITY              TIME                       |
  |   Africa     🇨🇲 Douala        04:42:17                   |
  |   Europe     🇬🇧 London        03:42:17                   |
  |   Asia       🇯🇵 Tokyo        12:42:17                   |
  |   ...                                                     |
  +----------------------------------------------------------+

LIGHT MODE
  Same layout, inverted color scheme (#f4f6f8 background).

FOCUS MODE
  The world clock table is hidden, leaving only the large local clock.

--------------------------------------------------------------------------------
4. PROJECT STRUCTURE
--------------------------------------------------------------------------------

  modern-clock-app/
  |
  |-- web/                          # Pure web build
  |   |-- index.html
  |   |-- style.css
  |   |-- script.js
  |
  |-- flask/                        # Python web build
  |   |-- app.py
  |   |-- templates/
  |   |   |-- index.html
  |
  |-- desktop/                      # Python desktop build
  |   |-- clock_app.py
  |
  |-- README.txt
  |-- LICENSE

--------------------------------------------------------------------------------
5. TECH STACK
--------------------------------------------------------------------------------

  WEB BUILD
    - HTML5  (semantic structure, data attributes)
    - CSS3   (flexbox, grid, backdrop-filter, custom properties)
    - ES6+ JavaScript (Date API, Intl.DateTimeFormat, setInterval)

  PYTHON WEB BUILD
    - Python 3.9+
    - Flask 2.2+
    - zoneinfo (standard library since Python 3.9)
    - Jinja2 templates (bundled with Flask)

  PYTHON DESKTOP BUILD
    - Python 3.9+
    - Tkinter (bundled with Python)
    - ttk.Treeview
    - zoneinfo

  No third-party JS libraries. No build tooling required.

--------------------------------------------------------------------------------
6. GETTING STARTED
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
6.1  WEB BUILD (HTML / CSS / JavaScript)
--------------------------------------------------------------------------------

  OPTION A — Direct use
    1. Download or clone the repository.
    2. Open web/index.html in any modern browser.
    3. Done — no server required.

  OPTION B — Local static server (recommended for consistent behavior)
    Using Python:
      cd web
      python -m http.server 8000

    Using Node.js:
      npx http-server web

    Then visit:
      http://localhost:8000

--------------------------------------------------------------------------------
6.2  PYTHON WEB BUILD (FLASK)
--------------------------------------------------------------------------------

  INSTALL
      pip install flask

  RUN
      cd flask
      python app.py

  OPEN
      http://localhost:5000

  HOW IT WORKS
    - The server renders the initial HTML with time values computed in Python.
    - A minimal JavaScript ticker updates the display once per second so the
      page does not need to reload.
    - Python handles all time-zone conversions via the zoneinfo module.

--------------------------------------------------------------------------------
6.3  PYTHON DESKTOP BUILD (TKINTER)
--------------------------------------------------------------------------------

  INSTALL
      Nothing to install — Tkinter ships with standard Python 3.
      Confirm Tkinter is available:
        python -c "import tkinter; print('ok')"

  RUN
      cd desktop
      python clock_app.py

  RESULT
      A native desktop window with the same layout, theme toggle, focus mode,
      and a live world clock table.

--------------------------------------------------------------------------------
7. KEYBOARD & UI CONTROLS
--------------------------------------------------------------------------------

  CONTROL        WEB BUILD              DESKTOP BUILD
  -------------  ---------------------  ---------------------
  Toggle theme   Click "Theme"          Click "Theme"
  Focus mode     Click "Focus Mode"     Click "Focus Mode"
  Refresh        Automatic (1 s)        Automatic (1 s)

  No keyboard shortcuts are bound by default; this can be added easily
  (see Future Enhancements).

--------------------------------------------------------------------------------
8. TECHNICAL HIGHLIGHTS
--------------------------------------------------------------------------------

WEB BUILD
  - Uses Intl.DateTimeFormat with the IANA timeZone option for accurate,
    DST-aware world-clock times — no manual offsets.
  - Glassmorphic UI via backdrop-filter: blur(10px) and layered shadows.
  - CSS custom properties make theme switching a single class toggle.
  - All intervals (1 s) are aligned across the two ticking clocks.

FLASK BUILD
  - Server-side rendering via Jinja2 — initial paint is instant, no JS needed
    for the first render.
  - zoneinfo used for all time-zone math (correct DST behavior).
  - Minimal client-side JS only for the 1 Hz ticking without a page refresh.
  - CITIES list is a single source of truth used by both server and browser.

DESKTOP BUILD
  - Single Tk root window with a card-style frame for the digital clock.
  - ttk.Treeview provides a native, scrollable world clock table.
  - Time update loop scheduled via root.after(1000, ...) — no threading.
  - Theme toggle modifies widget colors recursively without re-creating them.

--------------------------------------------------------------------------------
9. WORLD CLOCK CITIES
--------------------------------------------------------------------------------

  CONTINENT   CITY              IANA TIME ZONE
  ----------  ----------------  --------------------------
  Africa      Douala            Africa/Douala
  Africa      Lagos             Africa/Lagos
  Africa      Nairobi           Africa/Nairobi
  Africa      Johannesburg      Africa/Johannesburg
  Europe      London            Europe/London
  Europe      Paris             Europe/Paris
  Europe      Berlin            Europe/Berlin
  Asia        Dubai             Asia/Dubai
  Asia        New Delhi         Asia/Kolkata
  Asia        Tokyo             Asia/Tokyo
  Asia        Beijing           Asia/Shanghai
  Americas    New York          America/New_York
  Americas    Los Angeles       America/Los_Angeles
  Americas    São Paulo         America/Sao_Paulo
  Oceania     Sydney            Australia/Sydney
  Oceania     Auckland          Pacific/Auckland
  UTC         UTC               UTC

  To add a city, append a new entry to the CITIES array/list in your chosen
  build — the time zone string must be a valid IANA identifier.

--------------------------------------------------------------------------------
10. CUSTOMIZATION
--------------------------------------------------------------------------------

CHANGE THE COLOR THEME
  Web builds — edit the following values in style.css:
      body              { background: #0e1116; color: #eaeaea; }
      body.light        { background: #f4f6f8; color: #111; }
      .time             { background: rgba(255,255,255,0.05); }
      button            { background: #2d6cdf; }

  Desktop build — edit the hex values inside ClockApp.__init__ and
  toggle_theme().

CHANGE THE ACCENT COLOR
  Replace every occurrence of #2d6cdf with your brand color.

CHANGE THE CLOCK CARD SIZE
  Web builds — adjust .time { width: 85px; height: 75px; font-size: 38px; }
  Desktop build — adjust the width/height/font in _make_block().

CHANGE THE REFRESH RATE
  Web builds — change setInterval(..., 1000) to your preferred milliseconds.
  Desktop build — change self.root.after(1000, self.update_time).

ADD OR REMOVE CITIES
  Edit the CITIES list in the build you are using. No other changes needed.

SWITCH DEFAULT THEME
  Web builds — add class="light" to <body> in index.html.
  Desktop build — set self.light = True in __init__.

--------------------------------------------------------------------------------
11. KNOWN LIMITATIONS
--------------------------------------------------------------------------------

  - Web builds rely on the browser's Intl.DateTimeFormat. Extremely old
    browsers (pre-2017) may not support the timeZone option.
  - Flask build requires Python 3.9+ for zoneinfo; on older Python use the
    backports.zoneinfo package.
  - The Tkinter build uses system fonts for emoji flags. Some Linux
    distributions require installing a color-emoji font for flags to render.
  - Emoji flag rendering in the Flask/web builds depends on the user's OS and
    browser font stack.
  - No persistence — theme preference resets on reload unless you add
    localStorage support (see Future Enhancements).

--------------------------------------------------------------------------------
12. FUTURE ENHANCEMENTS
--------------------------------------------------------------------------------

  [ ] Persist theme choice via localStorage (web) or a config file (desktop)
  [ ] Add keyboard shortcuts (T = theme, F = focus, W = toggle world clock)
  [ ] User-selectable city list (add / remove / reorder)
  [ ] 12-hour / 24-hour format toggle
  [ ] Analog clock face option
  [ ] Alarm and stopwatch modes
  [ ] Progressive Web App (PWA) support with offline caching
  [ ] Unit tests with pytest (Python) and Vitest (JS)
  [ ] Internationalization (i18n) for labels and date formats
  [ ] Optional system-tray / menu-bar mini clock (desktop)

--------------------------------------------------------------------------------
13. CONTRIBUTING
--------------------------------------------------------------------------------

  Contributions are welcome. To contribute:

    1. Fork the repository.
    2. Create a feature branch:
         git checkout -b feature/amazing-feature
    3. Commit your changes:
         git commit -m "Add amazing feature"
    4. Push your branch:
         git push origin feature/amazing-feature
    5. Open a Pull Request describing what you changed and why.

  GUIDELINES
    - Follow the existing code style in each build.
    - Keep the CITIES dataset consistent across all three builds.
    - Add comments for any non-trivial logic.
    - Update this README if you add new features or options.

--------------------------------------------------------------------------------
14. LICENSE
--------------------------------------------------------------------------------

  MIT License

  Copyright (c) 2025

  Permission is hereby granted, free of charge, to any person obtaining a
  copy of this software and associated documentation files (the "Software"),
  to deal in the Software without restriction, including without limitation
  the rights to use, copy, modify, merge, publish, distribute, sublicense,
  and/or sell copies of the Software, and to permit persons to whom the
  Software is furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
  DEALINGS IN THE SOFTWARE.

--------------------------------------------------------------------------------
15. AUTHOR
--------------------------------------------------------------------------------

  Zekeyo Leslie NGWENYI 
    GitHub  : https://github.com/zekcmky
    Email   : zekeyoleslie@gmail.com
    Website : https://yourwebsite.com

  Maintainers and community contributors are listed in CONTRIBUTORS.txt
  (create this file as the project grows).

--------------------------------------------------------------------------------
16. ACKNOWLEDGMENTS
--------------------------------------------------------------------------------

  - Inspired by minimalist iOS and macOS clock apps.
  - Time-zone data powered by the IANA Time Zone Database.
  - Design influenced by modern glassmorphic UI trends.
  - Built with vanilla web technologies and the Python standard library —
    no frameworks, no external assets.

================================================================================
      If you find this project useful, please consider giving it a star!
================================================================================
