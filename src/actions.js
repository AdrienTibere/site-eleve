import fetch from 'isomorphic-fetch'
import {server_url} from './config.js';

export const LOG_IN = 'LOG_IN';
export function logIn(user) {
  return {
    type: LOG_IN,
    user: user
  }
}

export const LOG_OUT = 'LOG_OUT';
export function logOut() {
  return {
    type: LOG_OUT
  }
}

export const SET_REDIRECT_URL = 'SET_REDIRECT_URL';
export function setRedirectUrl(newUrl = '/') {
  return {
    type: SET_REDIRECT_URL,
    newUrl: newUrl
  }
}

export const AUTHENTICATE_USER = 'AUTHENTICATE_USER';
export function authenticateUser(user) {
  return {
    type: AUTHENTICATE_USER,
    user: user
  }
}

export const REQUEST_LOG_IN = 'REQUEST_LOG_IN'
function requestLogIn() {
  return {
    type: REQUEST_LOG_IN
  }
}

export const RECEIVE_LOG_IN = 'RECEIVE_LOG_IN'
function receiveLogIn(json) {
  return {
    type: RECEIVE_LOG_IN,
    user: json
  }
}

// Though its insides are different, you would use it just like any other action creator:
// store.dispatch(fetchLogIn())
export function fetchLogIn(formData) {
  return function (dispatch) {
    dispatch(requestLogIn());
    return fetch(server_url + 'api/login',
      {
        method: 'POST',
        body:formData
      })
      .then(
        response => response.json(),
        error => console.log('An error occured.', error)
      )
      .then(json =>
        dispatch(receiveLogIn(json))
      )
  }
}
