from dataclasses import dataclass
import re
from typing import Dict, List, Optional
import common


# parses a single line of the catalog; throw away " bags contain " as it's not
# useful to us and is merely a string anchor.
# group 1: bag color
# group 2: comma separated values of bags and their quantity
CATALOG_LINE_PATTERN = re.compile('^([a-z ]+) bags contain ([a-z 0-9,]+)\.$')

# parses a contains entry into a count and color
# Example expected string: "5 faded blue bags"
# group 1: number of bags
# group 2: color of bag
CATALOG_CONTENT_PATTERN = re.compile('^([0-9]+) ([a-z ]+) bag[s]*')

EMPTY_BAG: str = "no other bags"


@dataclass
class SuitcaseContent:
    count: int
    color: str


class SuitcaseCatalog:
    catalog: Dict

    def __init__(self, raw_entries: List[str]):
        self.catalog = {}

        for entry in raw_entries:
            match = re.match(CATALOG_LINE_PATTERN, entry)
            if match:
                color: str = match.group(1)
                contents: Optional[List[SuitcaseContent]] = self._break_contents(match.group(2))

                self.catalog[color] = contents
            else:
                raise re.error(f'Line does not match pattern, {entry}')

    @staticmethod
    def _break_contents(raw_contents: str) -> Optional[List[SuitcaseContent]]:
        if raw_contents == EMPTY_BAG:
            return None

        contents: List = []
        for entry in raw_contents.split(', '):
            match = re.match(CATALOG_CONTENT_PATTERN, entry)
            if match:
                count: int = int(match.group(1))
                color: str = match.group(2)
                sc = SuitcaseContent(count, color)

                contents.append(sc)
            else:
                raise re.error(f"Contents don't match pattern {entry}")

        return contents

    # This return handling here is very strange due to the fact that we can't use a return keyword within the loop.
    # Doing so ends the for loop and which doesn't traverse the whole tree. If any child contains the desired color,
    # ret will end up being a nonzero number, so we can simply check if that value is not zero
    def contains(self, key: str, color: str) -> bool:
        if self.catalog[key] is None:
            return 0

        ret: int = 0
        for entry in self.catalog[key]:
            if entry.color == color:
                ret += 1
            else:
                ret += self.contains(entry.color, color)

        return bool(ret)

    def count_contains(self, color: str) -> int:
        count: int = 0

        # run the contains function for each color in the catalog
        for key in self.catalog:
            if self.contains(key, color):
                count += 1

        return count


if __name__ == '__main__':
    f = 'day07.txt'
    raw_list = common.read_list(f, str)

    sg      = SuitcaseCatalog(raw_list)
    answer1 = sg.count_contains('shiny gold')

    print(f'Answer 1: {answer1}')
