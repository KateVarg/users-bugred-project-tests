import dataclasses


@dataclasses.dataclass
class SearchUser:
    start_date_year: str
    start_date_month: str
    start_date_day: str
    end_date_year: str
    end_date_month: str
    end_date_day: str
    name: str
