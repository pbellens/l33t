from dataclasses import dataclass
import typing


@dataclass
class ConversionPair:
    first: str
    second: str
    factor: float

    def reverse(self):
        return ConversionPair(first = self.second, second = self.first, factor = 1 / self.factor)


def close(table: typing.Dict, p: ConversionPair) -> typing.Dict:
    changes = [p]
    while changes:
        c = changes.pop()
        present = (c.first, c.second) in table.keys()
        if not present:
            for (ks,f) in table.items():
                if ks[1] == c.first and ks[0] != c.second:
                    changes.append(ConversionPair(first = ks[0], second = c.second, factor = f * c.factor))
                elif c.second == ks[0] and c.first != ks[1]:
                    changes.append(ConversionPair(first = c.first, second = ks[1], factor = f * c.factor))
            table[(c.first, c.second)] = c.factor
    return table
    
def build_metrics(cpairs: typing.Sequence[ConversionPair]) -> typing.Dict:
    res = {}
    for cp in cpairs:
        res = close(res, cp)
        res = close(res, cp.reverse())
    return res


if __name__ == '__main__':
    facts = [
        ConversionPair(first = 'm', second = 'ft', factor = 3.28),
        ConversionPair(first = 'ft', second = 'in', factor = 12.0),
        ConversionPair(first = 'hr', second = 'min', factor = 60.0),
        ConversionPair(first = 'min', second = 'sec', factor = 60.0),
    ]
    metrics = build_metrics(facts)

    queries = [(2, 'm', 'in'), (13, 'in', 'm'), (13, 'in', 'h')]
    for q in queries:
        if (q[1], q[2]) in metrics.keys():
            print(f'{q[0]} {q[1]} = {q[0] * metrics[(q[1], q[2])]} {q[2]}')
        else:
            print(f'Could not convert between {q[1]} and {q[2]}')
