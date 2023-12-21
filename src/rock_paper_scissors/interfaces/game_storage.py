import sqlite3
from uuid import UUID
from rock_paper_scissors.entities import GameBoard, move_from_str
from typing import Optional, List, Dict


class GameStorage:

    def __init__(self):
        self.db: Optional[sqlite3.Connection] = None

    def mad_hax(self):
        cursor = self._connect()
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
        return self._rows_to_gameboard([game])[0]

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

    def get_open_game_ids(self) -> List[UUID]:
        cursor = self._connect()
        cursor.execute('SELECT game_id FROM game_board WHERE player_2 IS NULL AND player_2_move IS NULL')

        results = cursor.fetchall()
        self._disconnect(False)
        return [UUID(row[0]) for row in results]

    def _rows_to_gameboard(self, rows: List[tuple[str]]) -> List[GameBoard]:
        return [
            GameBoard(
                game_id=UUID(row[0]),
                player_1=UUID(row[1]),
                player_2=row[2] if row[2] is None else UUID(row[2]),
                player_1_move=move_from_str(row[3]),
                player_2_move=row[4] if row[4] is None else move_from_str(row[4]),
            )
            for row in rows
        ]



    def _connect(self):
        self.db = sqlite3.connect('your_database.db')
        return self.db.cursor()

    def _disconnect(self, commit: bool):
        if commit:
            self.db.commit()
        self.db.close()



