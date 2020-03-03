# Setup

- use elephantsql postgres URL (set URL as DATABASE_URI in .env)
- pip install flask-migrate -> flask db init
- flask db migrate
- flask db upgrade (allows you to create table before starting app)
- after make change to table in Users model, run "flask db migrate"
  - (Detected added unique constraint 'None' on '['username']')
- flask db upgrade (Running upgrade b518aec40f0c -> 943288b55818)
- SELECT \* FROM alembic_version; in elephantsql will tell you what version you're in
- when you create a new migration, make sure that your constraints are named
- flask db migrate -m "Added email column in users table for email notifications"
- add names to upgrade and downgrade functions in migration versions ('users_email_key')
- flask db upgrade
