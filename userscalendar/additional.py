def give_month_for_data(i):
    if i in range(1, 31):
        return "September"

    if i in range(31, 62):
        return "October"

    if i in range(62, 92):
        return "November"

    if i in range(92, 123):
        return "December"

    if i in range(123, 154):
        return "January"

    if i in range(154, 183):
        return "February"

    if i in range(183, 214):
        return "March"

    if i in range(214, 244):
        return "April"

    if i in range(244, 275):
        return "May"

    if i in range(275, 305):
        return "June"

    if i in range(305, 336):
        return "July"

    if i in range(336, 368):
        return "August"


def i_to_month_day(i):
    if i in range(1, 31):
        return i

    if i in range(31, 62):
        return i - 30

    if i in range(62, 92):
        return i - 61

    if i in range(92, 123):
        return i - 91

    if i in range(123, 154):
        return i - 122

    if i in range(154, 183):
        return i - 153

    if i in range(183, 214):
        return i - 182

    if i in range(214, 244):
        return i - 213

    if i in range(244, 275):
        return i - 243

    if i in range(275, 305):
        return i - 274

    if i in range(305, 336):
        return i - 304

    if i in range(336, 368):
        return i - 335
