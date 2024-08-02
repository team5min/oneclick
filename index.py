# ライブラリ
import scratchattach as scratch3
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

load_dotenv()

project_id = "1051954768"

# ログインや接続
session = scratch3.Session(os.environ["session"], username=os.environ["user"])
conn = session.connect_cloud(project_id)
client = scratch3.CloudRequests(conn)

cred = credentials.Certificate("./admin.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": os.environ["database"],
        "databaseAuthVariableOverride": {"uid": "my-service-worker"},
    },
)

root = db.reference("/users")


@client.request
def used(user):
    ref = root.child(user)
    ref.set(False)
    print("inited")
    return "sure"


@client.event
def on_ready():
    print("Ready!")


client.run()
