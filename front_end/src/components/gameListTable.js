
import React, { useState, useEffect } from 'react';
import fetchOpenGameIDs from 'src/services/gameApi';


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
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default GameIDTable;
