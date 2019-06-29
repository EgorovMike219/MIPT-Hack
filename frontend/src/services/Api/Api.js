const SERVER = 'http://localhost:8080';
// Upload data
const API_UPLOAD = '/upload';

// Get result
const API_RESULT = '/result';


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
    uploadData,
    getResult,
    getUser
};

function uploadData(login, password, picture, test) {
    return fetch(SERVER + API_UPLOAD, {
            method: 'post',
            body: JSON.stringify({login: login, password: password, picture: picture, test: test}),
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

function getResult() {
    return fetch(SERVER + API_RESULT, {
            method: 'get',
            headers: { 'content-type': 'application/json'}
        })
        .then(fetchStatusCheck);
    // не забыть поймать искючения в месте где вызываю метод
}

function getUser() { 
    // если в хранилище нет login false - 
    // это означает пользователь не закончил заполнять о себе данные
    if (sessionStorage.getItem('login'))
        return true;
    else {
        return false;
    }
}
