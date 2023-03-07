from app.main import app

import os
import sys
import uvicorn
from typing import Optional
import json
from glob import glob

def run_server(host: Optional[str] = None, port: Optional[int] = None) -> None:
    host = host or "127.0.0.1"
    port = port or 8000
    uvicorn.run(app, host=host, port=port)

def makemigrations():
    with open('migrations/migrate.json') as f: migrate = json.load(f)
    with open('migrations/makemigrations.json') as f: migration = json.load(f)
    if not(migrate.get('is_migrated')): raise Exception("please migrate")

    version = str(len(migration) + 1)
    length = 5 - len(version)
    name = length*"0"+version
    os.system('alembic revision --autogenerate -m '+name)

    revision = glob('migrations/versions/'+name+"*")[0]
    revision = revision.split("migrations/versions/")[1].split("_")

    migrate['is_migrated'] = False
    migration[revision[0]] = revision[1]

    with open('migrations/migrate.json', "w") as f: json.dump(migrate, f)
    with open('migrations/makemigrations.json', "w") as f: json.dump(migration, f)

def migrate():
    os.system("alembic upgrade head")
    migrate = {"is_migrated":True}
    with open('migrations/migrate.json', "w") as f: json.dump(migrate, f)

def main():
    input_ = sys.argv
    
    #runserver
    if input_[1] == "runserver": run_server()

    #migration
    elif str(" ".join(input_[1:])) == 'makemigrations': makemigrations()
    elif str(" ".join(input_[1:])) == 'migrate': migrate()

    #other
    else: 
        print('migrations/versions/'+"*")
        print(glob('migrations/versions/'))
        # raise Exception('Not Command')


if __name__=="__main__":
    main()
