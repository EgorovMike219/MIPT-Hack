import React, { Component } from 'react';
import { Router, Route} from 'react-router-dom';
import WelcomePage from './WelcomePage/WelcomePage';
import MainPage from './MainPage/MainPage';
import { history } from './_components/history';
import { PrivateRoute } from './_components/PrivateRoute';
import './App.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'font-awesome/css/font-awesome.css'


class App extends Component {

    render() {
        return (
            <Router history={history}>
                <div className='app-container'>
					<PrivateRoute exact path="/" component={MainPage} />
					<Route path="/login" component={WelcomePage} />
                </div>
            </Router>
        );
    }
}

export default App;