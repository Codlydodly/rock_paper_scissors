import sqlite3
from uuid import UUID
from rock_paper_scissors.src.rock_paper_scissors.entities import GameBoard, move_from_str
from typing import Optional


class GameStorage:

    def __init__(self):
        self.db: Optional[sqlite3.Connection] = None

    def mad_hax(self):
        cursor = self._connect()
        cursor.execute('''
            DROP TABLE game_board;
            ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_board (
                game_id TEXT PRIMARY KEY,
                player_1 TEXT NOT NULL,
                player_2 TEXT,
                player_1_move TEXT NOT NULL,
                player_2_move TEXT
            )
        ''')
        self._disconnect(True)

    def load_game(self, game_id: UUID) -> GameBoard:
        cursor = self._connect()
        cursor.execute(
            '''
            SELECT game_id, player_1, player_2, player_1_move, player_2_move
            FROM game_board
            WHERE game_id = ?
            ''',
            (str(game_id),)
        )
        game = cursor.fetchone()
        self._disconnect(False)
        if not game:
            raise Exception('no game')
        return GameBoard(
            game_id=UUID(game[0]),
            player_1=UUID(game[1]),
            player_2=game[2] if game[2] is None else UUID(game[2]),
            player_1_move=move_from_str(game[3]),
            player_2_move=game[4] if game[4] is None else move_from_str(game[4]),
        )

    def save_game(self, game_board: GameBoard):
        cursor = self._connect()
        cursor.execute(
            '''
            INSERT OR REPLACE INTO game_board (game_id, player_1, player_2, player_1_move, player_2_move)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (
                str(game_board.game_id),
                str(game_board.player_1),
                None if game_board.player_2 is None else str(game_board.player_2),
                game_board.player_1_move.name,
                game_board.player_2_move.name,
            )
        )
        self._disconnect(True)

    def _connect(self):
        self.db = sqlite3.connect('your_database.db')
        return self.db.cursor()

    def _disconnect(self, commit: bool):
        if commit:
            self.db.commit()
        self.db.close()



