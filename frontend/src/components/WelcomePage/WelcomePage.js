import React, { Component } from 'react'
import Auth from './Auth/Auth';
import Example from './Example/Example'
import './WelcomePage.css';

class WelcomePage extends Component {
      render() {
        return (
          <div className='welcome'>
            <div className='auth'>
              <Auth/>
            </div>
            <div className='example'>
              <Example/>
            </div>
          </div>
        );
      }
}

export default WelcomePage