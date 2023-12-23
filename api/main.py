from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from user.routers import router as userRouter
from game.routers import router as gameRouter


app = FastAPI(
    title="Rock Paper Scissors API",
    description="Rock Paper Scissors API based game!",
    docs_url="/v1/docs",
    redoc_url="/v1/redoc",
    openapi_url="/v1/openapi.json"
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    # Add frontend URLs here
]

# Allow all origins (replace '*' with specific origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(userRouter)
app.include_router(gameRouter)

#TODO: relocate routes below elsewhere

# @app.get('/player_1')
# def player_1_move(player_id: UUID, move: str) -> UUID:
#     new_move = move_from_str(move)
#     new_game_id = RockPaperScissors(GameStorage()).player_1_move(player_id, new_move)
#     return new_game_id
#
# @app.get('/player_2')
# def player_2_move(game_id: UUID, player_id: UUID, move: str) -> str:
#     new_move = move_from_str(move)
#     result = RockPaperScissors(GameStorage()).player_2_move(game_id, player_id, new_move)
#     return result
#
# @app.get('/open_games')
# def get_open_game_ids() -> List[UUID]:
#     open_game_ids = RockPaperScissors(GameStorage()).get_open_game_ids()
#     return open_game_ids
