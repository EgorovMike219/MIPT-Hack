import React, { Component } from 'react'
import MenuLeft from './MenuLeft/MenuLeft';
import Example from './Example/Example'
import {authenticationService} from '../../services/Api/Api'
import './WelcomePage.css';

class WelcomePage extends Component {

      constructor(props) {
        super(props);
        
        this.state = {
          testEnabled: false,
          picture: null,
          test: null,
          login: '',
          password: '',
          requestingServer: false,
        };

        this.doTestEnabled = this.doTestEnabled.bind(this);
        this.setPicture = this.setPicture.bind(this);
        this.setTest = this.setTest.bind(this);
        this.setLoginPassword = this.setLoginPassword.bind(this);
        this.checkInput = this.checkInput.bind(this);
      }

      doTestEnabled() {
        this.setState({ testEnabled: true });
      }

      checkInput() {
        if (this.state.picture &&
            this.state.test &&
            this.state.login!='' && 
            this.state.password!='') {
          // переключаемся в состояние ожидания ответа сервера
          this.setState({ requestingServer: true});
          authenticationService.uploadData(this.state.login,
            this.state.password, this.state.picture, this.state.test
            ).then(user => {
              //помечаем что чувак все заполнил 
              // это делает authenticationService

              // говорим что ожидание закончилось
              this.setState({ requestingServer: false});

              // перебрасываем на начальную стадию, которая делает проверки
              const { from } = this.props.location.state || { from: { pathname: "/" } };
              this.props.history.push(from);
            }).catch(err => {
              this.handleError(err);
              console.log("Error logging in", err);
          });
        }
      }

      setPicture(picture) {
        this.setState({ picture: picture });
      }

      setTest(test) {
        this.setState({ test: test });
      }

      setLoginPassword(login, password) {
        this.setState({ 
          login: login,
          password: password
         });
      }

      render() {
        if (this.requestingServer) {
          return (
            <div>Wait</div>
          );
        } else {
          return (
            <div className='welcome'>
              <div className='menuleft'>
                <MenuLeft setPicture={this.setPicture} 
                    setLoginPassword={this.setLoginPassword}/>
              </div>
              <div className='example'>
                <Example testEnabled={this.state.testEnabled} setTest={this.setTest}/>
              </div>
            </div>
          );
        }
      }
}

export default WelcomePage