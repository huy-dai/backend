from dateparser.search import search_dates
import re
import calendar


def expand_event_time(text):
    # remmove pipelines
    text = re.sub(r'\|', "", text)

    # move dates closer to month
    for month in calendar.month_name[1:]:
        text = re.sub('{month}\s+'.format(month=month),
                      month, text, flags=re.IGNORECASE)
        text = re.sub(
            '{month}\s+'.format(month=month[:3]), month, text, flags=re.IGNORECASE)

    # crazy specific 10-4 pm edge case
    text = re.sub(r'(9|10|11|12)-([1-5])\s*(pm)',
                  r'\1AM - \2\3', text, flags=re.IGNORECASE)
    # 1 to 3 pm
    text = re.sub(r'(10|11|12|[1-9])\s*(?:to)\s*(10|11|12|[1-9])\s*([ap][m])',
                  r'\1\3 - \2\3', text, flags=re.IGNORECASE)
    # 1-3 pm
    text = re.sub(r'(10|11|12|[1-9])\s*-\s*(10|11|12|[1-9])\s*([ap][m])',
                  r'\1\3 - \2\3', text, flags=re.IGNORECASE)

    # merge ams and pms spaces
    text = re.sub(
        r'(10|11|12|[0-9](:[0-9]{2})?)\s+([ap]m)', r'\1\3', text, flags=re.I)

    # Add minutes
    text = re.sub(r'(10|11|12|[0-9])([ap]m)', r'\1:00\2', text, flags=re.I)

    return text


def parse_dates(text):
    test_strings = ["AM", "PM", "NOON", "NIGHT"]
    matches = parse_dates_possibilities(text)
    # Now we need to find the actual dates
    if not matches:
        return None
    # Start by looking forwards and finding the first one with an AM or PM
    i = 0
    start_date = None
    while i < len(matches):
        matched_string, potential_date = matches[i]
        if (any([t in matched_string for t in test_strings])):
            if start_date:
                return [start_date, potential_date]
            else:
                start_date = potential_date
        i += 1
    if start_date:
        return [start_date]
    return None


def parse_dates_possibilities(text):
    text = expand_event_time(text.upper())
    matches = search_dates(text, languages=['en'])
    return matches


if __name__ == "__main__":
    f = open("test_dates.txt", "r")
    for l in f.readlines():
        print(l.strip())
        print(parse_dates_possibilities(l.strip()))
        print(parse_dates(l.strip()))
