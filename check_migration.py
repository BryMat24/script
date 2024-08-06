from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import argparse
import sys

def create_app(db_uri):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db = SQLAlchemy(app)
    return app, db

def check_migration_version(target_version, db_uri):
    try:
        app, db = create_app(db_uri)

        # finding all the schema with the alembic_version table
        schemas_result = db.session.execute("SELECT DISTINCT table_schema FROM INFORMATION_SCHEMA.TABLES WHERE table_name = 'alembic_version';")
        schemas = [row[0] for row in schemas_result]

        # checking if all the schema version is as expected
        migration_status = True
        for schema in schemas:
            current_version_result = db.session.execute(f"SELECT version_num FROM {schema}.alembic_version")
            current_version = current_version_result.fetchone()[0]
            if current_version != target_version:
                print(f"Migration version mismatch in schema '{schema}': Expected {target_version}, Found {current_version}")
                migration_status = False
        
        if migration_status:    
            print(f"Migration to version {target_version} has been completed successfully.")
            return 0
        else:
            return -1
    except Exception as e:
        print(str(e))
        return -1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check the database migration version.')
    parser.add_argument('--db_uri', type=str, required=True, help='Database URI')
    parser.add_argument('--target_version', type=str, required=True, help='The target migration version to check against')
    args = parser.parse_args()
    
    result = check_migration_version(args.target_version, args.db_uri)
    sys.exit(result)