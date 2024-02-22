from datetime import datetime
from dateutil import tz
from enum import Enum


class Format(Enum):
    DATE_TIME = "%Y-%m-%d %H:%M:%S"
    DATE = "%Y-%m-%d"


class Timezone(Enum):
    Tokyo = 'Asia/Tokyo'
    HCM = 'Asia/Ho_Chi_Minh'


def get_current(fmt: Format = Format.DATE_TIME, timezone=Timezone.HCM):
    return datetime.now(tz=tz.gettz(timezone.value)).strftime(fmt.value)


def get_time(time: str = "0001-01-01 00:00:00", fmt: Format = Format.DATE_TIME) -> datetime.date:
    return datetime.fromisoformat(time)


def get_time_str(time: datetime, fmt: Format = Format.DATE_TIME):
    return time.strftime(fmt.value)
