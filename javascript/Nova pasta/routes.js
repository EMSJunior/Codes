import { Fragment } from 'react';
import {BrowserRouter, Route, Routes } from "react-router-dom";
import home from "./pages/home"
import signIn from "./pages/signIn"
import signUp from "./pages/signUp"

const Private = ({ Item })  =>{
  const signed = false;

  return signed > 0 ? <Item /> : <signIn />
};


const RoutesApp = () => {
  return (
    <BrowserRouter>
      <Fragment>
        <Routes>
          <Route exact path="/home" element={<Private Item={home} />} />
          <Route path="/" element={<signIn />} />
          <Route extact path="/signUp" element={<signUp />} />
          <Route path="*" element={<signIn />} />


        </Routes>
      </Fragment>
    </BrowserRouter>
  );
};

export default RoutesApp;