
export const fetchOpenGameIDs = async () => {
    try {
        const response = await fetch('http://localhost:8000/open_games');
        const result = await response.json();
        console.log('================HELLO ZACH=================')
        console.log(result.data)
        return result.data;
    } catch (error) {
        console.error('Error fetching data: ', error);
        return [];
    }
};

const playerOneTurn = async() => {
    return [];
};

const playerTwoTurn = async() => {
    return [];
};

