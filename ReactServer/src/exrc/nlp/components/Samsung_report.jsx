import { useState } from "react";
import webcrawlerService from "../api";
const Samsung = () => {
  const [movie, setMovie] = useState();

  const onClick = (e) => {
    e.preventDefault();
    webcrawlerService.samsungWords().then((res) => {
      const json = JSON.parse(res); // JSON.parse : json을 js객체로 바꿈 =>.이나 []로 내부 데이터 접근 가능 <-> JSON.stringify()
      setMovie(json["result"]);
      console.log(json["result"]);
    });
  };

  return (
    <>
      <h2>samsung</h2>
      <button onClick={onClick}>Click</button>
      <p>버튼을 클릭하시면, samsung words index이 출력됩니다.</p>
      {
        <table>
          <th>rank</th>
          <th>word</th>
          <th>count</th>
          {movie &&
            movie.map(({ rank, word, count }) => (
              <tr key={rank}>
                <td>{rank}</td>
                <td>{word}</td>
                <td>{count}</td>
              </tr>
            ))}
        </table>
      }
    </>
  );
};
export default Samsung;
