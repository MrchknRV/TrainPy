from datetime import datetime, timedelta


def date_format(dates):
    results = []
    for date in dates:
        date_obj = datetime.strptime(date, "%Y.%m.%d")
        new_time_obj = date_obj + timedelta(days=7)
        results.append(new_time_obj.strftime("%B %#d, %Y"))
    return results


if __name__ == "__main__":
    assert date_format(["2022.12.31", "2023.1.7"]) == ['January 7, 2023', 'January 14, 2023']
    assert date_format([]) == []
    print("ok")