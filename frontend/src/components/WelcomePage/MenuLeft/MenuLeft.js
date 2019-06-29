import React, { Component } from 'react'
import ImageUploader from 'react-images-upload'
import { Button} from 'react-bootstrap'
import Auth from '../Auth/Auth'
import './MenuLeft.css'

class MenuLeft extends Component {
    // нужно проверить что выолнены все условия
    // чувак залогинился на гитхабе
    // чувак загрузил фотку
    // чувак прошел тест
	constructor(props) {
        super(props);

        this.state = { 
            pictures: [],
            show: false, 
        };

        this.connectToGitHub = this.connectToGitHub.bind(this);
        this.uploadPhoto = this.uploadPhoto.bind(this);
        this.passTest = this.passTest.bind(this);
        this.handleShow = this.handleShow.bind(this);
        this.handleClose = this.handleClose.bind(this);

      }
    
      connectToGitHub(event) {
          console.log("connect to gitHub")
      }
    
      uploadPhoto(picture) {
        console.log("uploadPhoto");
        this.setState({
            pictures: this.state.pictures.concat(picture),
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