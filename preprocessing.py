def init_dataframe(df, feature_idx, row_start_idx):
    new = df.iloc[row_start_idx:, :]
    new.columns = df.iloc[feature_idx, :]
    print('== Dataframe Initialization ==')
    print('Before : {} / After : {}'.format(df.shape, new.shape))
    return new


def set_dataframe_priorities(df, priorities):
    """ type(priorities) == 'list' """
    new = df[priorities]
    print('\n== Set Dataframe Only Priority Columns == ')
    print('Before : {} / After : {}'.format(df.shape, new.shape))
    return new


def drop_missing_features(df):
    drops = [c for c in df.columns if df[c].isnull().sum() > 500 and c != 'Postop_Chemo_Regimen']
    new = df.drop(drops, axis = 1)
    print('\n== Missing Features Has Been Dropped ==')
    for c in drops:
        print('-', c)
    print('\nBefore : {} / After : {}'.format(df.shape, new.shape))
    return new


def drop_time_features(df, time_features):
    new = df.drop(time_features, axis=1)
    print('\n== Time Features Has Been Dropped ==')
    for c in time_features:
        print('-', c)
    print('\nBefore : {} / After : {}'.format(df.shape, new.shape))
    return new


def drop_NA_instances(df):
    new = df.dropna()
    print('\n== Drop NA instances ==')
    print('Before : {} / After : {}'.format(df.shape, new.shape))
    return new


def numerical_preprocessing(df, numerical_features):
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])
    return df
