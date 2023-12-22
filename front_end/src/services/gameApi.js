
export const fetchOpenGameIDs = async () => {
    try {
        const response = await fetch(`${process.env.REACT_APP_GAME_API_URL}/open_games`);
        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Error fetching data: ', error);
        return [];
    }
};

export const playerOneTurn = async() => {
    return [];
};

export const playerTwoTurn = async() => {
    return [];
};

