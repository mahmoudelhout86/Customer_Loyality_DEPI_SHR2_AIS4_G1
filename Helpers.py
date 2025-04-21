import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")
from IPython.core.interactiveshell import InteractiveShell
import scipy.stats as stats
from datetime import datetime





#crdits:https://github.com/heba14101998/Elo-customer-loyalty-score-prediction.ipynb/
# use the following to suppress scientific notation in Pandas
pd.set_option('display.float_format', lambda x: '%.3f' % x)
# Set the maximum number of rows and columns to display
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

sns.set_context('talk')
InteractiveShell.ast_node_interactivity = "all"

colors = sns.cubehelix_palette(20,reverse = True, light= 0.01,dark = 0.5, gamma= 0.7)
palette_color  = sns.color_palette("RdBu",20)
sns.set_theme(style="whitegrid", palette=palette_color)


##############################################################

# crdits: https://www.kaggle.com/fabiendaniel/elo-world
def reduce_mem_usage(df, verbose=True):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    start_mem = df.memory_usage().sum() / 1024**2
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
    end_mem = df.memory_usage().sum() / 1024**2
    if verbose: print('Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)'.format(end_mem, 100 * (start_mem - end_mem) / start_mem))
    return df.dtypes


#checking missing values :
def CheckMissing(df):
    missing = df.isna().sum().sort_values(ascending = False)
    missing = missing[missing > 0]
    if not missing.empty:
        missing_percent = missing / len(df) * 100

        missing_df = pd.DataFrame({
            'Feature': missing.index,
            'NumMissing': missing.values,
            'PercentMissing':missing_percent.values,
            'NumUnique': df[missing.index].nunique().values,
            'MostCommon': df[missing.index].mode().iloc[0].values
        })
        return missing_df
    else:
        print("Dataset has No Nulls")
        return 0


## checking outliers

def IQROutlierCheck(df, col):

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    # Get outliers
    outliers = df[(df[col] < lower) | (df[col] > upper)]

    return outliers



def OutliersInfo(df, cols):
    outlier_dict = {}

    for col in cols:
        print(f"\n{col}")
        print("-" * 35)

        # Detect outliers
        critic_outliers = IQROutlierCheck(df, col)
        outlier_dict[col] = critic_outliers.index.tolist()

        # Print number of outliers
        print(f"Number of outlier samples produced by IQR: {critic_outliers.shape[0]}")

        # Print extreme percentile values
        for i in [0, 1, 98, 99, 100]:
            print(f"{i}% percentile value is {np.percentile(df[col], i):.3f}")

        # Count values below 1st percentile
        percent_1 = np.percentile(df[col], 1)
        count_1 = (df[col] < percent_1).sum()
        print(f"\n\t- Number of values less than {percent_1:.3f}: {count_1}")

        # Count values above 99th percentile
        percent_99 = np.percentile(df[col], 99)
        count_99 = (df[col] > percent_99).sum()
        print(f"\t- Number of values greater than {percent_99:.3f}: {count_99}")

    return outlier_dict


def SeparateOutliers(df, col):
    outliers = IQROutlierCheck(df, col)
    df_clean = df.drop(outliers.index)  # Remove outliers from original data
    # Calculate statistics
    mean_clean = df_clean[col].mean()
    std_clean = df_clean[col].std()

    mean_outliers = outliers[col].mean()
    std_outliers = outliers[col].std()

    # Print results
    print(f" Separated {outliers.shape[0]} outliers from '{col}'\n")
    print(f"**Statistics for Non-Outliers**:")
    print(f"   - Mean: {mean_clean:.3f}")
    print(f"   - Standard Deviation: {std_clean:.3f}\n")

    if not outliers.empty:  # Check if there are any outliers
        print(f" **Statistics for Outliers**:")
        print(f"   - Mean: {mean_outliers:.3f}")
        print(f"   - Standard Deviation: {std_outliers:.3f}")
    else:
        print(" No outliers detected!")

    return df_clean, outliers
