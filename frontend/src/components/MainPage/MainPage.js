import React, { Component } from 'react';
import './MainPage.css';


class MainPage extends Component {

    render() {
        this.props.logout();
        return (
            <div>
                MainPage
            </div>
        );
    }
}


export default MainPage