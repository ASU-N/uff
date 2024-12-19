import './App.css';
import React from 'react';
import {Routes,Route,NavLink,Link,createBrowserRouter,createRoutesFromElements,RouterProvider} from 'react-router-dom';
import Kyc from './pages/kyc';
import RootLayout from './layout/RootLayout';
import HomeLayout from './layout/HomeLayout';
import About from './pages/about';
import Result from './pages/result';
import Login from './pages/login';
import NotFoundPage from './pages/pagenotfound';

const router=createBrowserRouter(
  createRoutesFromElements(
    <Route>
      <Route index element={<Login/>}/>
      <Route path='home' element={<HomeLayout/>}>
        <Route path='kyc' element={<Kyc/>}/>
        <Route path='result' element={<Result/>}/>
        <Route path='guidelines' element={<About/>}/>
      </Route>
      <Route path='*' element={<NotFoundPage/>}/>
    </Route>
  )
);



function App() {
return(
  <main>
  <RouterProvider router={router}/>
  </main>
);
}

export default App;