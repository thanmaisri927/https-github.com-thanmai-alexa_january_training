import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder

def one_hot_encode(df, column):
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    encoded = encoder.fit_transform(df[[column]])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out([column]))
    df = df.drop(column, axis=1)
    return pd.concat([df, encoded_df], axis=1)

def label_encode(df, column):
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    return df

def ordinal_encode(df, column, categories):
    encoder = OrdinalEncoder(categories=[categories])
    df[column] = encoder.fit_transform(df[[column]])
    return df

def frequency_encode(df, column):
    freq_map = df[column].value_counts(normalize=True)
    df[column + '_freq'] = df[column].map(freq_map)
    return df

def target_encode(df, column, target):
    mean_target = df.groupby(column)[target].mean()
    df[column + '_target_enc'] = df[column].map(mean_target)
    return df
