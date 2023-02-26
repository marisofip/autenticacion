import React, { useContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/home.css";

export const Login = () => {
    const { store, actions } = useContext(Context);
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");    
    const navigate = useNavigate();

    console.log("This is your token", store.token);
    const handleClick = () => {
        actions.login(email, password)
    }

    useEffect(() => {
        if (store.token) {
          navigate("/")
        }
      }, [store.token])
	return (
		<div className="text-center mt-5">
			<h1>Login</h1>
            {store.token ? (
                <p>You are logged in with the token {store.token}</p>
             ) : (
                <div>
                    <input type="text" value={email} placeholder="email" onChange={(e) => setEmail(e.target.value)}/>
                    <input type="password" value={password} placeholder="password"onChange={(e) => setPassword(e.target.value)}/>
                    <button onClick={handleClick}>Login</button>
                </div>
    )}
		</div>
	);
};