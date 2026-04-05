import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # Merge tables
    df = employee.merge(bonus, on='empId', how='left')
    # Filter for bonus < 1000 or NaN (null)
    result = df[(df['bonus'] < 1000) | (df['bonus'].isna())]
    # Return only required columns
    return result[['name', 'bonus']]