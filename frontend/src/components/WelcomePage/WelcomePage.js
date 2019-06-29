import React, { Component } from 'react'
import MenuLeft from './MenuLeft/MenuLeft';
import Example from './Example/Example'
import './WelcomePage.css';

class WelcomePage extends Component {

      constructor(props) {
        super(props);
        
        this.state = {
          testEnabled: false
        };

        this.doTestEnabled = this.doTestEnabled.bind(this);  
      }

      doTestEnabled() {
        this.setState({ testEnabled: true });
      }

      render() {
        return (
          <div className='welcome'>
            <div className='menuleft'>
              <MenuLeft/>
            </div>
            <div className='example'>
              <Example testEnabled={this.state.testEnabled}/>
            </div>
          </div>
        );
      }
}

export default WelcomePage