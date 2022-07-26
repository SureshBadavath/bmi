class BMI:
    def __init__(self):
        self.calculate_bmi = lambda h, w : round(w/((h/100)**2), 2)

    def get_category_and_risk(self, bmi):
        if bmi <= 18.4:
            return 'Underweight', 'Malnutrition risk'
        elif bmi >=18.5 and bmi <= 24.9:
            return 'Normal weight', 'Low risk'
        elif bmi >=25 and bmi <= 29.9:
            return 'Overweight', 'Enhanced risk'
        elif bmi >=30 and bmi <= 34.9:
            return 'Moderately obese', 'Medium risk'
        elif bmi >= 35 and bmi <= 39.9:
            return 'Severely obese', 'High risk'
        elif bmi > 40:
            return 'Very severely obese', 'Very high risk'

    def bmi_check_up(self, height, weight, ow_counter):
        bmi, category, risk = None, None, None
        if isinstance(height, (int, float)) and isinstance(weight, (int, float)):
            if height > 0 and weight > 0 and height != None and weight != None:
                bmi = self.calculate_bmi(height, weight)
                category, risk = self.get_category_and_risk(bmi)
                status = 'Calculated'
                if category == 'Overweight':
                    ow_counter = ow_counter + 1
            else:
                status = 'Not Calculated - Check Inputs - Values are wrong'
        else:
            status = 'Not Calculated - Check Inputs - Types are wrong'
        return bmi, ow_counter, category, risk, status 

INPUT_PATH = 'bmi/input.json'
bmi_ = BMI()

# Adding additional status column though not defined in req

def bmi_by_json():
    bmi_data = []
    ow_counter = 0
    f = open(INPUT_PATH)
    inputs = json.load(f)
    for input_ in inputs:
        try:
            gender = input_['Gender']
            height = input_['HeightCm']
            weight = input_['WeightKg']
            bmi, ow_counter, category, risk, status = bmi_.bmi_check_up(height, weight, ow_counter)
        except KeyError:
            status = 'Not Calculated - Check Inputs - Key Missing'
        row = [gender, height, weight, bmi, category, risk, status]
        bmi_data.append(row)
    return bmi_data, ow_counter 

def write_csv(bmi_data):
    with open('BMI_Output.csv', 'w',newline='') as file:
        csv_ = csv.writer(file, delimiter=',')
        headers = ['Gender', 'Height', 'Weight', 'Categoty', 'Risk', 'Row_Status']
        csv_.writerow(headers)
        csv_.writerows(bmi_data)

def bmi_by_df():
    ow_counter = 0
    df = pd.read_json(INPUT_PATH)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    if len(df) >=1:
        for index, row in df.iterrows():
            height = row['HeightCm']
            weight = row['WeightKg']
            bmi, ow_counter, category, risk, status = bmi_.bmi_check_up(height, weight, ow_counter)
            df.loc[index, "BMI"], df.loc[index, "Category"], df.loc[index, "Risk"], df.loc[index, "Row_Status"] = bmi, category, risk, status
    else:
        print('Check Inputs')
    return df, ow_counter

if __name__ == '__main__':
    # # Option 1 
    import csv
    import json  
    bmi_data, ow_counter = bmi_by_json()
    write_csv(bmi_data)

    # Option 2 - Data frames 
    import pandas as pd
    df, ow_counter = bmi_by_df()
    df.to_json('BMI_Output.json', lines=True, orient='records')

    print(f'Total number of Overweight people : {ow_counter}')