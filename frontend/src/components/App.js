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

    constructor(props) {
        super(props);

        this.state = { 
            data: null, 
        };
        this.getData = this.getData.bind(this);
    }
    
    getData(data) {
        this.setState({data: data})
    }

    render() {
        return (
            <Router history={history}>
                <div className='app-container'>
					<PrivateRoute exact path="/" component={MainPage} data={this.state.data} />
                    <Route path="/login"
                        render={(props) => <WelcomePage {...props} getData={this.getData}/>} />
                </div>
            </Router>
        );
    }
}

export default App;