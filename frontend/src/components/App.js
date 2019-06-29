import React, { Component } from 'react';
import { Router, Route} from 'react-router-dom';
import WelcomePage from './WelcomePage/WelcomePage';
import MainPage from './MainPage/MainPage';
import { history } from './_components/history';
import {authenticationService} from '../services/Api/Api'
import { PrivateRoute } from './_components/PrivateRoute';
import './App.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'font-awesome/css/font-awesome.css'


class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            currentUser: authenticationService.getCurrentUser(),
        };
        this.logout = this.logout.bind(this);
    }

    logout(event) {
		authenticationService.logout();
		this.setState({ currentUser: authenticationService.getCurrentUser()});
        history.push('/login');
    }

    render() {
        // надо разобраться с шириной и высотой
        // ширина зависит от контента, поэтому прыгает при смене чат комнат
        return (
            <Router history={history}>
                <div className='app-container'>
					<PrivateRoute exact path="/" component={MainPage} logout={this.logout} />
					<Route path="/login" component={WelcomePage} />
                </div>
            </Router>
        );
    }
}

export default App;