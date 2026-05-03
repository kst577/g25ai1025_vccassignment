VCC Assignment 3 — g25ai1025
=============================

This repo is for my virtualization / cloud course submission (assignment 3). Everything here is plain Flask: a tiny app for local testing and the copies we used on the GCP instance.

Files
-----
app.py        — Local server on port 5000. Open http://127.0.0.1:5000/ in a browser; you should get the “LOCAL SERVER: RUNNING” page.

cloud_app.py  — Flask app for the VM, listening on port 80 (matches the usual firewall rule for HTTP).

monitor.py    — Same landing page as the cloud app; separate script for the monitoring part of the assignment.

The cloud-facing pages return my ID line (G25AI1025) so it’s obvious which instance is mine.

Run app.py on your machine
--------------------------
  pip install flask
  python app.py

Then visit http://127.0.0.1:5000/

Port 80
-------
cloud_app.py and monitor.py use port 80. On the Linux VM that’s normal. On a Mac, port 80 often needs admin rights, so for testing I mostly use app.py on 5000.

Repo: https://github.com/kst577/g25ai1025_vccassignment

— Saiteja (g25ai1025)
