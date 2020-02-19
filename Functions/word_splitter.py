
def word_splitter(df):
    
    twitter_df = df
    twitter_df['Split Tweets'] = twitter_df['Tweets'].apply(str.lower)
    twitter_df['Split Tweets'] = twitter_df['Split Tweets'].apply(str.split)
    
    return twitter_df