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
          test: 1,
          login: '',
          password: '',
          requestingServer: false,
        };

        this.doTestEnabled = this.doTestEnabled.bind(this);
        this.setPicture = this.setPicture.bind(this);
        this.setTest = this.setTest.bind(this);
        this.setLoginPassword = this.setLoginPassword.bind(this);
        this.checkInput = this.checkInput.bind(this);
        this.checkInput();
      }

      doTestEnabled() {
        this.setState({ testEnabled: true });
      }

      checkInput() {
        if (this.state.picture &&
            this.state.test &&
            this.state.login !== '' && 
            this.state.password !== '') {
          // переключаемся в состояние ожидания ответа сервера
          this.setState({ requestingServer: true});
          console.log("Upload data");
          authenticationService.uploadData(this.state.login,
            this.state.password, this.state.picture, this.state.test
            ).then(data => {
              console.log(data);
              //помечаем что чувак все заполнил 
              // это делает authenticationService

              // записываем данные которые пришли
              this.props.getData(data, ()=>{
                  // говорим что ожидание закончилось
                  this.setState({ requestingServer: false});

                  // не знаю нормально будет работать 
                  // может это засунуть в getData
                  // перебрасываем на начальную стадию, которая делает проверки
                  const { from } = this.props.location.state || { from: { pathname: "/" } };
                  this.props.history.push(from);
                });
            }).catch(err => {
              // говорим что ожидание закончилось
              this.setState({ requestingServer: false});
              console.log("Error logging in", err);
          });
        }
      }

      setPicture(picture) {
        this.setState({ picture: picture 
        }, () => {
          this.checkInput();
        });
      }

      setTest(test) {
        this.setState({ 
          test: test,
          testEnabled: false 
        }, () => {
          this.checkInput();
        });
      }

      setLoginPassword(login, password) {
        this.setState({ 
          login: login,
          password: password
        }, () => {
           this.checkInput();
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
                    setLoginPassword={this.setLoginPassword}
                    doTestEnabled={this.doTestEnabled} />
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
