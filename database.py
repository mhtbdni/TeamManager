import sqlite3
import os

DB_FOLDER = "data"
DB_NAME = "team.db"

if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

DB_PATH = os.path.join(DB_FOLDER, DB_NAME)


def connect_db():
    return sqlite3.connect(DB_PATH)


def create_tables():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        deadline TEXT
    )
    """)

    cursor.execute("""
   CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        title TEXT,
        status TEXT,
        priority TEXT,
        deadline TEXT,
        assigned_to TEXT
)
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS project_members(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        member_name TEXT
)
    """)
    conn.commit()
    conn.close()


def register_user(fullname, username, password):

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users(fullname,username,password) VALUES(?,?,?)",
            (fullname, username, password)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def login_user(username, password):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def add_project(title, description, deadline):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO projects(title,description,deadline) VALUES(?,?,?)",
        (title, description, deadline)
    )

    conn.commit()
    conn.close()


def get_projects():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM projects ORDER BY id DESC")

    projects = cursor.fetchall()

    conn.close()

    return projects
def delete_project(project_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM projects WHERE id=?",
        (project_id,)
    )

    conn.commit()
    conn.close()


def update_project(project_id, title, description, deadline):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE projects
        SET title=?,
            description=?,
            deadline=?
        WHERE id=?
    """, (title, description, deadline, project_id))

    conn.commit()
    conn.close()
def get_project(project_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM projects WHERE id=?",
        (project_id,)
    )

    project = cursor.fetchone()

    conn.close()

    return project
current_project_id = None


def set_current_project(project_id):
    global current_project_id
    current_project_id = project_id


def get_current_project():
    return current_project_id
def add_task(project_id, title, priority, deadline, assigned_to):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks(
            project_id,
            title,
            status,
            priority,
            deadline,
            assigned_to
        )
        VALUES(?,?,?,?,?,?)
    """, (
        project_id,
        title,
        "Pending",
        priority,
        deadline,
        assigned_to
    ))

    conn.commit()
    conn.close()

def get_tasks(project_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
        id,
        project_id,
        title,
        status,
        priority,
        deadline,
        assigned_to
        FROM tasks
        WHERE project_id=?
        ORDER BY id DESC
    """, (project_id,))

    tasks = cursor.fetchall()

    conn.close()

    return tasks
def delete_task(task_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()
def update_task_status(task_id, status):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET status=?
        WHERE id=?
        """,
        (status, task_id)
    )

    conn.commit()
    conn.close()
def project_progress(project_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE project_id=?",
        (project_id,)
    )

    total = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tasks
        WHERE project_id=?
        AND status='Completed'
        """,
        (project_id,)
    )

    completed = cursor.fetchone()[0]

    conn.close()

    if total == 0:
        return 0

    return int((completed / total) * 100)
def complete_task(task_id):

    update_task_status(
        task_id,
        "Completed"
    )
def add_member(project_id, member_name):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO project_members(project_id, member_name)
        VALUES(?,?)
    """, (project_id, member_name))

    conn.commit()
    conn.close()
def get_members(project_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM project_members
        WHERE project_id=?
    """, (project_id,))

    members = cursor.fetchall()

    conn.close()

    return members