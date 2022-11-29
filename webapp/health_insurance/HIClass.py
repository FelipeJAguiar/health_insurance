import pickle
import pandas as pd
import numpy as np

class HIClass():
    def __init__(self):
        self.home_path = ''
        self.annual_premium_scaler = pickle.load(open(self.home_path + 'webapp/features/annual_premium_scaler.pkl', 'rb'))
        self.age_scaler = pickle.load(open(self.home_path + 'webapp/features/age_scaler.pkl', 'rb'))
        self.vintage_scaler = pickle.load(open(self.home_path + 'webapp/features/vintage_scaler.pkl', 'rb'))
        self.target_encode_region_code_scaler = pickle.load(open(self.home_path + 'webapp/features/target_encode_region_code_scaler.pkl', 'rb'))
        self.target_encode_gender_scaler = pickle.load(open(self.home_path + 'webapp/features/target_encode_gender_scaler.pkl', 'rb'))
        self.fe_policy_sales_channel_scaler = pickle.load(open(self.home_path + 'webapp/features/fe_policy_sales_channel_scaler.pkl', 'rb'))
    
    def feature_engineering(self, df1):
        
        df1['Vehicle_Age'] = df1['Vehicle_Age'].apply(lambda x: 'over_2_years' if x== '> 2 Years' else 'between_1_2_years' if x== '1-2 Year' else 'below_1_year')
        
        df1['Vehicle_Damage'] = df1['Vehicle_Damage'].apply(lambda x: 1 if x== 'Yes' else 0)
        
        return df1
    
    def data_preparation(self, df2):
        # Standardization
        #Annual Premium
        df2['Annual_Premium'] =  self.annual_premium_scaler.transform(df2[['Annual_Premium']].values)
        
        # Rescaling
        #Age
        df2['Age'] = self.age_scaler.transform(df2[['Age']].values)
        
        #Vintage
        df2['Vintage'] = self.vintage_scaler.transform(df2[['Vintage']].values)
        
        # Encoding
        #Gender
        df2.loc[:,'Gender'] = df2['Gender'].map(self.target_encode_gender_scaler)
        
        #Region_Code
        df2.loc[:,'Region_Code'] = df2['Region_Code'].map(self.target_encode_region_code_scaler)
        
        #Policy_Sales_Channel
        df2.loc[:,'Policy_Sales_Channel'] = df2['Policy_Sales_Channel'].map(self.fe_policy_sales_channel_scaler)
        
        #Vehicle_Age
        df2 = pd.get_dummies(df2, prefix='Vehicle_Age', columns=['Vehicle_Age'])
        
        cols_selected = ['Vintage', 'Annual_Premium', 'Age', 'Region_Code', 
                         'Vehicle_Damage', 'Policy_Sales_Channel', 'Previously_Insured']
        
        return df2[cols_selected]
    
    def get_prediction(self, model, original_data, test_data):
        # prediction
        pred = model.predict_proba(test_data)
        
        # join pred into the original data
        original_data['prediction'] = pred[:, 1].tolist()
        
        return original_data.to_json(orient='records', date_format='iso')