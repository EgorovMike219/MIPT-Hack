import React, { Component } from 'react'
import MenuLeft from './MenuLeft/MenuLeft';
import Example from './Example/Example'
import './WelcomePage.css';

class WelcomePage extends Component {
      render() {
        return (
          <div className='welcome'>
            <div className='menuleft'>
              <MenuLeft/>
            </div>
            <div className='example'>
              <Example/>
            </div>
          </div>
        );
      }
}

export default WelcomePage