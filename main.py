from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipline


STAGE_NAME = "Data Ingestion Stage"
if __name__ == "__main__":
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = DataIngestionTrainingPipline()
            obj.initiate_data_ingestion()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e
