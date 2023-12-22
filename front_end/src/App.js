import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import GameIDTable from './components/gameListTable';
import RockPaperScissors from './components/rockPaperScissors';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<GameIDTable />} />
        <Route path="/game/:gameId" element={<RockPaperScissors />} />
      </Routes>
    </Router>
  );
};

export default App;
