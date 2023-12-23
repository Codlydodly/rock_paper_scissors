import React from 'react';
import { v4 } from 'uuid';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import GameIDTable from './components/gameListTable';
import RockPaperScissors from './components/rockPaperScissors';


const App = () => {
  const playerID = v4();

  return (
    <Router>
      <Routes>
        <Route path="/" element={<GameIDTable />} />
        <Route path="/game/:gameId" element={<RockPaperScissors playerID={playerID} />} />
      </Routes>
    </Router>
  );
};

export default App;
