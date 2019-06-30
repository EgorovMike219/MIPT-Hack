import React, { Component } from 'react'
import { Button, Modal, Form } from 'react-bootstrap'
import './Auth.css';

class Auth extends Component {
	    constructor(props) {
        super(props);
        
        this.state = {
          login : "",      // UI element
          password: "",    // UI element
          requestingServer: false,  // page status
          warning: null,            // warning message to display
        };
    
        this.onSubmit          = this.onSubmit.bind(this);  // вызывается на вызов Submit, 
          // отправляет на проверку backend-у логин и пароль
        this.handleInputChange = this.handleInputChange.bind(this); // постоянно записывает ввод с клавиатуры
        this.handleError       = this.handleError.bind(this);  // вызывается когда в ответ от сервера пришла ошибка
      }
    
      handleError(message) {
        this.setState({ requestingServer: false, warning: 'warning' });
      }
    
      onSubmit(event) {
        console.log('submit');
        event.preventDefault();
        this.props.setLoginPassword(this.state.login, this.state.password);
        // закрываем окно
        this.props.handleClose();
      }
    
      handleInputChange(event) {
        switch (event.target.placeholder){
          case "Login":
            this.setState({ login: event.target.value});
            break;
          case "Password":
            this.setState({ password: event.target.value});
            break;
          default:
            console.log('default');
            break;
        }
      }
    
      render() {
        return (
          <Modal show={this.props.show} onHide={this.props.handleClose}>
              <Modal.Header closeButton>
                  <Modal.Title>Connect to GitHub</Modal.Title>
              </Modal.Header>
              <Modal.Body>
                <Form onSubmit={this.onSubmit}>
                  <Form.Group controlId="formBasicEmail">
                    <Form.Label>GitHub Login</Form.Label>
                    <Form.Control type="text" placeholder="Login" value={this.state.login}
                      onChange={this.handleInputChange} required autoFocus />
                    <Form.Text className="text-muted">
                      We'll never share your login with anyone else.
                    </Form.Text>
                  </Form.Group>

                  <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" value={this.state.password}
                      onChange={this.handleInputChange} required />
                  </Form.Group>
                  {this.state.requestingServer === true ?
                    <Button variant="dark" type="submit" disabled>Signing in...</Button>:
                    <Button variant="dark" type="submit">Submit</Button>
                  }
                </Form>
              </Modal.Body>
              <Modal.Footer>
                  { this.state.warning === null ||
                    <div className="alert alert-danger" role="alert">{this.state.warning}</div>
                  } 
              </Modal.Footer>
          </Modal>
        );
      }
}

export default Auth
