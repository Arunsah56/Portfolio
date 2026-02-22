# PostgreSQL Database Setup Guide

This project is configured to use **PostgreSQL** as the primary database. All database credentials are managed through the `.env` file.

## Prerequisites

- PostgreSQL server installed and running
- Python virtual environment activated
- All dependencies installed from `requirements.txt`

## Step 1: Install PostgreSQL

### Windows
1. Download PostgreSQL from [postgresql.org](https://www.postgresql.org/download/windows/)
2. Run the installer and follow the setup wizard
3. Remember the **password** for the `postgres` user
4. Keep the default port as `5432`

### macOS
```bash
brew install postgresql
brew services start postgresql
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get install postgresql postgresql-contrib
sudo service postgresql start
```

## Step 2: Create Database and User

Open PostgreSQL command line:

### Windows (PowerShell)
```powershell
psql -U postgres -W
```

### macOS/Linux
```bash
sudo -u postgres psql
```

Then execute these commands:

```sql
-- Create a new database
CREATE DATABASE portfolio_db;

-- Create a new user
CREATE USER portfolio_user WITH PASSWORD 'your_secure_password';

-- Grant privileges
ALTER ROLE portfolio_user SET client_encoding TO 'utf8';
ALTER ROLE portfolio_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE portfolio_user SET default_transaction_deferrable TO on;
ALTER ROLE portfolio_user SET timezone TO 'UTC';

-- Grant all privileges on the database
GRANT ALL PRIVILEGES ON DATABASE portfolio_db TO portfolio_user;

-- Exit psql
\q
```

## Step 3: Update .env File

Edit your `.env` file with the PostgreSQL credentials:

```env
# PostgreSQL Database Configuration
DB_NAME=portfolio_db
DB_USER=portfolio_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432

# Keep your existing settings
SECRET_KEY=your-existing-secret-key
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## Step 4: Run Migrations

Activate your virtual environment and run migrations:

```powershell
# Windows
& venv\Scripts\Activate.ps1
python manage.py migrate
```

```bash
# macOS/Linux
source venv/bin/activate
python manage.py migrate
```

### Expected Output
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, home, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
  Applying home.0003_auto_sync_models... OK
```

## Step 5: Create Superuser (Admin Account)

```powershell
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

## Step 6: Verify Connection

Test the database connection:

```powershell
python manage.py shell
```

```python
from django.db import connection
cursor = connection.cursor()
print("✓ Database connected successfully!")
exit()
```

## Step 7: Start Development Server

```powershell
python manage.py runserver
```

Visit `http://localhost:8000` to see your project running with PostgreSQL.

## Backup and Restore

### Backup Database

```bash
pg_dump -U portfolio_user -W -h localhost portfolio_db > backup.sql
```

### Restore Database

```bash
psql -U portfolio_user -W -h localhost portfolio_db < backup.sql
```

## Troubleshooting

### Issue: "FATAL: Ident authentication failed"
**Solution**: Make sure you're using the correct password and the user exists in PostgreSQL.

### Issue: "Error loading psycopg2 module" (Windows)
**Solution**: The project uses `psycopg[binary]` which includes the PostgreSQL client libraries. If this error persists:
```powershell
pip install psycopg[binary] --upgrade --force-reinstall
```

### Issue: "Cannot connect to database server"
**Solution**: Ensure PostgreSQL is running:

**Windows**:
```powershell
Get-Service postgresql-x64-* | Start-Service
```

**macOS**:
```bash
brew services start postgresql
```

**Linux**:
```bash
sudo service postgresql start
```

### Issue: "Database 'portfolio_db' does not exist"
**Solution**: Run the SQL commands from Step 2 again to create the database and user.

## Development vs Production

### Development
- **Database**: Local PostgreSQL via `localhost`
- **Host**: `localhost` or `127.0.0.1`
- **Port**: `5432` (default)

### Production (e.g., Heroku, AWS RDS)
- Update `.env` with your cloud database credentials
- Example:
  ```env
  DB_HOST=your-rds-instance.amazonaws.com
  DB_PORT=5432
  DB_USER=your_db_user
  DB_PASSWORD=your_secure_password
  DB_NAME=your_db_name
  ```

## Docker Setup (Optional)

If you prefer running PostgreSQL in Docker:

```bash
docker run --name portfolio-db \
  -e POSTGRES_DB=portfolio_db \
  -e POSTGRES_USER=portfolio_user \
  -e POSTGRES_PASSWORD=your_secure_password \
  -p 5432:5432 \
  -d postgres:16
```

Then update `.env`:
```env
DB_HOST=localhost
DB_PORT=5432
```

## Additional Resources

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Django PostgreSQL Documentation](https://docs.djangoproject.com/en/6.0/ref/databases/#postgresql-notes)
- [psycopg Documentation](https://www.psycopg.org/)

---

**Note**: Never commit sensitive credentials to version control. The `.env` file is listed in `.gitignore` to prevent accidental exposure.
