from fastmcp import FastMCP
from dotenv import load_dotenv
import os
from psycopg.rows import dict_row
from psycopg import connect

load_dotenv()

mcp=FastMCP("student-chatbot")

@mcp.tool
def get_student_data(user_email:str):
    conn_str=os.getenv("DATABASE_URL")
    with connect(conn_str, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users where email=%s",(user_email,))
            results=cur.fetchall()
            return results

@mcp.tool
def get_student_certificates(user_email:str):
    conn_str=os.getenv("DATABASE_URL")
    with connect(conn_str, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM achievements where type='certificate' ",)
            results=cur.fetchall()
            return results

@mcp.tool
def get_student_projects(user_email:str):
    conn_str=os.getenv("DATABASE_URL")
    with connect(conn_str, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM achievements WHERE type='project' ")
            results=cur.fetchall()
            return results

@mcp.tool
def get_student_achievements(user_email:str):
    conn_str=os.getenv("DATABASE_URL")
    with connect(conn_str, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM achievements")
            results=cur.fetchall()
            return results

if __name__=="__main__":
    mcp.run()