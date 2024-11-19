def calculate_stem_and_branch(year):
    heavenly_stems = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
    earthly_branches = ['Tí', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']

    year_stem = heavenly_stems[(year - 4) % 10]
    year_branch = earthly_branches[(year - 4) % 12]

    return year_stem, year_branch


def calculate_stem_and_branch_for_month(year, month):
    heavenly_stems = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
    earthly_branches = ['Tí', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']

    month_stem = heavenly_stems[(year * 12 + month - 1) % 10]
    month_branch = earthly_branches[(year * 12 + month - 1) % 12]

    return month_stem, month_branch


def calculate_stem_and_branch_for_day(year, day):
    heavenly_stems = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
    earthly_branches = ['Tí', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']

    day_stem = heavenly_stems[(year * 365 + day - 1) % 10]
    day_branch = earthly_branches[(year * 365 + day - 1) % 12]

    return day_stem, day_branch


def calculate_stem_and_branch_for_hour(year, hour):
    heavenly_stems = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
    earthly_branches = ['Tí', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']

    hour_stem = heavenly_stems[(year * 24 + hour) % 10]
    hour_branch = earthly_branches[(year * 24 + hour) % 12]

    return hour_stem, hour_branch
