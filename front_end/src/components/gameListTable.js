import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { fetchOpenGameIDs } from '../services/gameApi';


const GameIDTable = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchDataFromApi = async () => {
      const result = await fetchOpenGameIDs();
      setData(result);
    };
 
    fetchDataFromApi();
  }, []);

  return (
    <div>
      <h1>Game List</h1>
      <table>
        <thead>
          <tr>
            <th>Game ID's</th>
          </tr>
        </thead>
        <tbody>
          {data.map((gameID, index) => (
            <tr key={index}>
              <td>
              <Link to={`/game/${gameID}`}>{gameID}</Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default GameIDTable;
