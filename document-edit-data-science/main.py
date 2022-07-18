import pandas as pd

data = pd.read_csv("/Users/hazalsenturk/Desktop/UDEMY/Complete 2020 Data Science & Machine Learning Bootcamp/section 2/cost_revenue_dirty.csv")
df = pd.DataFrame(data)

data_sorted = df.sort_values(by=["Worldwide Gross ($)", "Domestic Gross ($)"], ascending=False)
data_sorted = data_sorted.rename(columns=lambda x: x.replace("($)",""))
data_sorted = data_sorted.rename(columns=lambda x: x.strip().replace(' ','_'))
data_valid = data_sorted[(data_sorted.Worldwide_Gross != "$0") & (data_sorted.Domestic_Gross != "$0")]
data_cleaned = data_valid.drop(columns=['Rank', 'Release_Date', 'Movie_Title', 'Domestic_Gross'])
data_cleaned["Worldwide_Gross"] = data_cleaned["Worldwide_Gross"].str.replace('$', '')
data_cleaned["Production_Budget"] = data_cleaned["Production_Budget"].str.replace('$', '')
data_cleaned["Worldwide_Gross"] = data_cleaned["Worldwide_Gross"].str.replace(',.', '').astype(float)
data_cleaned["Production_Budget"] = data_cleaned["Production_Budget"].str.replace(',.', '').astype(float)
data_cleaned.to_csv("/Users/hazalsenturk/Desktop/UDEMY/Complete 2020 Data Science & Machine Learning Bootcamp/section 2/cost_revenue_clean.csv")