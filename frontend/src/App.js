import './App.css';
import React from 'react';
import {Routes,Route,NavLink,Link,createBrowserRouter,createRoutesFromElements,RouterProvider} from 'react-router-dom';
import Kyc from './pages/kyc';
import HomeLayout from './layout/HomeLayout';
import About from './pages/about';
import Result from './pages/result';
import NotFoundPage from './pages/notfoundpage'
import Login from './pages/login';
import Guidelines from './pages/guidelines';
import Home from './pages/home';

const router=createBrowserRouter(
  createRoutesFromElements(
    <Route>
      <Route index element={<Login/>}/>
      <Route path='/home' element={<HomeLayout/>}>
        <Route index element={<Home/>}/>
        <Route path='kyc' element={<Kyc/>}/>
        <Route path='result' element={<Result/>}/>
        <Route path='guidelines' element={<Guidelines/>}/>
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