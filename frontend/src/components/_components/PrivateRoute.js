import React from 'react';
import { Route, Redirect } from 'react-router-dom';

import { authenticationService } from '../../services/Api/Api';

export const PrivateRoute = ({ component: Component, ...rest }) => (
    <Route {...rest} render={props => {
        // console.log(props);
        const user = authenticationService.getUser();
        if (!user) {
            // not logged in so redirect to login page with the return url
            return <Redirect to={{ pathname: '/login', state: { from: props.location } }} />
        }

        // authorised so return component
        return <Component {...props} {...rest} />
    }} />
)