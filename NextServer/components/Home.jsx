import { Route, Routes } from "react-router-dom";
import { Navigation2, Counter, Footer } from "cmm";
import { Schedule } from "cop";
import { Login, SignUp, UserList } from "uat";
import { Stroke } from "exrc/stroke";
import { Iris, Fashion, Number, AiTraders } from "exrc/dlearn";
import { NaverMovie } from "exrc/webcrawler";
import { Samsung, NaverGrade, KoreanClassify } from "exrc/nlp";

export default function Home(){
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
              
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            style={{ width: "20%", height: "80%", border: "1px solid black" }}
          >
            <td style={{ width: "100%", border: "1px solid black" }}>
              
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
