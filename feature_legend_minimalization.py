class FeatureLegendMinialization:

    def one_and_other(self, df, feature, pivot, set_value):
        for i in range(len(df[feature])):
            if df[feature].iloc[i] != pivot:
                df[feature].iloc[i] = set_value
        print('\n== {} feature has been modified =='.format(feature))
        print(df[feature].value_counts()[:5])


    def n_and_other(self, df, feature, pivot, set_value):
        df[feature] = df[feature].astype(str)
        for i in range(len(df[feature])):
            if df[feature].iloc[i] not in pivot:
                df[feature].iloc[i] = set_value

        print('\n== {} feature has been modified =='.format(feature))
        print(df[feature].value_counts()[:5])


    def one_to_one(self, df, feature, pivot, set_value):
        for i in range(len(df[feature])):
            if df[feature].iloc[i] == pivot:
                df[feature].iloc[i] = set_value
        print('\n== {} feature has been modified =='.format(feature))
        print(df[feature].value_counts()[:5])


    def n_to_one(self, df, feature, pivot, set_value):
        df[feature] = df[feature].astype(str)
        for i in range(len(df[feature])):
            if df[feature].iloc[i] in pivot:
                df[feature].iloc[i] = set_value

            temp = all([(s.replace(' ', '') in pivot) for s in df[feature].iloc[i].split(',')])
            if temp == True:
                df[feature].iloc[i] = set_value

#        print('\n== {} feature has been modified =='.format(feature))
#        print(df[feature].value_counts()[:5])
