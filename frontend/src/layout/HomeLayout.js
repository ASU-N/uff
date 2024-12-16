import {NavLink,Outlet} from 'react-router-dom';
import {useState} from 'react';
import profile from '../assets/home_profile.jpg';
import './HomeLayout.css'

export default function HomeLayout(){
    
    const [hours,setHour]=useState(0);
    const [minutes,setMinute]=useState(0);
    const [seconds,setSecond]=useState(0);

    
    
    return(
        <div className='root-layout'>
            <header>
                <nav className='homeNavBar'>
                    <NavLink to="/home" className={({isActive})=>(isActive?"active":"")}>Home</NavLink>
                    <NavLink to="/home/kyc" className={({isActive})=>(isActive?"active":"")}>Know Your Candidates</NavLink>
                    <NavLink to="/home/result" className={({isActive})=>(isActive?"active":"")}>Results</NavLink>
                    <NavLink to="/home/guidelines" className={({isActive})=>(isActive?"active":"")}>Guidelines</NavLink>
                    <button><img src={profile} alt='Voters Profile'/></button>
                </nav>
            </header>
            <main>
                <nav className='timerNavBar'>
                    <h1>Ends In:</h1>

                </nav>
                <section>
                <Outlet/>
                </section>
                
            </main>
        </div>
    )
};