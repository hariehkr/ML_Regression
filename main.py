from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipline
from src.datascience.pipeline.model_trainer_pipelien import ModelTrainerTrainingPipeline 
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


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


STAGE_NAME = "Data Validation Stage"
if __name__ == "__main__":
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = DataValidationTrainingPipline()
            obj.initiate_data_validation()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e


STAGE_NAME = "Data Tranforamtion Stage"
if __name__ == "__main__":
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = DataTransformationPipline()
            obj.initiate_data_transformation()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e
        

STAGE_NAME = "Model Training Stage"
if __name__ == "__main__":
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = ModelTrainerTrainingPipeline()
            obj.initiate_model_training()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e
        
STAGE_NAME = "Model Evaluation Stage"
if __name__ == "__main__":
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = ModelEvaluationPipeline()
            obj.initiate_model_evaluation()
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e
