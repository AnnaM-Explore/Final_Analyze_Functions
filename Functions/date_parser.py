def date_parser(list_dates):
    """Function to extract dates from uniform "date time" list"""
    new_dates = [date[:10] for date in list_dates]
    return new_dates
