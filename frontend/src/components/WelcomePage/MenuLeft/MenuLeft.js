import React, { Component } from 'react'
import ImageUploader from 'react-images-upload'
import { Button} from 'react-bootstrap'
import Auth from '../Auth/Auth'
import {authenticationService} from '../../../services/Api/Api'
import './MenuLeft.css'

class MenuLeft extends Component {
    // нужно проверить что выолнены все условия
    // чувак залогинился на гитхабе
    // чувак загрузил фотку
    // чувак прошел тест
	constructor(props) {
        super(props);

        this.state = { 
            picture: null,
            show: false, 
        };

        this.connectToGitHub = this.connectToGitHub.bind(this);
        this.onDrop = this.onDrop.bind(this);
        this.passTest = this.passTest.bind(this);
        this.handleShow = this.handleShow.bind(this);
        this.handleClose = this.handleClose.bind(this);

      }
    
      connectToGitHub(event) {
          console.log("connect to gitHub")
      }
    
      onDrop(picture) {
        console.log("uploadPhoto");
        console.log(picture);
        this.setState({
            picture: picture,
        });
        authenticationService.loadImage(picture[0])
          .then(response => {
            this.setState({ 
              uploading: false,
            })
          })
          .catch(err => {
              this.setState({ 
                uploading: false,
              });
              console.log("Error logging in", err);
        });
      }
      handleClose() {
        this.setState({ show: false });
      }
    
      handleShow() {
        this.setState({ show: true });
      }

      passTest(event) {
        console.log("pass the test")
      }
    
      render() {
        return (
          <div className="text-center">
                <div className="buttons-form">
                    {/* <!-- Кнопка пуска модальное окно --> */}
                    <Button variant="dark" onClick={this.handleShow}>
                        Connect to GitHub
                    </Button>
                    {/* <!-- Модальное окно авторизации -->   */}
                    <Auth show={this.state.show} handleClose={this.handleClose}/>
                    <ImageUploader
                        withIcon={true}
                        buttonText='Choose images'
                        onChange={this.uploadPhoto}
                        imgExtension={['.jpg', '.gif', '.png', '.gif']}
                        maxFileSize={5242880}
                    />
                    <Button 
                        onClick={this.passTest}
                    >Pass the Test</Button>
                </div>
          </div>
        );
      }
}

export default MenuLeft