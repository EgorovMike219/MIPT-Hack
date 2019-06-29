import React, { Component } from 'react'
import {authenticationService} from '../../../services/Api/Api'
import { Button, Modal } from 'react-bootstrap'
import './Auth.css';

class Auth extends Component {
  // в пропах show, handleClose
	constructor(props) {
        super(props);
        
        this.state = {
          login : "",      // UI element
          password: "",    // UI element
          requestingServer: false,  // page status
          warning: null,            // warning message to display
        };
    
        this.onButton          = this.onButton.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleError       = this.handleError.bind(this);
        // redirect to home if already logged in
        if (authenticationService.getCurrentUser()) { 
            this.props.history.push('/');
        }
      }
    
      handleError(message) {
        this.setState({ requestingServer: false, warning: 'warning' });
      }
    
      onButton(event) {
        event.preventDefault();
        // переключаемся в состояние ожидания ответа сервера
        this.setState({ requestingServer: true, warning: null });
        authenticationService.signIn(
          this.state.login, 
          this.state.password,
          this.state.remember
          ).then(user => {
            const { from } = this.props.location.state || { from: { pathname: "/" } };
            this.props.history.push(from);
          }).catch(err => {
            this.handleError(err);
            console.log("Error logging in", err);
        });
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
                <form className="form-signin" onSubmit={this.onButton}>
                  <h1 className="h3 mb-3 font-weight-normal"> Please sign in </h1> 
                  <label htmlFor="inputLogin" className="sr-only">
                  Login
                  </label>
                  <input type="text" id="inputLogin" className="form-control"
                  placeholder="Login" value={this.state.login}
                  onChange={this.handleInputChange} required autoFocus />
                  <label htmlFor="inputPassword" className="sr-only">
                    Password
                  </label>
                    <Button variant="secondary" onClick={this.handleClose}>
                  Close
                  </Button>
                  <Button variant="primary" onClick={this.handleClose}>
                  Save Changes
                  </Button>
                    </form>
                <Form>
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
                    <Button variant="primary" type="submit" disabled>Signing in...</Button>:
                    <Button variant="primary" type="submit">Sign in</Button>
                  }
                </Form>
              </Modal.Body>
              <Modal.Footer>
                  <Button variant="secondary" onClick={this.props.handleClose}>
                  Close
                  </Button>
                  { this.state.warning === null ||
                    <div className="alert alert-danger" role="alert">{this.state.warning}</div>
                  } 
              </Modal.Footer>
          </Modal>
        );
      }
}

export default Auth