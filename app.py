from flask import Flask, render_template, request, redirect, session, flash, Response
import docker
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "docker_cleanup_dashboard_secret"

# =====================================
# Docker Connection
# =====================================

try:
    client = docker.from_env()
    client.ping()
    docker_connected = True
except Exception:
    client = None
    docker_connected = False


# =====================================
# Database Initialization
# =====================================

def init_db():
    conn = sqlite3.connect("cleanup.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cleanup_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image_name TEXT,
        image_id TEXT,
        size REAL,
        deleted_at TEXT
    )
    """)

    conn.commit()
    conn.close()


init_db()

# =====================================
# Demo Login Credentials
# =====================================

USERNAME = "admin"
PASSWORD = "admin123"


# =====================================
# Login Page
# =====================================
@app.route("/export")
def export_report():

    if "user" not in session:
        return redirect("/")

    conn = sqlite3.connect("cleanup.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM cleanup_history
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    csv_data = "ID,Image Name,Image ID,Size Freed(MB),Deleted At\n"

    for row in data:
        csv_data += (
            f"{row[0]},"
            f"{row[1]},"
            f"{row[2]},"
            f"{row[3]},"
            f"{row[4]}\n"
        )

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=cleanup_report.csv"
        }
    )
    
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:

            session["user"] = username
            return redirect("/dashboard")

        flash("Invalid username or password")

    return render_template("login.html")


# =====================================
# Dashboard
# =====================================

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    if not docker_connected:
        return """
        <h1>Docker Engine Not Running</h1>
        <p>Please start Docker Desktop and refresh.</p>
        """

    images = client.images.list()
    containers = client.containers.list(all=True)

    used_images = set()

    for container in containers:
        try:
            used_images.add(container.image.id)
        except Exception:
            pass

    image_data = []

    total_size = 0
    dangling_count = 0
    unused_count = 0
    duplicate_count = 0
    health_score = 100

    for image in images:

        try:
            size_mb = round(
                image.attrs["Size"] / (1024 * 1024),
                2
            )
        except Exception:
            size_mb = 0

        total_size += size_mb

        tags = image.tags if image.tags else ["<none>:<none>"]

        is_dangling = tags == ["<none>:<none>"]

        if is_dangling:
            dangling_count += 1

        is_unused = image.id not in used_images

        if is_unused:
            unused_count += 1

        image_data.append({
            "id": image.short_id.replace("sha256:", ""),
            "full_id": image.id,
            "tag": ", ".join(tags),
            "size": size_mb,
            "dangling": is_dangling,
            "unused": is_unused
        })


    health_score -= unused_count * 5
    health_score -= dangling_count * 10
    health_score -= duplicate_count * 5

    if health_score < 0:
     health_score = 0
     
    potential_savings = 0

    for img in image_data:

        if img["unused"] or img["duplicate"]:

            potential_savings += img["size"]

    potential_savings = round(
        potential_savings,
        2
)
    
    # Total saved storage

    conn = sqlite3.connect("cleanup.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COALESCE(SUM(size),0)
    FROM cleanup_history
    """)

    total_saved = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        images=image_data,
        health_score=health_score,
        total_images=len(image_data),
        total_size=round(total_size, 2),
        dangling_count=dangling_count,
        unused_count=unused_count,
        total_saved=round(total_saved, 2)
    )


# =====================================
# Delete Single Image
# =====================================

@app.route("/delete/<path:image_id>")
def delete_image(image_id):

    if "user" not in session:
        return redirect("/")

    try:

        image = client.images.get(image_id)

        image_name = (
            image.tags[0]
            if image.tags
            else "<none>:<none>"
        )

        size_mb = round(
            image.attrs["Size"] / (1024 * 1024),
            2
        )

        conn = sqlite3.connect("cleanup.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO cleanup_history
        (
            image_name,
            image_id,
            size,
            deleted_at
        )
        VALUES (?,?,?,?)
        """,
        (
            image_name,
            image_id,
            size_mb,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        ))

        conn.commit()
        conn.close()

        client.images.remove(
            image=image_id,
            force=True
        )

        flash("Image deleted successfully")

    except Exception as e:

        flash(f"Error deleting image: {str(e)}")

    return redirect("/dashboard")


# =====================================
# Cleanup Unused Images
# =====================================

@app.route("/cleanup")
def cleanup():

    if "user" not in session:
        return redirect("/")

    try:

        client.images.prune()

        flash(
            "Unused Docker images cleaned successfully"
        )

    except Exception as e:

        flash(str(e))

    return redirect("/dashboard")


# =====================================
# History Page
# =====================================

@app.route("/history")
def history():

    if "user" not in session:
        return redirect("/")

    conn = sqlite3.connect("cleanup.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM cleanup_history
    ORDER BY id DESC
    """)

    history_data = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        history=history_data
    )


# =====================================
# Logout
# =====================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# =====================================
# Run Application
# =====================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )