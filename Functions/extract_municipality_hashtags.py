def extract_municipality_hashtags(df):
    """Function to copy hashtags and municipality
    from pandas dataframe column Tweets and populate
    them each to a column respectively"""
    import numpy as np
    import pandas as pd
    mun_dict = {'@CityofCTAlerts': 'Cape Town',
                         '@CityPowerJhb': 'Johannesburg',
                         '@eThekwiniM': 'eThekwini',
                         '@EMMInfo': 'Ekurhuleni',
                         '@centlecutility': 'Mangaung',
                         '@NMBmunicipality': 'Nelson Mandela Bay',
                         '@CityTshwane': 'Tshwane'}

    def extract_hashtags(tweet):
        return [word.lower() for word in tweet.split() if word.startswith('#')] or np.nan

    def extract_municipality(tweet):
        return [word for word in tweet.split() if word in mun_dict] or np.nan

    df['municipality'] = df['Tweets'].apply(extract_municipality)
    df['hashtags'] = df['Tweets'].apply(extract_hashtags)
    return df
