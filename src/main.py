import os
from pipeline.extract import extract_csv
from pipeline.transform import transform
from pipeline.load import load_to_db
from utils.logger import setup_logger
from utils.db_connector import get_connection
from config_loader import load_config

def main():
    # Setup logger
    logger = setup_logger("data_pipeline")

    # Load configuration
    config = load_config()
    raw_path = config['paths']['raw_data']
    db_name = config['database']['name']

    # Connect to database
    conn = get_connection(db_name)

    # Process all CSVs in raw folder
    for file in os.listdir(raw_path):
        if file.endswith(".csv"):
            try:
                logger.info(f"Starting ETL pipeline for {file}")

                # Extract
                df = extract_csv(file, raw_path)
                logger.info(f"Extracted {len(df)} rows")

                # Transform
                df = transform(df)
                logger.info(f"Transformed {len(df)} rows")

                # Load
                load_to_db(df, conn)
                logger.info(f"Loaded {file} into database successfully")

            except Exception as e:
                logger.error(f"Failed processing {file}: {e}")

    # Close DB connection
    conn.close()
    logger.info("ETL pipeline finished successfully")

if __name__ == "__main__":
    main()
