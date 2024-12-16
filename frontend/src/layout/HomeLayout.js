import {NavLink,Outlet} from 'react-router-dom';
import {useState} from 'react';
import profile from '../assets/home_profile.jpg';

export default function HomeLayout(){
    
    const [timer,setTimer]=useState("00:00:00");
    
    
    return(
        <div className='root-layout'>
            <header>
                <nav>
                    <NavLink to="/home">Home</NavLink>
                    <NavLink to="/home/kyc">Know Your Candidates</NavLink>
                    <NavLink to="/home/result">Results</NavLink>
                    <NavLink to="/home/guideline">Guidelines</NavLink>
                </nav>
            </header>
            <main>
                <nav>
                    <img src={profile} alt='Voters Profile'/>




                </nav>
                <section>
                <Outlet/>
                </section>
                
            </main>
        </div>
    )
};