import React, { useState, useEffect } from 'react';
import { playerOneTurn, playerTwoTurn } from '../services/gameApi';
import { useParams } from 'react-router-dom';


const RockPaperScissors = (props) => {
    const params = useParams();
    const playerID = props.playerID;
    const [outcome, setOutcome] = useState(null);

    const makeMove = async(move) => {
        const result = await playerTwoTurn(params.gameId, playerID, move);
        setOutcome(result);
    };


    return (
        <div>
            <button onClick={() => makeMove('rock')}>Rock</button>
            <button onClick={() => makeMove('paper')}>Paper</button>
            <button onClick={() => makeMove('scissors')}>Scissors</button>
            <h1>{outcome}</h1>
        </div>    
    );
};

export default RockPaperScissors;
