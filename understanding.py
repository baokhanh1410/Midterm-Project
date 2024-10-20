import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------BUSINESS PROBLEMS-------------------------------

# Q1: WHICH CUSTOMER HAS THE HIGHEST PROBABILITY TO LEAVE
#  --> Một số các features quan trọng cần phải phân tích là: Age, City, Monthly Charges, Total Charges, Customer Status, Churn Reason, Tenure in Months
#  --> Sau khi phân tích các features thì tìm ra nguyên nhân tại sao lại xuất hiện tình trạng customer churn

# Q2: WHAT COULD BE THE REASON WHY CUSTOMER CHURN HAPPENING



# -------------------------------LOADING DATA-------------------------------
df = pd.read_csv('Midterm Project/Dataset/telecom_customer_churn.csv')


# NUMERICAL DATA
df_num = df.select_dtypes(exclude=['bool_','object_'])

# CATERICAL DATA
df_cat = df.select_dtypes(exclude=['number','bool_',])

# -------------------------------UNDERSTANDING DATA-------------------------------


# Có tổng cộng 38 Features
# print(df.columns.to_list())

# Kiếm tra các giá trị null trong các Features
null_values = df.isnull().sum()
print(null_values[null_values>0])
# Offer                                3877
# Avg Monthly Long Distance Charges     682
# Multiple Lines                        682
# Internet Type                        1526
# Avg Monthly GB Download              1526
# Online Security                      1526
# Online Backup                        1526
# Device Protection Plan               1526
# Premium Tech Support                 1526
# Streaming TV                         1526
# Streaming Movies                     1526
# Streaming Music                      1526
# Unlimited Data                       1526
# Churn Category                       5174
# Churn Reason                         5174














df_churnReason = df_cat["Churn Reason"].dropna()
print(df_churnReason.mode())
# Competitor had better devices là nguyên nhân chính dẫn đến customer churn

