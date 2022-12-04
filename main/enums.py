from enum import Enum


class QuestionType(str, Enum):
    TEXT = "text"
    MULTIPLE_CHOICE = "multiple_choice"
