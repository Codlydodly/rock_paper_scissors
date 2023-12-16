from uuid import UUID
from rock_paper_scissors.game import RockPaperScissors
from rock_paper_scissors.entities import move_from_str
from rock_paper_scissors.interfaces.game_storage import GameStorage
from fastapi import FastAPI
from typing import List


app = FastAPI()


@app.get('/player_1')
def player_1_move(player_id: UUID, move: str) -> UUID:
    new_move = move_from_str(move)
    new_game_id = RockPaperScissors(GameStorage()).player_1_move(player_id, new_move)
    return new_game_id


@app.get('/player_2')
def player_2_move(game_id: UUID, player_id: UUID, move: str) -> str:
    new_move = move_from_str(move)
    result = RockPaperScissors(GameStorage()).player_2_move(game_id, player_id, new_move)
    return result


@app.get('/open_games')
def get_open_game_ids() -> List[UUID]:
    open_game_ids = RockPaperScissors(GameStorage()).get_open_game_ids()
    return open_game_ids
