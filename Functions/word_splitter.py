def word_splitter(df):
    """This will take list of words split them and return df"""
    df['Split Tweets'] = df['Tweets'].apply(str.lower)
    df['Split Tweets'] = df['Split Tweets'].apply(str.split)
    return df