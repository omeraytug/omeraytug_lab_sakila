import dlt
from dlt.sources.sql_database import sql_database
from pathlib import Path 

# Paths
DATA_PATH = Path(__file__).parent / "data"

SQLITE_PATH = DATA_PATH / "sqlite-sakila.db" #source
DUCKDB_PATH = DATA_PATH / "sakila.duckdb" # target

source = sql_database(f"sqlite:///{SQLITE_PATH}", schema="main")

pipeline = dlt.pipeline(
    pipeline_name="sakila_sqlite_duckdb",
    destination=dlt.destinations.duckdb(str(DUCKDB_PATH)),
    dataset_name="staging"
)

load_info = pipeline.run(source, write_disposition="replace")

print(load_info)