import React, { Component } from 'react'
import ImageUploader from 'react-images-upload'
import { Button} from 'react-bootstrap'
import Auth from '../Auth/Auth'
import './MenuLeft.css'

class MenuLeft extends Component {
	constructor(props) {
        super(props);

        this.state = { 
            picture: null,
            show: false, 
        };

        this.onDrop = this.onDrop.bind(this);
        this.passTest = this.passTest.bind(this);
        this.handleShow = this.handleShow.bind(this);
        this.handleClose = this.handleClose.bind(this);

      }
    
      onDrop(picture) {
        console.log("uploadPhoto");
        console.log(picture);
        this.setState({
            picture: picture,
        });
        this.props.setPicture(picture);
      }
      handleClose() {
        this.setState({ show: false });
      }
    
      handleShow() {
        this.setState({ show: true });
      }

      passTest(event) {
        console.log("pass the test");
        event.preventDefault();
        this.props.doTestEnabled();
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
                    <Auth show={this.state.show}
                      handleClose={this.handleClose}
                      setLoginPassword={this.props.setLoginPassword}/>
                    <ImageUploader
                        withIcon={true}
                        buttonText='Choose images'
                        onChange={this.onDrop}
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