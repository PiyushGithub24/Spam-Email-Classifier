import sys
import os
from src.exception import CustomException
from src.utils import load_object,clean_text


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,email_content):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','tfidf_vectorizer.pkl')
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            email_content=clean_text(str(email_content))                            #data cleaning
            data_vectorized = preprocessor.transform([email_content]).toarray()     #vectorization
            preds=model.predict(data_vectorized)                                    #prediction
            return int(preds[0])
        
        except Exception as e:
            raise CustomException(e,sys)

# if __name__=="__main__":   
#     pp=PredictPipeline()
#     print(pp.predict("Dear Students.You Won 3 Lakhs"))