from uuid import UUID
from rock_paper_scissors.entities import GameBoard, Move
from rock_paper_scissors.interfaces.game_storage import GameStorage
from typing import List, Dict


class RockPaperScissors:

    def __init__(self, game_storage: GameStorage):
        self.game_storage = game_storage

    def player_1_move(self, player_id: UUID, move: Move) -> UUID:
        new_game_board = GameBoard(player_1=player_id, player_1_move=move)
        self.game_storage.save_game(new_game_board)
        return new_game_board.game_id

    def player_2_move(self, game_id: UUID, player_id: UUID, move: Move) -> str:
        game_board = self.game_storage.load_game(game_id)
        game_board.set_player_2_params(player_id, move)
        self.game_storage.save_game(game_board)
        return game_board.check_for_winner()

    def get_open_game_ids(self) -> List[UUID]:
        return self.game_storage.get_open_game_ids()
