import React, { Component } from 'react';
import './MainPage.css';
import TableV from './Table'


class MainPage extends Component {
	componentDidMount() {
        this._chart = TableV.create(
            this._rootNode,
            this.props.loadData,
            this.props.readyToLoad,
            this.props.onChangeLoading
        );
    }

    _setRef(componentNode) {
        this._rootNode = componentNode;
    }


    render() {	
        return <svg height="500"  viewBox="-300 -300 665 665" ref={this._setRef.bind(this)} />
    }
}


export default MainPage