# Flask-on-Fly-boilerplate

Boilerplate to deploy a Flask app on Fly(fly.io), making use of GitHub Actions.
Flask-admin is used for CRUD on the database. 

To run code locally (development):
flask --app main run


Deploying on fly.io:
- Make sure you have an account on both Fly and on GitHub
- Install the flyctl CLI package for your OS: https://github.com/superfly/flyctl
- Setup a repository on GitHub for your project
- Take steps 1 to 5

1. Setup GitHub actions for own repo:
- Log into Fly platform: flyctl auth login
- Get Fly token: flyctl auth token
- Add Fly token as secret to GitHub repo: Settings --> Secrets --> Actions --> New repository secret: FLY_API_TOKEN="fly_token"

2. Initialize app on Fly:
- Launch app: flyctl launch --> git add fly.toml (automatically created on launch)
- Edit fly.toml --> add to [env] section: PRIMARY_REGION = "ams" (the region picked during launch)
- Push project to main --> docker image built and deployed on Fly

3. Initialize postgres db on Fly:
- Create postgres db: flyctl postgres create --> copy output for own use
- Attach db to app: flyctl attach --app <app name from fly.toml> <db name> --> $DATABASE_URL automatically set on Fly; copy for own use

4. Setup production environment:
- Set secret key: flyctl secrets set SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex())')
- Edit fly.toml --> add to [env] section: FLASK_CONFIG = "production"
- Push project to main --> ProductionConfig in config.py is activated on Fly

5. First db migrations:
- Initialize db locally: flask --app main db init --> file db.sqlite created
- Add first migration to repository: flask --app main db -m "first db migration" --> git add migrations folder
- Upgrade db locally: flask --app main db upgrade
- Edit fly.toml --> create [deploy] section and add to it: release_command = "flask --app main db upgrade"
- Push project to main --> postgres db working remotely
