# rock_paper_scissors

Learning project

Run on Python version: Python 3.9.6

To run you will need the following libs:

pip install fastapi uvicorn

to run the project, use the following command:
python3 -m uvicorn rock_paper_scissors.src.routes:app --reload

then there are two endpoints:
http://127.0.0.1:8000/player_1?player_id=9f466a4a-1af7-4ddf-ba6a-514b55566072&move=Rock
and 
http://127.0.0.1:8000/player_2?game_id=32119960-2e90-4e4e-9ab6-dc683c2fc653&player_id=fccd13b2-7885-43bc-918a-9700c2414315&move=Scissors

possibly on different ports when you run it
