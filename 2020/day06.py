from dataclasses import dataclass
from string import ascii_lowercase
from typing import List

from common import read_blocks


@dataclass
class SurveyResponse:
    answers: str

    def has_affirmative_response(self, char: str) -> bool:
        if char in self.answers:
            return True
        else:
            return False

    def get_answer_set(self) -> set:
        return set(list(self.answers))


class SurveyGroup:
    participants: List[SurveyResponse]

    def __init__(self, group_answers: str):
        self.participants = []

        for line in group_answers.split():
            self.participants.append(SurveyResponse(line))

    def count_unique_entries(self) -> int:
        unique_chars = set()
        for char in ascii_lowercase:
            for participant in self.participants:
                if participant.has_affirmative_response(char):
                    unique_chars.add(char)
                    break

        return len(unique_chars)

    def count_consensus(self) -> int:
        sets = map(lambda x: x.get_answer_set(), self.participants)
        return len(set.intersection(*sets))


def get_yes_summary(survey_groups: List[SurveyGroup]) -> int:
    count: int = 0
    for group in survey_groups:
        count += group.count_unique_entries()

    return count


def get_consensus_summary(survey_groups: List[SurveyGroup]) -> int:
    count: int = 0
    for group in survey_groups:
        count += group.count_consensus()

    return count


if __name__ == '__main__':
    groups = read_blocks('day06.txt', SurveyGroup)

    answer1 = get_yes_summary(groups)
    print(f'Answer 1: {answer1}')

    answer2 = get_consensus_summary(groups)
    print(f'Answer 2: {answer2}')
