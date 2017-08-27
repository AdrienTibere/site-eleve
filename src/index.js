import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import {Provider} from 'react-redux';
import mainReducer from './reducers.js'
import thunkMiddleware from 'redux-thunk'
import { createLogger } from 'redux-logger'
import { createStore, applyMiddleware } from 'redux'

const loggerMiddleware = createLogger()

let store = createStore(
  mainReducer,
  applyMiddleware(
    thunkMiddleware, // lets us dispatch() functions
//    loggerMiddleware // neat middleware that logs actions
  )
)

ReactDOM.render(
  <Provider store={store}>
    <App />  
  </Provider>
, document.getElementById('root'));
registerServiceWorker();
