import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/home.css";

export const Navbar = () => {
	const { store, actions } = useContext(Context);
	return (
		<nav className="navbar navbar-light bg-light">
		<Link to="/">
		  <span className="navbar-brand mb-0 mx-3 h1">React Boilerplate</span>
		</Link>
		<div className="container d-flex justify-content-end mr-2">
		  {!store.token ? (
			<Link to="/login">
			  <button className="btn btn-primary">Login</button>
			</Link>
		  ) : (
			<Link to="/login">
			  <button
				className="btn btn-primary"
				onClick={() => actions.logout()}
			  >
				Logout
			  </button>
			</Link>
		  )}
		</div>
	  </nav>
	);
};
