import {Link} from 'react-router-dom';
import './login.css';
import votingImage from '../assets/login.png';
import {useState,useEffect} from 'react';
import axios from 'axios';


export default function RootLayout(){
    
    const [votingId,setVotingId]=useState('');
    

   const handleSubmission=(event)=>{      
    
    event.preventDefault();

    axios.post('https://hello.com',{votingId})
    .then(response=>console.log(response))
    .catch(error=>console.log(error))

   }


    return (
        <div className='login-container'>
            <div className="container">
                <div className="image-section">
                    <img src={votingImage} alt="Voting Illustration" />
                </div>
                <form className="form-section" >
                    <h2>Enter Your Voting ID</h2>
                    <input type="text" placeholder="Enter your Voting Id here" value={votingId} onChange={({target})=>{setVotingId(target.value)}} />
                    <div className="button-container">
                        <button onClick={handleSubmission}>Continue</button>
                    </div>
                </form>
            </div>
        </div>
      );
}
