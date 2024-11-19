from lunarcalendar import Converter, Solar

def convert_solar_to_lunar(year, month, day):
    solar_date = Solar(year, month, day)
    lunar_date = Converter.Solar2Lunar(solar_date)
    return lunar_date
