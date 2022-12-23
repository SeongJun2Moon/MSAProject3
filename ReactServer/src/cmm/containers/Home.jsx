import { Route, Routes } from "react-router-dom";
import { Navigation2, Counter, Footer } from "cmm";
import { Schedule } from "cop";
import { LoginForm, SignUp } from "uat";
import fasion from "img/fasion01.png";
import { Stroke } from "blog";
import { Iris, Fashion, Number } from "shop";
import { NaverMovie } from "webcrawler";
import { Samsung } from "nlp";

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
          <tr columns="3">
            <td style={{ width: "100%", border: "1px solid black" }}>
              <Navigation2 />
            </td>
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
                <Route path="/login" element={<LoginForm />}></Route>
                <Route path="/signup" element={<SignUp />}></Route>
                <Route path="/stroke" element={<Stroke />}></Route>
                <Route path="/iris" element={<Iris />}></Route>
                <Route path="/fashion" element={<Fashion />}></Route>
                <Route path="/number" element={<Number />}></Route>
                <Route path="/navermovie" element={<NaverMovie />}></Route>
                <Route path="/samsung" element={<Samsung />}></Route>
              </Routes>
            </td>
          </tr>
          <tr>
            <td>
              <img src={fasion} />
            </td>
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
