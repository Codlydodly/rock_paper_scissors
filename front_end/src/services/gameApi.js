
export const fetchOpenGameIDs = async () => {
    try {
        const response = await fetch(`${process.env.REACT_APP_GAME_API_URL}/open_games`);
        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Error getting open game IDs: ', error);
        return [];
    }
};

export const playerOneTurn = async(playerID, move) => {
    const response = await fetch(`${process.env.REACT_APP_GAME_API_URL}/player_1?player_id=${playerID}&move=${move}`);
    const result = await response.json();
    return result;
};

export const playerTwoTurn = async(gameID, playerID, move) => {
    console.log('player 2s turn', gameID, playerID, move);
    const response = await fetch(
        `${process.env.REACT_APP_GAME_API_URL}/player_2?game_id=${gameID}&player_id=${playerID}&move=${move}`
    );
    const result = await response.json();
    console.log('and the winner is: ', result);
    return result;
};
