import { Fragment } from 'react';
import {BrowserRouter, Route, Routes } from "react-router-dom";
import home from "../pages/Home"
import Signin from "../pages/Signin"
import Signup from "../pages/Signup"
import useAuth from "../hooks/useAuth"

const Private = ({ Item })  =>{
  const {signed} = useAuth();

  return signed > 0 ? <Item /> : <signIn />
};


const RoutesApp = () => {
  return (
    <BrowserRouter>
      <Fragment>
        <Routes>
          <Route exact path="/home" element={<Private Item={home} />} />
          <Route path="/" element={<Signin />} />
          <Route extact path="/Signup" element={<Signup />} />
          <Route path="*" element={<Signin />} />


        </Routes>
      </Fragment>
    </BrowserRouter>
  );
};

export default RoutesApp;