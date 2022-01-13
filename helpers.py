# get upper and lower thresholds
def get_outlier_thresholds(df, col, q1=0.01, q3=0.99):
    Q1 = df[col].quantile(q1)  # find q1 quantile
    Q3 = df[col].quantile(q3)  # find q3 quantile
    IQR = Q3 - Q1  # Interquartile value
    UPPER = Q3 + 1.5 * IQR  # upper threshold limit
    LOWER = Q1 - 1.5 * IQR  # lower threshold limit
    return UPPER, LOWER


# replace outliers with upper threshold or lower threshold
def replace_with_thresholds(df, col):
    upper, lower = get_outlier_thresholds(df, col)
    df.loc[(df[col] < lower), col] = lower
    df.loc[(df[col] > upper), col] = upper


# get prepared retail data set
def retail_data_prep(df):
    df.dropna(inplace=True)  # drop null
    df = df[~df["Invoice"].str.contains("C", na=False)]  # remove returned product
    df = df[df["Quantity"] > 0]   # quantity cannot be below zero
    df = df[df["Price"] > 0]  # price cannot be below zero

    # outliers
    replace_with_thresholds(df, "Quantity")
    replace_with_thresholds(df, "Price")
    return df


def reduce_mem_usage(df):
    import numpy as np
    """ iterate through all the columns of a dataframe and modify the data type
        to reduce memory usage.
    """
    start_mem = df.memory_usage().sum() / 1024 ** 2
    print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:
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
        else:
            df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024 ** 2
    print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))

    return df
