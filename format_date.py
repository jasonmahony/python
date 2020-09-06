def format_date(date):
    new_date = date.split("/")
    print("".join(reversed(new_date)))


format_date("11/12/2019")