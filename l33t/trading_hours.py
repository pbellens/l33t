'''
Given a list of trading hours for several firms, determine 
whether a given time period is covered by the trading hours.
E.g. 
12:00 - 16:00       Deutsche Boerse
10:00 - 14:00       Bloomberg
18:00 - 20:00       Refinitiv

Jimmy wants to trade from 15:00 until 19:00 -> False
Lionel trades from 11:00h until 16:00 -> True
'''


from dataclasses import dataclass
import enum
import typing

@dataclass
class TradingHour:
    begin: int
    end: int

class Overlap(enum.Enum): 
    Left = enum.auto()
    Right = enum.auto()
    Included= enum.auto()
    Includes= enum.auto()
    Nolap= enum.auto()

def overlaps(t1: TradingHour, t2: TradingHour) -> Overlap:
    overlapright = t1.begin > t2.begin and t1.begin < t2.end
    overlapleft = t1.end > t2.begin and t1.end < t2.end
    included = overlapleft and overlapright
    includes = t1.begin < t2.begin and t1.end > t2.end
    if included:
        return Overlap.Included
    elif includes:
        return Overlap.Includes
    elif overlapright:
        return Overlap.Right
    elif overlapleft:
        return Overlap.Left
    else:
        return Overlap.Nolap


def merge_hours(t1: TradingHour, t2: TradingHour, overlap: Overlap) -> TradingHour: 
    if overlap is Overlap.Included:
        return t2
    elif overlap is Overlap.Includes:
        return t1
    elif overlap is Overlap.Right:
        return TradingHour(begin = t2.begin, end = t1.end)
    else:
        return TradingHour(begin = t1.begin, end = t2.end)


class TradingProviders:
    def __init__(self, provided_hours: typing.Sequence[TradingHour]):
        sorted_hours = sorted(provided_hours, key = lambda h: (h.begin, h.end))
        self.hours 
    

