# -*- coding: utf-8 -*-
from collections import deque
from pathlib import Path
from pygerber.mathclasses import BoundingBox
from typing import Tuple

from pygerber.meta import Meta
from pygerber.meta.apertureset import ApertureSet
from pygerber.tokens.token import Token

from .exceptions import (
    EndOfStream,
    InvalidSyntaxError,
    TokenNotFound,
    TokenizationFatalFailure,
)
from .tokens import token_classes


DEFAULT_TRACE_FILEPATH = "<string>"


class Tokenizer:

    token_stack: deque  # contains Token objects
    meta: Meta
    source: str = ""
    begin_index: int = 0
    token_stack_size: int = 0
    file_path: str = None
    bbox: BoundingBox

    def __init__(
        self, apertureSet: ApertureSet, *, ignore_deprecated: bool = True
    ) -> None:
        self.token_stack = deque()
        self.apertureSet = apertureSet
        self.ignore_deprecated = ignore_deprecated
        self.meta = Meta(self.apertureSet, ignore_deprecated=self.ignore_deprecated)
        self.reset_state()
        self.bbox = None

    def reset_state(self):
        self.meta.reset_defaults()
        self.begin_index = 0
        self.char_index = 0
        self.line_index = 1

    def render(self) -> None:
        """
        Render all tokens contained in token_stack.
        """
        try:
            for token in self.token_stack:
                self.__render_token(token)
        except EndOfStream:
            return

    def __render_token(self, token: Token) -> None:
        token: Token
        token.affect_meta()
        token.pre_render()
        token.render()
        token.post_render()

    def tokenize_file(self, file_path: str) -> deque:
        """
        Opens file that file_path is pointing to and tokenizes its contents.
        Deque containing all of the tokens is returned.
        """
        self.file_path = file_path
        source = self.load_file()
        return self.tokenize_string(source)

    def load_file(self) -> str:
        with open(self.file_path, "r", encoding="utf-8") as file:
            source = file.read()
        return source

    def tokenize_string(self, string: str) -> deque:
        """
        Tokenizes source string, assuming that it contains Gerber code.
        Deque containing all of the tokens is returned.
        """
        self.source = string
        return self.tokenize()

    def tokenize(self) -> deque:
        try:
            while not self.__has_reached_end():
                self.__next_token()
        except EndOfStream:
            pass
        except InvalidSyntaxError as e:
            raise e.__class__(
                f"""File "{self.__get_abspath_if_possible()}", line {self.line_index}, character {self.char_index}:\n{e}"""
            ) from e
        else:
            raise InvalidSyntaxError(
                "No explicit indication of end at the end of file."
            )
        self.reset_state()
        return self.token_stack

    def __get_abspath_if_possible(self):
        if self.file_path is None:
            return DEFAULT_TRACE_FILEPATH
        else:
            return Path(self.file_path).absolute()

    def __has_reached_end(self):
        return self.begin_index >= len(self.source)

    def __next_token(self) -> int:
        token: Token = self.__find_matching_token()
        token.dispatch(self.meta)
        self.push_token(token)
        self.__update_indexes(token)
        token.affect_meta()
        token.pre_render()
        self.__update_bbox(token.bbox())
        token.post_render()

    def __update_bbox(self, bbox: BoundingBox):
        if bbox is not None:
            if self.bbox is None:
                self.bbox = bbox
            else:
                self.bbox += bbox

    def push_token(self, token: Token) -> None:
        if token.keep == True:
            self.token_stack.append(token)
            self.token_stack_size += 1

    def __update_indexes(self, token: Token) -> None:
        # update begin index
        self.begin_index = token.re_match.end()
        matched_string: str = token.re_match.group()
        endl_count = matched_string.count("\n")
        # update line index
        self.line_index += endl_count
        source_length = len(matched_string)
        # update char index
        if endl_count == 0:
            self.char_index += source_length
        else:
            last_endl_index = matched_string.rfind("\n")
            self.char_index = source_length - last_endl_index

    def __find_matching_token(self):
        for token_class in token_classes:
            if token := token_class.match(
                self.source,
                self.begin_index,
            ):
                return token
        else:
            self.raise_token_not_found()

    def raise_token_not_found(self):
        end_index = min(len(self.source), self.begin_index + 30)
        raise TokenNotFound(f"{self.source[self.begin_index:end_index]}")

    def get_bbox(self):
        if self.bbox is not None:
            return self.bbox
        else:
            return BoundingBox(0, 0, 0, 0)