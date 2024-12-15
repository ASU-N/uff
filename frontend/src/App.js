import './App.css';
import React from 'react';
import {Routes,Route,NavLink,Link,createBrowserRouter,createRoutesFromElements,RouterProvider} from 'react-router-dom';
import Kyc from './pages/kyc';
import RootLayout from './layout/RootLayout';
import HomeLayout from './layout/HomeLayout';
import About from './pages/about';
import Result from './pages/result';

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<RootLayout />}>
      <Route path="about" element={<About />} />
      <Route path="home" element={<HomeLayout />}>
        <Route path="kyc" element={<Kyc />} />
        <Route path="result" element={<Result />} />
        <Route path="guidelines" element={<About />} />
      </Route>
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