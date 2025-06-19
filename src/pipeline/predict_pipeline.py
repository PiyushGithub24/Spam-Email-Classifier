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

if __name__=="__main__":   
    pp=PredictPipeline()
    print(pp.predict("Dear Students, This is a reminder that the registration for the upcoming semester closes on July 5th. Make sure to clear any outstanding dues and consult your advisor before submitting your final course selection. For any technical issues with the portal, please contact support@university.edu. Regards, Academic Affairs Office."))