import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Use .loc to filter the row where student_id is 101 and select the 'name' and 'age' columns
    return students.loc[students['student_id'] == 101, ['name', 'age']]