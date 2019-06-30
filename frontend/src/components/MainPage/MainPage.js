import React, { Component } from 'react';
import './MainPage.css';
import TableV from './Table'


class MainPage extends Component {
    constructor(props){
        super(props);
    }

    componentDidUpdate(prevProps) {
        if(prevProps.data !== this.props.data) {
          // У this.props.myProp изменилось значение
          // Поэтому мы можем выполнять любые операции для которых
          // нужны новые значения и/или выполнять сайд-эффекты
          // вроде AJAX вызовов с новым значением - this.props.myProp
          this._chart = TableV.create(
            this._rootNode,
            this.props.data
        );
        }
      }
	componentDidMount() {
        if (this.props.data) {
            this._chart = TableV.create(
                this._rootNode,
                this.props.data
            );
        }
    }

    _setRef(componentNode) {
        this._rootNode = componentNode;
    }


    render() {	
        return <svg height="500"  viewBox="-300 -300 665 665" ref={this._setRef.bind(this)} />
    }
}


export default MainPage