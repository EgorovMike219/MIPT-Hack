const SERVER = 'http://messenger.westeurope.cloudapp.azure.com';
// Authentication
const API_SIGNIN = '/api/authentication/signin';
const API_SIGNUP = '/api/authentication/signup';
//Conversations
const API_CONVERSATIONS = '/api/conversations';
function get_user_conservartions(userId) {
    return `/api/conversations/${userId}/messages`;
}
const API_PUBLIC_MESSAGES = '/api/conversations/public/messages';
//Users
function get_user_info(userId) {
    return `/api/users/${userId}`;
}
const API_ME = '/api/users/me';
const API_FIND_USER = '/api/users';

function API_WEBSOCKET() {
    return 'ws://messenger.westeurope.cloudapp.azure.com/socket/messages?token=';
}

function fetchStatusCheck(response) {
    // console.log(response)
    if (!response.ok) {
        if ([401, 403].indexOf(response.status) !== -1) {
            // это ошибки связанные с авторизацией
            console.log(response.status);
            // window.location.reload(true);
        }
        const error = response.text() || response.statusText;
        return Promise.reject(error);
    }
    return response.json();
  }

// Requests
export const authenticationService = {
    signIn,
    getUser,
    getPublicMessages,
    postPrivateMessages,
};

function signIn(login, password, remember) {
    return fetch(SERVER + API_SIGNIN, {
            method: 'post',
            body: JSON.stringify({login: login, password: password}),
            headers: { 'content-type': 'application/json' }
            })
        .then(fetchStatusCheck)
        .then(user => {
            // запоминаем пользователя
            sessionStorage.setItem('login', login);
            return user;
            }
        );
    // не забыть поймать искючения в месте где вызываю метод
}

function getUser() { 
    // если в хранилище нет login или картинки или теста возвращается false
    if (sessionStorage.getItem('login') && sessionStorage.getItem('face')
        && sessionStorage.getItem('test'))
        return true;
    else {
        return false;
    }
}

function getPublicMessages() {
    return fetch(SERVER + API_PUBLIC_MESSAGES, {
            method: 'get',
            headers: { 'content-type': 'application/json', 'Authorization': 'Bearer ' }
        })
        .then(fetchStatusCheck);
    // не забыть поймать искючения в месте где вызываю метод
}


function postPrivateMessages(id, message) {
    return fetch(SERVER + get_user_conservartions(id), {
            method: 'post',
            body: JSON.stringify({content: message}),
            headers: { 'content-type': 'application/json', 'Authorization': 'Bearer'}
        })
        .then(fetchStatusCheck)
        .then(function(json) {
            return [json, id]
        });
    // не забыть поймать искючения в месте где вызываю метод
}

