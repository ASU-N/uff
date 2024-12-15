import {NavLink} from 'react-router-dom';
import {useState} from 'react';

export default function HomeLayout(){
    
    const [timer,setTimer]=useState("00:00:00");
    
    
    return(
        <div className='root-layout'>
            <header></header>
            <main>
                <nav>
                    <img></img>


                </nav>
                <section>
                    

                </section>
            </main>
        </div>
    )
};