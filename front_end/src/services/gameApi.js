
export const fetchOpenGameIDs = async () => {
    // try {
        const path = `${process.env.REACT_APP_GAME_API_URL}/open_games`;
        console.log('All Environment Variables:', process.env);
        const response = await fetch(`${process.env.REACT_APP_GAME_API_URL}/open_games`);
        const result = await response.text();
        return result;
    // } catch (error) {
    //     console.error('Error fetching data: ', error);
    //     return [];
    // }
};

const playerOneTurn = async() => {
    return [];
};

const playerTwoTurn = async() => {
    return [];
};

