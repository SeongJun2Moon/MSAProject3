import { Route, Routes } from "react-router-dom";
import { Navigation2, Counter, Footer } from "cmm";
import { Schedule } from "cop";
import { Login, SignUp, UserList } from "uat";
import fashion from "img/fasion01.png";
import { Stroke } from "exrc/stroke";
import { Iris, Fashion, Number } from "exrc/dlearn";
import { NaverMovie } from "exrc/webcrawler";
import { Samsung, NaverGrade } from "exrc/nlp";

const Home = () => {
  return (
    <>
      <table
        style={{
          width: "1200px",
          height: "550px",
          margin: "0 auto",
          border: "1px solid black",
        }}
      >
        <thead>
          <tr columns="1">
            <th style={{ width: "100%", border: "1px solid black" }}>
              <Navigation2 />
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            style={{ width: "20%", height: "80%", border: "1px solid black" }}
          >
            <td style={{ width: "100%", border: "1px solid black" }}>
              <Routes>
                <Route path="/counter" element={<Counter />}></Route>
                <Route path="/todos" element={<Schedule />}></Route>
                <Route path="/login" element={<Login />}></Route>
                <Route path="/signup" element={<SignUp />}></Route>
                <Route path="/stroke" element={<Stroke />}></Route>
                <Route path="/iris" element={<Iris />}></Route>
                <Route path="/fashion" element={<Fashion />}></Route>
                <Route path="/number" element={<Number />}></Route>
                <Route path="/navermovie" element={<NaverMovie />}></Route>
                <Route path="/samsung" element={<Samsung />}></Route>
                <Route path="/navergrade" element={<NaverGrade />}></Route>
                <Route path="/userlist" element={<UserList />}></Route>
              </Routes>
            </td>
          </tr>
          <tr>
            <td>{/* <img src={fashion} /> */}</td>
          </tr>
          <tr
            style={{ width: "100%", height: "20%", border: "1px solid black" }}
          >
            <td style={{ width: "100%", border: "1px solid black" }}>
              <Footer />
            </td>
          </tr>
        </tbody>
      </table>
    </>
  );
};
export default Home;
