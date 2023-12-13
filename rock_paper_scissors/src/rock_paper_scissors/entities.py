from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4, UUID
from typing import Optional

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

DRAW = 'Draw'
WIN = 'Win'
LOSE = 'Lose'


WHAT_BEATS_WHAT = {
    SCISSORS: PAPER,
    PAPER: ROCK,
    ROCK: SCISSORS
}


@dataclass
class Move:
    name: str = None


@dataclass
class Rock(Move):
    name: str = ROCK


@dataclass
class Paper(Move):
    name: str = PAPER


@dataclass
class Scissors(Move):
    name: str = SCISSORS


def move_from_str(move_as_str: str) -> Move:
    input_str = move_as_str.lower()
    if input_str == ROCK:
        return Rock()
    elif input_str == PAPER:
        return Paper()
    elif input_str == SCISSORS:
        return Scissors()

    raise Exception("uh oh stinky")


@dataclass
class GameBoard:
    player_1: UUID
    player_1_move: Move

    player_2: Optional[UUID] = None
    player_2_move: Optional[Move] = Move()

    game_id: UUID = uuid4()

    def __str__(self):
        return f'Game ID: {self.game_id}, ' \
               f'Player 1 Move: {self.player_1_move}, ' \
               f'Player 2 Move: {self.player_2_move}'

    def set_player_2_params(self, player_2_id: UUID, player_2_move: Move):
        self.player_2 = player_2_id
        self.player_2_move = player_2_move

    def check_for_winner(self) -> str:
        if WHAT_BEATS_WHAT.get(self.player_1_move.name) == self.player_2_move.name:
            return LOSE
        elif WHAT_BEATS_WHAT.get(self.player_2_move.name) == self.player_1_move.name:
            return WIN
        else:
            return DRAW
