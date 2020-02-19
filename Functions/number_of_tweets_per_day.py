def number_of_tweets_per_day(df):
    """Function to tabulate number of tweets tweeted to
    corrresponding date from pandas dataframe input"""
    import pandas as pd
    date_count = {}
    col = df['Date']
    col = [date[:10] for date in col]
    for entry in col:
        if entry in date_count.keys():
            date_count[entry] += 1
        else:
            date_count[entry] = 1
    tpd_frame = pd.DataFrame(date_count.items(), columns=['Date', 'Tweets'])
    tpd_frame = tpd_frame.set_index('Date')
    return tpd_frame
